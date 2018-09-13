from .. import modelDBConnection as con
from .util import *
from .queries import course_list_query, course_query
import json


def group_query(group):
    if group is None:
        return {}
    else:
        query = {
            group_schema: group
        }
        return query

def group_task_query(task):
    if task is None:
        return {}
    else:
        query = {
            task_schema: task
        }
        return query

# Retrieve
def getLatencies(course, group, context):

    # get action sequence for corresponding course, group and context
    data = list(con.db.group_sequence.find({'course_id': course, 'group_id': group, 'context_id': context}))
    data = data[0]
    action_sequence = data['action_sequence']
    elem_count = len(action_sequence)
    overall_latency = 0
    all_latencies = list() # list of latencies between all activities

    for i in range(len(action_sequence)):
        if i == 0:
            # do nothing for first activity
            first_activity = action_sequence[i]['start']
        else:
            # calculate time between current and previous activity
            current = action_sequence[i]
            previous = action_sequence[i-1]
            latency = int(current['start']) - int(previous['start'])
            all_latencies.append(latency)
            overall_latency = overall_latency + latency

    # calculate average latency
    average_latency = round(overall_latency / (elem_count-1))

    return average_latency, all_latencies

def get_group_tasks(course):
    query = {"courseid": course}
    group_tasks = list(con.db.grouptasks.find(query, {"_id": 0}))
    return group_tasks

def get_all_users_for_group(course, group, *constraints):
    query = merge_query(course_query(course), group_query(group), *constraints)
    result = list(con.db.xapi_statements.distinct(user_schema, query))
    return result

def get_all_groups_for_course(course):
    return list(con.db.xapi_statements.distinct(group_schema, course_query(course)))

def get_all_groups_for_task(task):

    return list(con.db.xapi_statements.distinct(group_schema, group_task_query(task)))

def get_group_activities(course, group, start_time, *constraints):
    """
    Returns json array of objects with fields [group_id, user_id, verb_id, object_id, timestamp]
    :param group:
    :type group:
    :return:
    :rtype:
    """

    # forum posts
    forumQuery = {
        "verb.id": "http://id.tincanapi.com/verb/replied",
        "object.definition.type": "http://id.tincanapi.com/activitytype/forum-topic"
    }
    forumContentSchema = "$object.definition.extensions.message"

    # wiki edits
    wikiQuery = {
        "verb.id": "http://id.tincanapi.com/verb/updated",
        "object.definition.type": "http://collide.info/moodle_wiki_page"
    }
    forumContentSchema = "$object.definition.extensions.message"

    # git commits


    db.getCollection('xapi_statements').aggregate([
        {"$match": {"context.groups.id": "16"}},
        {"$project": {
            "group_id": "16",
            "user_id": "$actor.name",
            "verb_id": "$verb.id",
            "object_id": "$object.id",
            "timestamp": "$timestamp",
            "object_type": "$object.definition.type",
            "object_name": "$object.definition.name.en"
        }
        }
    ])
    # # TODO Project content especially forum post text
    # users = get_all_users_for_group(course, group, *constraints)
    # projection = {
    #     "object_id": "$" + artefact_schema,
    #     "verb_id": "$" + verb_schema,
    #     "timestamp": True,
    #     "object_type": "$" + artefact_type_schema,
    #     "object_name": "$" + "object.definition.name",
    #     "forum_content": "$" + "object.definition.extensions.message",
    #     "wiki_content": "$" + "context.extensions.other"
    # }
    # group_activities = []
    # for user in users:
    #
    #     query = merge_query(user_query(user), group_query(group), *constraints)
    #     aggregation = [
    #         {"$match": query},
    #         {"$project": projection},
    #     ]
    #     user_statements = list(con.db.xapi_statements.aggregate(aggregation))
    #
    #     for statement in user_statements:
    #
    #         activity = {
    #             "group_id": group,
    #             "user_id": user,
    #             "verb_id": statement["verb_id"],
    #             "object_id": statement["object_id"],
    #             "timestamp": statement["timestamp"],
    #             "object_type": statement["object_type"],
    #             "object_name": list(statement["object_name"].values())[0],
    #         }
    #
    #         #TODO fix: only write object content if not empty
    #         if "forum_content" in statement:
    #             if statement["forum_content"]:
    #                 activity["forum_content"] = statement["forum_content"]
    #
    #         #TODO fix: only write object content if not empty
    #         print(statement["verb_id"])
    #         if not statement["verb_id"] == "http://id.tincanapi.com/verb/replied":
    #             activity["wiki_content"] = statement["wiki_content"]
    #
    #
    #         group_activities.append(activity)
    # group_activities = [item for item in group_activities if item["timestamp"] > start_time]
    group_activities.sort(key=lambda x: x["timestamp"], reverse=True)
    return group_activities

def get_group_activities_for_task(course, group, start_time, task):
    get_group_activities(course, group, start_time, group_task_query(task))

def get_all_task_activities(task):
    get_group_activities(course, group, start_time, group_task_query(task))

# def get_group_average_latency(startpoint, group, course, *constraints):
#     users = get_all_users_for_group(course, group)
#     group_times = []
#     for user in users:
#         constraints = list(constraints) + [group_query(group)]
#         user_times = get_all_user_times(user, course, *constraints)
#         time_tuples = [(time, user) for time in user_times]
#         group_times.extend(time_tuples)
#
#     group_times.sort()
#     response_times = []
#     current_time = startpoint
#     current_user = None
#     for time, user in group_times:
#         if user != current_user:
#             diff_time = time - current_time
#             current_time = time
#             response_times.append(diff_time)
#
#     avg_latency = sum(response_times)/len(response_times)
#
#     return avg_latency

def update_group(group, course):
    con.db.groups.update({"id": group["id"], "courseid": course}, group, upsert=True)


def update_group_task(task, course):
    con.db.grouptasks.update({"task_id": task["task_id"], "courseid": course}, task, upsert=True)