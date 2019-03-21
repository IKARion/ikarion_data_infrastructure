import datetime
from collections import abc
import pytz
import bdateutil.parser as dp
import ikarion_data_management.data_access_layer.model_db_access_layer.group_model_dao as gmd

RELVANT_MODEL_OBJECT_TYPES = [
    "wiki",
    "forum",
]


def convert_timestamp(statement):
    """
    converts xapi_statements weird timestamp format to epoch time timestamps
    :param statement:
    :type statement:
    :return:
    :rtype:
    """
    timestamp = statement["timestamp"]
    if isinstance(timestamp, float):
        return timestamp
    # year, month, rest = timestamp.split("-")
    # day, rest = rest.split("T")
    # hours = rest[0:2]
    # minutes = rest[3:5]
    # seconds = rest[6:8]
    #
    # date_time = datetime.datetime(int(year),
    #                               int(month),
    #                               int(day),
    #                               int(minutes),
    #                               int(hours),
    #                               int(seconds),
    #                               tzinfo=pytz.utc)
    # epoch_timestamp = date_time.timestamp()
    epoch_timestamp = dp.parse(timestamp).timestamp()
    statement["timestamp"] = epoch_timestamp
    return epoch_timestamp


def nested_json_extensions(nested):
    """
    yields any map that has a extentions key
    :param nested:
    :type nested:
    :return:
    :rtype:
    """
    if isinstance(nested, abc.Mapping):
        if "extensions" in nested:
            yield nested
        for value in nested.values():
            yield from nested_json_extensions(value)
    if isinstance(nested, list):
        for value in nested:
            yield from nested_json_extensions(value)


def nested_data(nested):
    """
    yields any map that has a extentions key
    :param nested:
    :type nested:
    :return:
    :rtype:
    """
    if isinstance(nested, abc.Mapping):
        yield nested
        for value in nested.values():
            yield from nested_data(value)
    if isinstance(nested, list):
        for value in nested:
            yield from nested_data(value)


def replace_dots(statement):
    """
    Replace Dots in xapi statement keys because it violates
    MongoDB Key naming constraints.
    :param statement:
    :type statement:
    :return:
    :rtype:
    """
    for statement_map in nested_data(statement):
        for key in statement_map.keys():
            if "." in key:
                value = statement_map[key]
                replaced_key = key.replace(".", "__dot__")
                statement_map[replaced_key] = value
                statement_map.pop(key, None)


def statement_relevant(statement):
    # TODO find out what statements are not relevant and filter them.
    return True


def restructure_extensions(statement):
    extentions_list = nested_json_extensions(statement)
    for extensions_map in extentions_list:
        extensions = extensions_map["extensions"]
        mongo_compliant_extensions = []
        for k, v in extensions.items():
            if isinstance(v, list):
                v = {}
            v["id"] = k
            mongo_compliant_extensions.append(v)
        extensions_map["extensions"] = mongo_compliant_extensions


def process_groups(statement):
    extensions = statement["context"]["extensions"]

    group_ext_id = "http://collide.info/extensions/group"

    extensions = [item for item in extensions if item["id"] == group_ext_id]
    groups = []
    for extension in extensions:
        for k, v in extension.items():
            if k != "id":
                groups.append(v)
    statement["context"]["groups"] = groups


def extract_course_id(statement):
    groupings = statement["context"]["contextActivities"]["grouping"]
    course_type = "http://lrs.learninglocker.net/define/type/moodle/course"
    # for grouping in groupings:
    #     if grouping["definition"]["type"] == course_type:
    #         return grouping["id"]
    site = groupings[0]["id"]
    course_extention_url = "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log"
    course_extension = [item for item in statement["context"]["extensions"]
                        if item["id"] == course_extention_url][0]
    courseid = course_extension["courseid"]

    full_id_template = "{}/course/view.php?id={}"
    return full_id_template.format(site, courseid)
    # return courseid

def extract_course_name(statement):
    groupings = statement["context"]["contextActivities"]["grouping"]
    course_type = "http://lrs.learninglocker.net/define/type/moodle/course"
    course_name = ""
    for grouping in groupings:
        if grouping["definition"]["type"] == course_type:
            course_name = list(grouping["definition"]["name"].values())[0]

    object = statement["object"]
    if object["definition"]["type"] == course_type:
        course_name = list(object["definition"]["name"].values())[0]
    return course_name


def project_fields(statement):
    """
    Make certain data fields of xapi statemements
    easier to query
    :param statements:
    :type statements:
    :return:
    :rtype:
    """

    course_id = extract_course_id(statement)
    course_name = extract_course_name(statement)
    statement["course_id"] = course_id
    statement["course_name"] = course_name

def write_new_groups_and_tasks(statement):
    # courseid = extract_course_id(statement)
    courseid = statement["course_id"]
    groups = statement["context"]["groups"]
    for group in groups:
        task = group["task"]
        task["courseid"] = courseid
        group["courseid"] = courseid
        gmd.update_group(group, courseid)
        gmd.update_group_task(task, courseid)


def determine_relevant_task(statement):
    # is it a self assessment statement?
    self_id = "http://lrs.learninglocker.net/define/extensions/moodle_block"
    obj_name = "Groupactivity self assessment"

    self_assessment = False
    obj = statement["object"]
    if list(obj["definition"]["name"].values())[0] == obj_name:
        self_assessment = True

    groups = statement["context"]["groups"]
    statement["relevant_group_task"] = {}
    groupings = statement["context"]["contextActivities"]["grouping"]
    statement_time = statement["timestamp"]
    if self_assessment:
        for group in groups:
            task = group["task"]
            task_start = int(task["task_start"])
            task_end = int(task["task_end"])
            if task_start < statement_time < task_end:
                statement["relevant_group_task"] = group
    else:
        for group in groups:
            task = group["task"]
            task_modules = task["task_resources"]
            for grouping in groupings:
                if grouping["id"] in task_modules:

                    task_start = int(task["task_start"])
                    task_end = int(task["task_end"])
                    if task_start < statement_time < task_end:
                        statement["relevant_group_task"] = group
                        break


def process_statement(statement):
    restructure_extensions(statement)
    replace_dots(statement)
    convert_timestamp(statement)
    project_fields(statement)
    process_groups(statement)
    write_new_groups_and_tasks(statement)
    determine_relevant_task(statement)


def relevant_model_change(statement):
    object_type = statement["object"]["definition"]["type"]
    verb_id = statement["verb"]["id"]

    if relevant_object_type(object_type) and relevant_verb(verb_id):
        return True
    else:
        return False


def relevant_object_type(type):
    for relevant_type in RELVANT_MODEL_OBJECT_TYPES:
        if relevant_type in type:
            return True
    return False


def relevant_verb(verb_id):
    if "view" in verb_id:
        return False
    else:
        return True
