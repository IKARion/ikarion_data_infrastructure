from flask import Blueprint, jsonify, request
from ..data_access_layer.model_db_access_layer import user_model_dao as umd
from .util import fix_url_chars

from concurrent.futures import ThreadPoolExecutor

user_model_blueprint = Blueprint('user_model_blueprint', __name__)

@user_model_blueprint.url_value_preprocessor
def fix_url_encoding(endpoint, values):
    for k, v in values.items():
        values[k] = fix_url_chars(v)

@user_model_blueprint.route('/about')
def about():
    return 'User model endpoints.'


# User models
@user_model_blueprint.route("/model/<path:course>/<user>")
def get_user_model(course, user):
    return jsonify(data=umd.get_user_model_for_course(user, course))


@user_model_blueprint.route("/models/<course>")
def get_all_user_models(course):
    from ikarion_data_management.ikarion_data_infrastructure import app
    users = umd.get_all_users_for_course(course)

    def get_user_model(user):
        with app.app_context():
            return umd.get_user_model_for_course(user, course)
    with ThreadPoolExecutor(max_workers=100) as thread_pool:
        user_models = list(thread_pool.map(get_user_model, users))
    return jsonify(data=user_models)


# List of users
@user_model_blueprint.route("/")
def get_all_users():
    return jsonify(data=umd.get_all_users())


@user_model_blueprint.route("/<course>")
def get_all_users_for_course(course):
    print("***5")
    # print(request.url)
    # print(request.query_string)
    # print("***6")
    print(course)
    # print("***7")
    # print(course)
    # print(request.query_string)
    print("***8")
    s = request.query_string
    print(course)
    #print(course + "?" + s.decode("utf-8"))
    #course = course + "?" + s.decode("utf-8")

    course = fix_url_chars(course)

    return jsonify(data=umd.get_all_users_for_course(course))


# List of courses
@user_model_blueprint.route("/courses")
def get_all_courses():
    return jsonify(data=umd.get_all_courses())

# test repo2
@user_model_blueprint.route("/git_users/<repo>")
def test_for_repo2(repo):
    print(repo)
    repo = fix_url_chars(repo)
    print(repo)
    return jsonify(data=umd.get_all_users_for_git_repo(repo))


# List of repositories
@user_model_blueprint.route("/repositories")
def get_all_repositories():
    return jsonify(data=umd.get_all_group_repos())

# List of activities for repository

@user_model_blueprint.route("/repo_activities/<repo>")
def get_all_repo_activities(repo):

    repo = fix_url_chars(repo)

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
    group_activities = umd.get_repo_activities(repo, start_time, *constraints)

    return jsonify(data=group_activities)


@user_model_blueprint.route("/times/<user>/<course>")
def get_all_user_times(user, course):
    return jsonify(data=umd.get_all_user_times(user, course))

@user_model_blueprint.route("/active_days/<user>/<course>")
def get_user_active_days(user, course):

    user = fix_url_chars(user)
    course = fix_url_chars(course)
    return jsonify(data=umd.get_user_active_days(user, course))

@user_model_blueprint.route("/avg_latency/<user>/<course>")
def get_avg_latency(user, course):
    course = fix_url_chars(course)
    if request.is_json:
        constraints = request.get_json()
    else:
        constraints = []
    latency = umd.get_user_average_latency(user, course, *constraints)
    return jsonify(data=latency)

@user_model_blueprint.route("/courses/<user>")
def get_all_courses_for_user(user):

    return jsonify(data=umd.get_all_courses_for_user(user))


def encode_url_chars(url):
    url = url.replace("/", "$slash$")
    url = url.replace("?", "$qmark$")
    return url


