from .. import modelDBConnection as con

# Fields
RES_USED_LIST = 'ressources_list'
RES_USED_FIELD = 'resource_accesses'
DISTINCT_RES_USED = 'distinct_resource_accesses'
DISTINCT_RES_USED = 'distinct_resource_accesses'


# ...

# Retrieve
def getAllCourses():
    return con.db.usermodels.distinct('course')


def getAllUsers():
    return con.db.usermodels.distinct('uid')


def getAllUsersForCourse(course):
    docs = con.db.usermodels.find({'course': course}, {'uid': 1})
    if docs.count == 0:
        raise NoSuchCourseException(course)
    return list(docs)


def getAllCoursesForUser(user):
    docs = con.db.usermodels.find({'uid': user}, {'course': 1})
    if docs.count() == 0:
        raise NoSuchUserException(user, "all courses")

    return list(docs)


def getUserModel(user, course):
    doc = con.db.usermodels.find_one({'uid': user, 'course': course}, {'_id': 0})
    if doc is None:
        raise NoSuchUserException(user, course)
    return doc


def getUserModelsForCourse(course):
    docs = con.db.usermodels.find({'course': course}, {'_id': 0})
    if docs.count == 0:
        raise NoSuchCourseException(course)
    return list(docs)


# Update
def updateOrInsertUserModel(user, course, newModel):
    con.db.usermodels.updateOne(
        {'uid': user, 'course': course},
        {'$set': newModel},
        upsert=True
    )


def updateUserModelSetField(user, course, field, incValue):
    res = con.db.usermodels.updateOne(
        {'uid': user, 'course': course},
        {'$set': {field: incValue}}
    )

    if (res.matched_count == 0):
        raise NoSuchUserException(user, course)


def updateUserModelIncrementField(user, course, field, incValue):
    res = con.db.usermodels.updateOne(
        {'uid': user, 'course': course},
        {'$inc': {field: incValue}}
    )

    if (res.matched_count == 0):
        raise NoSuchUserException(user, course)


# Exception classes
class NoSuchUserException(Exception):
    def __init__(self, user, course):
        self.message = "No such user {} in course {}".format(user, course)


class NoSuchCourseException(Exception):
    def __init__(self, course):
        self.message = "No such course {}".format(course)
