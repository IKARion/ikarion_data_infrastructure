import json
from flask import Blueprint
from ..data_access_layer.model_db_access_layer import user_model_dao
#from ..data_access_layer.model_db_access_layer import group_model_dao
import sys
import datetime
from flask import request
from flask import Response
from ikarion_data_management.data_access_layer import modelDBConnection as con
from ikarion_data_management.log_aggregator import statement_processing as sp

from ikarion_data_management.data_access_layer.model_db_access_layer.user_model_dao import course_query
from ikarion_data_management.data_access_layer.management_access_layer import scheduler

log_receiver_blueprint = Blueprint('log_receiver_blueprint', __name__)


@log_receiver_blueprint.route('/about')
def about():
    return 'Log receiver endpoints.'


# The LRS fowards resource access logs to this endpoint.
# Log forwarding has to be specified in learning locker first.
# (See https://ht2ltd.zendesk.com/hc/en-us/articles/115002026451--NEW-LL-Statement-Forwarding)
@log_receiver_blueprint.route('/log_forwarding', methods=["GET", "POST"])
def processLog():
    if request.method == "GET":
        statement = request.get_json(force=True)


    if request.method =="POST":
        statement = request.get_json(force=True)

    statement_string = json.dumps(statement)
    statement_string = statement_string.replace("&46;", ".")
    statement = json.loads(statement_string)
    relevant = sp.statement_relevant(statement)
    if relevant:
        sp.process_statement(statement)
        con.db.xapi_statements.insert_one(statement)
    # if sp.relevant_model_change(statement):
    #     for job in scheduler.get_jobs():
    #         job.modify(next_run_time=datetime.datetime.now())

    return Response(status=200)









