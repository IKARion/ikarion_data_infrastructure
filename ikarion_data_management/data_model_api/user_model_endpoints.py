from flask import Blueprint, jsonify, request
from ..data_access_layer.model_db_access_layer import user_model_dao as umd

user_model_blueprint = Blueprint('user_model_blueprint', __name__)


@user_model_blueprint.route('/about')
def about():
    return 'User model endpoints.'


# User models
@user_model_blueprint.route("/model/<course>/<user>")
def get_user_model(course, user):
    return jsonify(model=umd.get_user_model_for_course(user, course))


@user_model_blueprint.route("/models/<course>")
def get_all_user_models(course):
    users = umd.get_all_users_for_course(course)
    user_models = [umd.get_user_model_for_course(user, course) for user in users]
    return jsonify(models=user_models)


# List of users
@user_model_blueprint.route("/")
def get_all_users():
    return jsonify(users=umd.get_all_users())


@user_model_blueprint.route("/<course>")
def get_all_users_for_course(course):
    return jsonify(users=umd.get_all_users_for_course(course))


# List of courses
@user_model_blueprint.route("/courses")
def get_all_courses():
    return jsonify(courses=umd.get_all_courses())


@user_model_blueprint.route("/times/<user>/<course>")
def get_all_user_times(user, course):
    return jsonify(courses=umd.get_all_user_times(user, course))

@user_model_blueprint.route("/active_days/<user>/<course>")
def get_user_active_days(user, course):
    return jsonify(umd.get_user_active_days(user, course))

@user_model_blueprint.route("/avg_latency/<user>/<course>")
def get_avg_latency(user, course):
    if request.is_json:
        constraints = request.get_json()
    else:
        constraints = []
    latency = umd.get_user_average_latency(user, course, *constraints)
    return jsonify({"avg_latency": latency})

@user_model_blueprint.route("/group_activities/<course>/<group>")
def get_group_activities(course, group):
    """
    Returns json array of objects with fields [group_id, user_id, verb_id, object_id, timestamp]
    :param course:
    :type course:
    :param group:
    :type group:
    :return:
    :rtype:
    """
    try:
        start_time = 0
        constraints = []
        if request.is_json:
            r_json = request.get_json()
            if "start_time" in r_json:
                start_time = float(r_json["start_time"])
            if "artefact_id" in r_json:
                artefact_id = r_json["artefact_id"]
                artefact_constraint = umd.artefact_query(artefact_id)
                constraints.append(artefact_constraint)
        group_activities = umd.get_group_activities(course, group, start_time, *constraints)
    except Exception as e:
        print(e)
    return jsonify(group_activities=group_activities)


@user_model_blueprint.route("/avg_group_latency/<course>/<group>/<startpoint>")
def get_average_latency_for_group(course, group, startpoint):

    return jsonify(avg_group_latency=umd.get_group_average_latency(int(startpoint), group, course))

@user_model_blueprint.route("/groups_for_course/<course>")
def get_all_groups_for_course(course):
    print("groups_for_course")
    return jsonify(groups=umd.get_all_groups_for_course(course))

@user_model_blueprint.route("/courses/<user>")
def get_all_courses_for_user(user):

    return jsonify(courses=umd.get_all_courses_for_user(user))


