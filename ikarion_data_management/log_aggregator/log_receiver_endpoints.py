from flask import Blueprint
from ..data_access_layer.model_db_access_layer import user_model_dao
#from ..data_access_layer.model_db_access_layer import group_model_dao
from flask import request
from flask import Response
from collections import abc
from ikarion_data_management.data_access_layer import modelDBConnection as con
import datetime
import pytz
log_receiver_endpoints = Blueprint('log_receiver_endpoints', __name__)


@log_receiver_endpoints.route('/about')
def about():
    return 'Log receiver endpoints.'

# The LRS fowards resource access logs to this endpoint.
# Log forwarding has to be specified in learning locker first.
# (See https://ht2ltd.zendesk.com/hc/en-us/articles/115002026451--NEW-LL-Statement-Forwarding)
@log_receiver_endpoints.route('/resource_access')
def processResourceAccessLog():
    statement = request.get_json()
    relevant = statement_relevant(statement)
    if relevant:
        statement["timestamp"] = convert_timestamp(statement)
        restructure_extensions(statement)
        con.db.xapi_statements.insert_one(statement)
    return Response(status=200)


def statement_relevant(statement):
    # TODO find out what statements are not relevant and filter them.
    return True


def restructure_extensions(statement):
    # TODO restructure statement so that keys with dots in them become fields instead

    extentions_list = nested_json_extensions(statement)
    for extensions_map in extentions_list:
        extensions = extensions_map["extensions"]
        mongo_compliant_extensions = []
        for k, v in dict(extensions.items()):
            v["id"] = k
            mongo_compliant_extensions.append(v)
        extensions_map["extensions"] = mongo_compliant_extensions


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


def convert_timestamp(statement):
    """
    converts xapi_statements weird timestamp format to epoch time timestamps
    :param statement:
    :type statement:
    :return:
    :rtype:
    """
    timestamp = statement["timestamp"]
    year, month, *rest = timestamp.split("-")
    day, *rest = rest.split("T")
    rest = rest.replace("+", ":")
    hours, minutes, seconds, *rest = rest.split(":")

    date_time = datetime.datetime(year, month, day, minutes, hours, seconds, tzinfo=pytz.utc)
    epoch_timestamp = date_time.timestamp()
    return epoch_timestamp
