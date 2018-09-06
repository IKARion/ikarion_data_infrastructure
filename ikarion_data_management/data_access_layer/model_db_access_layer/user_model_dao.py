from .. import modelDBConnection as con
from pymongo import MongoClient
mongo_uri = "mongodb://ikarion:ikariondb@cluster0-shard-00-00-n3pml.mongodb.net:27017,cluster0-shard-00-01-n3pml.mongodb.net:27017,cluster0-shard-00-02-n3pml.mongodb.net:27017/db?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"

# con = MongoClient(mongo_uri)

import datetime


# onstraints parameter for the functions is used to keep query context flexible
# and add constraints at a later time without rewriting all the functions every time
# constraints are dictionaries/maps as used in mongodb query. They all get merged to create a query

context_extension_id = "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log"

# Fields
RES_USED_LIST = 'resources_list'
RES_USED_FIELD = 'resource_accesses'
DISTINCT_RES_USED = 'distinct_resource_accesses'


#course_schema = "context.extensions.courseid"
group_schema = "context.groups.id"
artefact_schema = "object.id"
artefact_type_schema = "object.definition.type"
#artefact_
user_schema = "actor.name"
time_stamp_schema = "timestamp"
action_schema = "verb.id"
verb_schema = "verb.id"
repository_schema = "context.extensions.repository"
object_content_schema = "object.definition.extensions.message"
# Retrieve

# Standart queries
course_list_query = [
    {"$match" : {
        "context.contextActivities.grouping" : {
            "$elemMatch" : {"definition.type" : "http://lrs.learninglocker.net/define/type/moodle/course"}
         }
     }},
     {"$project" : {
         "course" : {
            "$filter" : {
                "input" : "$context.contextActivities.grouping",
                "as" : "item",
                "cond" : {"$eq": ["$$item.definition.type", "http://lrs.learninglocker.net/define/type/moodle/course"]}
            }
         }
     }},
     {"$unwind" : "$course"},
     {"$unwind" : "$course.definition.extensions"},
     {"$group" : {
         "_id" : {"courseid" : "$course.definition.extensions.url", "name" : "$course.definition.extensions.fullname"}
     }},
     {"$project" : {
         "_id" : 0, "courseid" : "$_id.courseid", "name" :  "$_id.name"
     }}
]

def course_query(course):
    if course is None:
        return {}
    else:
        query = {
            "context.contextActivities.grouping" : {
                "$elemMatch" : {
                    "definition.type" : "http://lrs.learninglocker.net/define/type/moodle/course",
                    "definition.extensions" : {
                        "$elemMatch" : {"url" : course}
                    }
                }
            }
        }
        return query


def group_query(group):
    if group is None:
        return {}
    else:
        query = {
            group_schema: group
        }
        return query



def user_query(user):
    query = {
        user_schema: user
    }
    return query

def repo_query(repo):
    query = {
        repository_schema: repo
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


def get_all_user_statements(user, *constraints):
    query = merge_query(user_query(user), *constraints)
    result = con.db.xapi_statements.find(query)
    return list(result)

def get_all_course_statements(course, *constraints):
    query = merge_query(course_query(course), *constraints)
    result = con.db.xapi_statements.find(query)
    return list(result)

def get_all_user_times(user, course, *constraints):
    ##print("q1")
    query = merge_query(user_query(user), course_query(course), *constraints)
    #print("q")
    #print(query)
    result = con.db.xapi_statements.find(query, {time_stamp_schema: 1})
    result = list(set([item[time_stamp_schema] for item in result]))

    # sorted(map(float, result))
    #sorted(map(float, result))
    return result


def get_all_courses():
    return list(con.db.xapi_statements.aggregate(course_list_query))


def get_all_users():

    return list(con.db.xapi_statements.distinct(user_schema))

def get_all_group_repos():
    return list(con.db.xapi_statements.distinct(repository_schema))

def get_all_users_for_course(course, *constraints):
    query = merge_query(course_query(course), *constraints)
    #print("q2")
    #print(query)
    #print(course)
    result = list(con.db.xapi_statements.distinct(user_schema, query))
    return result


def get_all_users_for_group(course, group, *constraints):
    query = merge_query(course_query(course), group_query(group), *constraints)
    result = list(con.db.xapi_statements.distinct(user_schema, query))
    return result

def get_all_users_for_git_repo(repo, *constraints):
    #query = merge_query(course_query(course), group_query(group), *constraints)
    result = list(con.db.xapi_statements.distinct(user_schema, repo_query(repo)))
    return result

def get_all_groups_for_course(course):
    query = merge_query(course_query(course))
    result = list(con.db.xapi_statements.distinct(group_schema, query))
    return result

def get_all_courses_for_user(user):
    # TODO: Update course schema
    result = list(con.db.xapi_statements.distinct(course_schema, user_query(user)))
    return result


def get_user_active_days(user, course, *constraints):
    #print("**")
    epoch_times = get_all_user_times(user, course, *constraints)
    datetimes = [datetime.datetime.utcfromtimestamp(item) for item in epoch_times]
    dates = [item.date() for item in datetimes]
    distinct_dates = set(dates)
    sorted_date_list = sorted(list(distinct_dates))
    sorted_date_list = [date.isoformat() for date in sorted_date_list]
    return sorted_date_list


def get_user_artefact_actions(user, artefact, *constraints):
    query = merge_query(user_query(user), artefact_query(artefact), *constraints)
    result = list(con.db.xapi_statements.find(query))
    return result


def get_user_verbs(user, course, *constraints):
    query = merge_query(user_query(user), course_query(course), *constraints)
    return list(con.db.xapi_statements.distinct(verb_schema, query))


def get_user_artefact_types(user, course, *constraints):
    query = merge_query(user_query(user), course_query(course), *constraints)
    return list(con.db.xapi_statements.distinct(artefact_type_schema, query))


def get_user_verbs_for_artefact_type(user, artefact_type, course, *constraints):
    query = merge_query(user_query(user),
                        artefact_type_query(artefact_type),
                        course_query(course),
                        *constraints)
    return list(con.db.xapi_statements.distinct(verb_schema, query))


def get_user_artefact_action_stats(user, artefact, verb):

    query = merge_query(user_query(user), artefact_query(artefact), verb_query(verb))
    result = list(con.db.xapi_statements.find(query))
    return {"count": len(result)}


def get_user_artefact_type_action_stats(user, artefact_type, verb, course, *constraints):
    query = merge_query(user_query(user),
                        artefact_type_query(artefact_type),
                        verb_query(verb),
                        course_query(course),
                        *constraints)
    artefact_list = list(con.db.xapi_statements.distinct(artefact_schema, query))
    result = []
    for artefact in artefact_list:
        stats = get_user_artefact_action_stats(user, artefact, verb)
        data = {
            "id": artefact,
            **stats,
        }
        result.append(data)
    return result

def get_group_activities(course, group, start_time, *constraints):
    """
    Returns json array of objects with fields [group_id, user_id, verb_id, object_id, timestamp]
    :param group:
    :type group:
    :return:
    :rtype:
    """
    # TODO Project content especially forum post text
    print(con.db.name)
    users = get_all_users_for_group(course, group, *constraints)
    projection = {
        "object_id": "$" + artefact_schema,
        "verb_id": "$" + verb_schema,
        "timestamp": True,
        "object_type": "$" +artefact_type_schema,
        "object_name": "$" + "object.definition.name",
        "forum_content": "$" + "object.definition.extensions.message",
        "wiki_content": "$" + "context.extensions.other"
    }
    group_activities = []
    for user in users:

        query = merge_query(user_query(user), group_query(group))
        aggregation = [
            {"$match": query},
            {"$project": projection},
        ]
        user_statements = list(con.db.xapi_statements.aggregate(aggregation))

        for statement in user_statements:

            activity = {
                "group_id": group,
                "user_id": user,
                "verb_id": statement["verb_id"],
                "object_id": statement["object_id"],
                "timestamp": statement["timestamp"],
                "object_type": statement["object_type"],
                "object_name": list(statement["object_name"].values())[0],
            }

            #TODO fix: only write object content if not empty
            if "forum_content" in statement:
                if statement["forum_content"]:
                    activity["forum_content"] = statement["forum_content"]

            #TODO fix: only write object content if not empty
            print(statement["verb_id"])
            if not statement["verb_id"] == "http://id.tincanapi.com/verb/replied":
                activity["wiki_content"] = statement["wiki_content"]


            group_activities.append(activity)
    group_activities = [item for item in group_activities if item["timestamp"] > start_time]
    group_activities.sort(key=lambda x: x["timestamp"], reverse=True)
    return group_activities

def get_repo_activities(repo, start_time, *constraints):
    """
    Returns json array of objects with fields [group_id, user_id, verb_id, object_id, timestamp]
    :param group:
    :type group:
    :return:
    :rtype:
    """
    # TODO Project content especially forum post text
    print(con.db.name)
    #users = get_all_users_for_group(course, group, *constraints)
    users = get_all_users_for_git_repo(repo, *constraints)

    projection = {
        "object_id": "$" + artefact_schema,
        "verb_id": "$" + verb_schema,
        "timestamp": True,
        "added_lines": "$" + "object.definition.extensions.added_lines",
        "deleted_lines": "$" + "object.definition.extensions.deleted_lines",
        "fileURL": "$" + "object.definition.extensions.fileURL"
    }
    group_activities = []
    for user in users:

        query = merge_query(user_query(user), repo_query(repo))
        aggregation = [
            {"$match": query},
            {"$project": projection},
        ]
        user_statements = list(con.db.xapi_statements.aggregate(aggregation))

        for statement in user_statements:

            activity = {
                "group_id": repo,
                "user_id": user,
                "verb_id": statement["verb_id"],
                "object_id": statement["object_id"],
                "timestamp": statement["timestamp"],
                "added_lines": statement["added_lines"][0],
                "deleted_lines": statement["deleted_lines"][0],
                "fileURL": statement["fileURL"][0]
            }
            group_activities.append(activity)
    group_activities = [item for item in group_activities if item["timestamp"] > start_time]
    group_activities.sort(key=lambda x: x["timestamp"], reverse=True)
    return group_activities




def get_group_average_latency(startpoint, group, course, *constraints):
    users = get_all_users_for_group(course, group)
    group_times = []
    for user in users:
        constraints = list(constraints) + [group_query(group)]
        user_times = get_all_user_times(user, course, *constraints)
        time_tuples = [(time, user) for time in user_times]
        group_times.extend(time_tuples)

    group_times.sort()
    response_times = []
    current_time = startpoint
    current_user = None
    for time, user in group_times:
        if user != current_user:
            diff_time = time - current_time
            current_time = time
            response_times.append(diff_time)

    avg_latency = sum(response_times)/len(response_times)

    return avg_latency


def get_user_average_latency(user, course, *constraints):

    times = get_all_user_times(user, course, *constraints)

    latencies = []
    for first, second in zip(times[:-1], times[1:]):
        latencies.append(second-first)

    avg_latency = sum(latencies)/len(latencies)
    return avg_latency


def get_user_model_for_course(user, course, *constraints):
    # TODO Update Usermodel on Site
    course_constraint = course_query(course)
    artefact_types = get_user_artefact_types(user, course, *constraints)
    artefacts = []
    for artefact_type in artefact_types:
        artefact_type_stats = []
        verbs = get_user_verbs_for_artefact_type(user, artefact_type, course, *constraints)
        for verb in verbs:
            verb_stats = get_user_artefact_type_action_stats(user, artefact_type, verb, course, *constraints)
            artefact_type_stats.append({verb: verb_stats})

        artefacts.append({artefact_type: artefact_type_stats})

    user_model = {
        "uid": user,
        "course_id": course,
        "updated_at": get_user_last_updated_at(user, course, *constraints),
        "active_days": get_user_active_days(user, course, *constraints),
        "artifacts": artefacts,
    }
    return user_model


def get_user_last_updated_at(user, course, *constraints):
    user_times = get_all_user_times(user, course, *constraints)
    if len(user_times) > 0:
        return user_times[-1]
    else:
        return 


def merge_query(*args):
    merged_query = {

    }
    for arg in args:
        merged_query.update(arg)
    print(merged_query)
    return merged_query

# Exception classes
class NoSuchUserException(Exception):
    def __init__(self, user, course):
        self.message = "No such user {} in course {}".format(user, course)


class NoSuchCourseException(Exception):
    def __init__(self, course):
        self.message = "No such course {}".format(course)
