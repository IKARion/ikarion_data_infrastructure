from flask import Blueprint, jsonify
from ..data_access_layer.model_db_access_layer import user_model_dao

user_model_endpoints = Blueprint('user_model_endpoints', __name__)

@user_model_endpoints.route('/test/<int:value>')
def test(value):

    return user_model_dao.testDB(value)

@user_model_endpoints.route('/about')
def about():
    return 'User model endpoints.'

# User models
@user_model_endpoints.route("/models/<course>/<user>")
def getUserModel(course, user):

    return jsonify(model=user_model_dao.getUserModel(course, user))


@user_model_endpoints.route("/models/<course>")
def getAllUserModels(course):

    return jsonify(model=user_model_dao.getUserModelsForCourse(course))


# List of users
@user_model_endpoints.route("/")
def getAllUsers():

    return jsonify(result=user_model_dao.getAllUsers())


@user_model_endpoints.route("/<course>")
def getAllUsersForCourse(course):
    return jsonify(users=user_model_dao.getAllUsersForCourse(course))


# List of courses
@user_model_endpoints.route("/courses")
def getAllCourses():

    return jsonify(result=user_model_dao.getAllCourses())


@user_model_endpoints.route("/courses/<user>")
def getAllCoursesForUser(user):

    return jsonify(courses=user_model_dao.getAllCoursesForUser(user))