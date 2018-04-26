from flask import Blueprint, jsonify
from ..data_access_layer.model_db_access_layer import group_model_dao

group_model_blueprint = Blueprint('group_model_blueprint', __name__)

# models: group content, group sequence, group structure

@group_model_blueprint.route('/about')
def about():
    return 'Group model endpoints.'

@group_model_blueprint.route("/")
def getAllGroups():
    return jsonify(model=group_model_dao.getGroups())

def getGroupsInContext(context):
    # context: task or course or both
    return 'todo'

def getContexts():
    # context: zeitraum, kurs, resourcen, name
    return 'todo'

@group_model_blueprint.route('/models')
def models():
    return 'Group models'

@group_model_blueprint.route('/models/<string:course>/<string:group>/<string:context>')
def getLatencies(course, group, context):
    latency, latencies = group_model_dao.getLatencies(course, group, context)
    return jsonify(average_latency=latency, latencies=latencies)

def getAllLatencies(context):
    return 'todo'

def getConceptCoverage(group, context):
    return 'todo'

def getActionsOfUsers(group, context):
    return 'todo'

def getProducedContentByUsers(group, context):
    return 'todo'

def getInactiveUsers(group, context):
    # needs log for group and groupmembers (log by group formation plugin?)
    return 'todo'

def getConceptMap(group, context):
    return 'todo'

# define URL
# define result for URL call (wiki)

