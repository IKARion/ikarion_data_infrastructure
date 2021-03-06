from flask import Blueprint, jsonify, request
from ..data_access_layer.model_db_access_layer import group_model_dao
from ..data_access_layer.model_db_access_layer import user_model_dao
from .util import fix_url_chars

group_model_blueprint = Blueprint('group_model_blueprint', __name__)


# models: group content, group sequence, group structure

# Convert special char replacements back to normal
@group_model_blueprint.url_value_preprocessor
def fix_url_encoding(endpoint, values):
    for k, v in values.items():
        if isinstance(v, str):
            values[k] = fix_url_chars(v)


@group_model_blueprint.route('/about')
def about():
    return 'Group model endpoints.'


@group_model_blueprint.route("/")
def getAllGroups():
    return jsonify(model=group_model_dao.getGroups())


@group_model_blueprint.route("/group_tasks/<string:course>")
def get_group_tasks(course):
    return jsonify(data=group_model_dao.get_group_tasks(fix_url_chars(course)))


# @group_model_blueprint.route("/group_tasks/groups/<task>")
# def get_group_tasks(task):
#    return jsonify(data=group_model_dao.get_group_tasks(fix_url_chars(course)))


@group_model_blueprint.route("/groups_for_course/<course>")
def get_all_groups_for_course(course):
    course = fix_url_chars(course)
    return jsonify(data=group_model_dao.get_all_groups_for_course(course))


@group_model_blueprint.route("/groups_for_task/<course>/<task>")
def get_all_groups_for_task(course, task):
    task = fix_url_chars(task)
    course = fix_url_chars(course)
    return jsonify(data=group_model_dao.get_all_groups_for_task(course, task))


@group_model_blueprint.route("/group_self_assessment/<course_id>/<group_id>/<task_id>/", defaults={
    "timestamp": "2147483648"
})
@group_model_blueprint.route("/group_self_assessment/<course_id>/<group_id>/<task_id>/<timestamp>")
def get_group_self_assessment(course_id, group_id, task_id, timestamp):
    res = group_model_dao.get_group_self_assesment(course_id, group_id, task_id, int(timestamp))

    return jsonify(data=res)


@group_model_blueprint.route("/weighted_wiki_wordcount/<course_id>/<group_id>/<task_id>/", defaults={
    "timestamp": "2147483648"
})
@group_model_blueprint.route("/weighted_wiki_wordcount/<course_id>/<group_id>/<task_id>/<int:timestamp>")
def get_group_weighted_wiki_word_count(course_id, group_id, task_id, timestamp):
    res, wiki_concepts_per_user = group_model_dao.get_group_weighted_wiki_count_for_task(course_id, group_id, task_id,
                                                                                         int(timestamp))

    return jsonify(data=res, wiki_concepts_per_user=wiki_concepts_per_user)


@group_model_blueprint.route("/group_interventions/<course_id>/<group_id>/<task_id>/", defaults={
    "timestamp": "2147483648"
})
@group_model_blueprint.route("/group_interventions/<course_id>/<group_id>/<task_id>/<int:timestamp>")
def get_group_interventions(course_id, group_id, task_id, timestamp):
    res = group_model_dao.get_group_interventions_for_task(course_id, group_id, task_id, int(timestamp))
    return jsonify(data=res)


"""
    Returns json array of objects with fields [group_id, user_id, verb_id, object_id, timestamp]
    :param course:
    :type course:
    :param group:
    :type group:
    :return:
    :rtype:
"""


@group_model_blueprint.route("/group_activities/<course>/<group>")
def get_group_activities(course, group):
    course = fix_url_chars(course)
    group_activities = group_model_dao.get_group_activities(course, group, [])

    return jsonify(data=group_activities)


@group_model_blueprint.route("/all_group_activities/<course>/<group>")
def get_all_group_activities(course, group):
    course = fix_url_chars(course)
    all_group_activities = group_model_dao.get_all_group_activities(course, group, [])

    return jsonify(data=all_group_activities)


@group_model_blueprint.route("/grouptask_activities/<course>/<group>/<task>")
def get_group_activities_task(course, group, task):
    # TODO: Use urls as ids for groups and tasks and only work with task ids instead of course ids.
    course = fix_url_chars(course)
    group_activities = group_model_dao.get_group_activities_for_task(course, group, task, [])

    return jsonify(data=group_activities)


# def get_group_ikarion_element_actions(course, group_id, task_id, timestamp):

@group_model_blueprint.route("/ikarion_element_activities/<course>/<group>/<task>/")
def get_ikarion_element_activities_for_task(course, group, task):
    # TODO: Use urls as ids for groups and tasks and only work with task ids instead of course ids.
    course = fix_url_chars(course)
    group_activities = group_model_dao.get_group_ikarion_element_actions(course, group, task)

    return jsonify(data=group_activities)


# @group_model_blueprint.route("/avg_group_latency/<course>/<group>/<startpoint>")
# def get_average_latency_for_group(course, group, startpoint):
#     course = fix_url_chars(course)
#
#     return jsonify(data=group_model_dao.get_group_average_latency(int(startpoint), group, course))


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
