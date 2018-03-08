from flask import Blueprint
from ..data_access_layer.model_db_access_layer import user_model_dao
#from ..data_access_layer.model_db_access_layer import group_model_dao
from flask import request
from flask import Response
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
        statement = convert_timestamp(statement)
        con.db.xapi_statements.insert_one(statement)

    return Response(status=200)


def statement_relevant(statement):
    # TODO find out what statements are not relevant and filter them.
    return True


def convert_timestamp(statement):
    timestamp = statement["timestamp"]
    year, month, *rest = timestamp.split("-")
    day, *rest = rest.split("T")
    rest = rest.replace("+", ":")
    hours, minutes, seconds, *rest = rest.split(":")

    date_time = datetime.datetime(year, month, day, minutes, hours, seconds,tzinfo=pytz.utc)
    epoch_timestamp = date_time.timestamp()
    return epoch_timestamp
