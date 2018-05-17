import datetime
from collections import abc
import pytz
import bdateutil.parser as dp
import ikarion_data_management.data_access_layer.model_db_access_layer.user_model_dao as umd


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
    # TODO restructure statement so that keys with dots in them become fields instead

    extentions_list = nested_json_extensions(statement)
    for extensions_map in extentions_list:
        extensions = extensions_map["extensions"]
        mongo_compliant_extensions = []
        for k, v in extensions.items():
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

def process_statement(statement):
    restructure_extensions(statement)
    replace_dots(statement)
    convert_timestamp(statement)
    process_groups(statement)

