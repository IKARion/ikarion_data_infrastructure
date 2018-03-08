from .. import modelDBConnection as con

import datetime

coll = con.db.xapi_statements

# Fields
RES_USED_LIST = 'ressources_list'
RES_USED_FIELD = 'resource_accesses'
DISTINCT_RES_USED = 'distinct_resource_accesses'
DISTINCT_RES_USED = 'distinct_resource_accesses'


# ...

course_schema = "context.course.name"
artefact_schema = "object.id"
# TODO lookup artefact type schema
artefact_type_schema = ""
user_schema = "actor.name"
time_stamp_schema = "timestamp"
action_schema = "verb.id"
verb_schema = "verb.id"
# Retrieve


def convert_timestamp():
    pass


def course_query(course):
    query = {
        course_schema: course
    }
    return query

def user_query(user):
    query = {
        user_schema: user
    }
    return query

def verb_query(verb):
    query = {
        verb_schema: verb
    }
    return query

def artefact_query(artefact):
    query = {
        artefact_schema: artefact
    }
    return query

def artefact_type_query(artefact_type):
    query = {
        artefact_type_schema: artefact_type
    }
    return query

def get_all_user_statements(user):
    result = coll.find(user_query(user))
    return list(result)

def get_all_user_times(user):
    result = list(coll.find(user_query(user), {time_stamp_schema: 1}))
    result = [item[time_stamp_schema] for item in result].sort()
    return result

def getAllCourses():
    return list(coll.distinct(course_schema))


def getAllUsers():
    return list(coll.distinct(user_schema))


def getAllUsersForCourse(course):

    result = list(coll.distinct(user_schema, course_query(course)))
    return result


def getAllCoursesForUser(user):
    result = list(coll.distinct(course_schema, user_query(user)))
    return result


def get_user_active_days(user):
    epoch_times = get_all_user_times(user)
    datetimes = [datetime.datetime.utcfromtimestamp(item) for item in epoch_times]
    dates = [item.date for item in datetimes]
    distinct_dates = set(dates)
    sorted_date_list = list(distinct_dates).sort()
    return sorted_date_list

def get_user_artefact_actions(user, artefact):
    query = merge_query(user_query(user), artefact_query(artefact))
    result = list(coll.find(query))
    return result


def get_user_artefact_action_stats(user, artefact, verb):

    query = merge_query(user_query(user), artefact_query(artefact), verb_query(verb))
    result = list(coll.find(query))
    return len(result)

def get_user_artefact_type_action_stats(user, artefact_type, verb):
    query = merge_query(user_query(user),
                        artefact_type_query(artefact_type),
                        verb_query(verb))
    result = coll.find(query)
    return len(result)

def aggregate_actions(user, artefact_type, action):
    pass

def merge_query(*args):
    merged_query = {

    }
    for arg in args:
        merged_query = {**merged_query, **arg}

    return merged_query


# def getUserModel(user, course):
#     doc = con.db.usermodels.find_one({'uid': user, 'course': course}, {'_id': 0})
#     if doc is None:
#         raise NoSuchUserException(user, course)
#     return doc
#
#
# def getUserModelsForCourse(course):
#     docs = con.db.usermodels.find({'course': course}, {'_id': 0})
#     if docs.count == 0:
#         raise NoSuchCourseException(course)
#     return list(docs)


# # Update
# def updateOrInsertUserModel(user, course, newModel):
#     con.db.usermodels.updateOne(
#         {'uid': user, 'course': course},
#         {'$set': newModel},
#         upsert=True
#     )
#
#
# def updateUserModelSetField(user, course, field, incValue):
#     res = con.db.usermodels.updateOne(
#         {'uid': user, 'course': course},
#         {'$set': {field: incValue}}
#     )
#
#     if (res.matched_count == 0):
#         raise NoSuchUserException(user, course)
#
#
# def updateUserModelIncrementField(user, course, field, incValue):
#     res = con.db.usermodels.updateOne(
#         {'uid': user, 'course': course},
#         {'$inc': {field: incValue}}
#     )
#
#     if (res.matched_count == 0):
#         raise NoSuchUserException(user, course)


# Exception classes
class NoSuchUserException(Exception):
    def __init__(self, user, course):
        self.message = "No such user {} in course {}".format(user, course)


class NoSuchCourseException(Exception):
    def __init__(self, course):
        self.message = "No such course {}".format(course)
