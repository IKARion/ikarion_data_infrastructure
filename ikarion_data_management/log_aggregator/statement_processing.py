import datetime
from bs4 import BeautifulSoup
import traceback
from collections import abc, Counter
import sys
import pytz
import bdateutil.parser as dp
import ikarion_data_management.data_access_layer.model_db_access_layer.group_model_dao as gmd

RELVANT_MODEL_OBJECT_TYPES = [
    "wiki",
    "forum",
]

context = ["context"]
context_logstore_extensions = ["http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log"]
# Get "courseid" out of this
logstore_full_path = context + ["extensions"] + context_logstore_extensions
# List of groupings first one being moodle data
# gouping[0] get id (moodleurl) and name[countrycode](moodle name)
context_grouping_data = ["contextActivities", "grouping"]

log_store_ext = "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log"
log_store_keys = ["context", "extensions", log_store_ext]

timestamp = "timestamp"
verb = "verb"
object = "object"
actor = "actor"


def get_nested_value(dictionary, keys):
    current_val = dictionary
    for key in keys:
        current_val = current_val[key]
    return current_val


def get_moodle_data(statement):
    keys = context_grouping_data + [0]
    moodle_grouping = get_nested_value(statement, keys)
    moodle_url = moodle_grouping["id"]
    moodle_name = list(moodle_grouping["definition"]["name"].values())[0]
    return {"url": moodle_url, "name": moodle_name}


def get_course_data(statement):
    obj_type = statement["object"]["definition"]["type"]
    course_type = "http://lrs.learninglocker.net/define/type/moodle/course"
    course_is_object = obj_type == course_type
    if course_is_object:
        keys = ["object", "definition"]
        obj_def = get_nested_value(statement, keys)
        name = list(obj_def["name"].values())[0]
        description = list(obj_def["description"].values())[0]
        id = statement["object"]["id"]
    else:
        keys = log_store_keys + [1]
        course_grouping = get_nested_value(statement, keys)
        obj_def = course_grouping["definition"]
        name = list(obj_def["name"].values())[0]
        description = list(obj_def["description"].values())[0]
        id = course_grouping["id"]

    res = {
        "name": name,
        "id": id,
        "description": description
    }

    return res


def get_group_task_data(statement):
    group_extension = "http://collide.info/extensions/group"
    keys = ["context", "extensions", group_extension]
    group_task_data = get_nested_value(statement, keys)
    res_list = []
    for k, v in group_task_data.items():
        group_id = k
        task = v["task"]
        group_members = v["group_members"]
        group_members = [item["name"] for item in group_members]
        res = ({"id": group_id}, task, group_members)
        res_list.append(res)

    return res_list


def get_user_data(statement):
    keys = ["actor", "account", "name"]
    user_name = get_nested_value(statement, keys)
    return {"name": user_name}


def get_object_data(statement):
    obj = statement["object"]
    o_id = obj["id"]
    o_def = obj["definition"]
    o_type = o_def["type"]
    o_name = list(o_def["name"].values())[0]
    res = {
        "id": o_id,
        "type": o_type,
        "name": o_name,
    }
    return res


def get_action_data(statement):
    act = statement["verb"]
    v_id = act["id"]
    verb = v_id.split("/")[-1]
    res = {
        "id": v_id,
        "verb": verb,
    }
    return res


def get_content_data(statement):
    # forum posts
    f_o_type = "http://id.tincanapi.com/activitytype/forum-topic"
    f_v_id = "http://id.tincanapi.com/verb/replied"
    f_content_keys = [
        "extensions",
        "http://inf.uni-due.de/define/extensions/moodle_forum_post",
        "message"
    ]
    forumContentProjection = {"content": "$object.definition.extensions.message"}
    # wiki update
    w_o_type = "http://collide.info/moodle_wiki_page"
    w_v_id = "http://id.tincanapi.com/verb/updated"
    w_content_keys = [
        "extensions",
        "http://collide.info/moodle_wiki_update",
        "content_clean"
    ]
    wikiContentProjection = {"content": "$object.definition.extensions.content_clean"}

    is_wiki_update = False
    is_forum_update = False

    obj = statement["object"]
    v = statement["verb"]

    v_id = v["id"]
    obj_type = obj["definition"]["type"]

    if v_id == f_v_id and obj_type == f_o_type:
        text = get_nested_value(obj, f_content_keys)
        text = BeautifulSoup(text, "lxml").get_text()
        type = "forum_post"
    elif v_id == w_v_id and obj_type == w_o_type:
        text = get_nested_value(obj, w_content_keys)
        type = "wiki_entry"
    else:
        return None

    res = {
        "text": text,
        "type": type,
    }
    return res


def extract_data(statement):
    moodle_data = get_moodle_data(statement)
    course_data = get_course_data(statement)
    group_task_data = get_group_task_data(statement)
    user_data = get_user_data(statement)
    # object id
    object_data = get_object_data(statement)
    # action id
    action_data = get_action_data(statement)
    content = get_content_data(statement)

    properties = {
        "moodle": moodle_data,
        "course": course_data,
        "user": user_data,
        "object": object_data,
        "action": action_data,
    }

    return {
        "properties": properties,
        "group_tasks": group_task_data,
        "action_extras": {"content": content},
    }


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
        try:
            task = group["task"]
            task["courseid"] = courseid
            group["courseid"] = courseid
            gmd.update_group(group, courseid)
            gmd.update_group_task(task, courseid)
        except Exception  as e:
            message = "Could not write group task mapping for \n Group: {}\n Course: {}\n"
            message = message.format(group, courseid)
            print(message, file=sys.stderr)


def is_self_assessment(statement):
    self_type = "https://moodle.ikarion-projekt.de/define/type/moodle/block_groupactivity"
    obj_name = "Groupactivity self assessment"
    obj = statement["object"]
    name_is_self = False
    type_is_self = False
    try:
        if list(obj["definition"]["name"].values())[0] == obj_name:
            name_is_self = True
    except:
        pass
    try:
        if obj["definition"]["type"] == self_type:
            type_is_self = True
    except:
        pass

    return name_is_self or type_is_self


def determine_relevant_task(statement):
    # is it a self assessment statement?
    self_assessment = is_self_assessment(statement)

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


def is_wiki_update(statement):
    wiki_verb = "http://id.tincanapi.com/verb/updated"
    wiki_object_type = "http://collide.info/moodle_wiki_page"
    verb = statement["verb"]["id"]
    type = statement["object"]["definition"]["type"]
    right_verb = wiki_verb == verb
    right_type = wiki_object_type == type
    if right_verb and right_type:
        return True
    else:
        return False


def add_wiki_concepts(statement):
    group_task = statement["relevant_group_task"]
    task = group_task["task"]
    task_name = task["task_name"]
    object_extensions = statement["object"]["definition"]["extensions"]
    wiki_content_clean = ""
    extraced_concepts = []
    for ext in object_extensions:
        if ext["id"] == "http://collide.info/moodle_wiki_update":
            wiki_content_clean = ext["content_clean"]
    try:
        extraced_concepts = gmd.calc_wiki_concepts(wiki_content_clean, task_name)
    except Exception as e:
        print(e)
        traceback.print_exc()
    counted_concepts = Counter(extraced_concepts)
    wiki_concepts = [{
        "word": k[0],
        "score": k[1],
        "count": v
    } for k, v in counted_concepts.items()]
    statement["wiki_concepts"] = wiki_concepts


def process_statement(statement):
    restructure_extensions(statement)
    replace_dots(statement)
    convert_timestamp(statement)
    project_fields(statement)
    process_groups(statement)
    write_new_groups_and_tasks(statement)
    determine_relevant_task(statement)
    if is_wiki_update(statement):
        add_wiki_concepts(statement)


def relevant_model_change(statement):
    object_type = statement["object"]["definition"]["type"]
    verb_id = statement["verb"]["id"]

    if relevant_object_type(object_type) and relevant_verb(verb_id):
        return True
    elif is_self_assessment(statement):
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
