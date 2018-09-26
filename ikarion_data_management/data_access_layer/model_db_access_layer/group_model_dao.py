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


def get_groups_users_for_task(task):
    query = {"task.task_id" : task}
    groups = list(con.db.groups.find(query, {"_id": 0}))
    return groups

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

def get_all_groups_for_task(course, task):

    query = {
        "task.task_id": task,
        "courseid": course
    }

    return list(con.db.groups.find(query, {"_id": 0}))

def get_group_activities(course, group, *constraints):
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
    forumContentProjection = {"content": "$object.definition.extensions.message"}

    # wiki edits
    wikiQuery = {
        "verb.id": "http://id.tincanapi.com/verb/updated",
        "object.definition.type": "http://collide.info/moodle_wiki_page"
    }
    wikiContentProjection = {"content": "$object.definition.extensions.content_clean"}

    # git commits
    # TODO: Query Git commits.

    projection = {
        "_id": 0,
        "group_id": group,
        "user_id": "$" + user_schema,
        "verb_id": "$verb.id",
        "object_id": "$object.id",
        "timestamp": "$timestamp",
        "object_type": "$object.definition.type",
        "object_name": "$object.definition.name.en",
        "content": "$object.definition.extensions.message"

    }

    forumPosts = list(

        con.db.xapi_statements.aggregate([
            {"$match": merge_query(course_query(course), group_query(group), forumQuery, *constraints)},
            {"$unwind": "$object.definition.extensions"},
            {"$project": merge_query(projection, forumContentProjection)}
        ])
    )

    wikiEdits = list(
        con.db.xapi_statements.aggregate([
            {"$match": merge_query(course_query(course), group_query(group), wikiQuery, *constraints)},
            {"$unwind": "$object.definition.extensions"},
            {"$project": merge_query(projection, wikiContentProjection)}
        ])
    )
    combList = (wikiEdits + forumPosts)
    combList.sort(key=lambda x: x["timestamp"], reverse=True)

    return combList


def get_group_activities_for_task(course, group, task, *constraints):

    return get_group_activities(course, group, group_task_query(task))

def get_all_task_activities(course, task):
    # TODO: Make sure that task id is a url (course_id + task_id). In this case the course query is not necessary.
    # TODO: Reuse get_group_activities
    query = merge_query(
        group_task_query(task),
        {"relevant_group_task.courseid": course}
    )

    projection = {
        "$project": {
            "_id": 0,
            "group_id": "relevant_group_task.id",
            "user_id": "$" + user_schema,
            "verb_id": "$verb.id",
            "object_id": "$object.id",
            "timestamp": "$timestamp",
            "object_type": "$object.definition.type",
            "object_name": "$object.definition.name.en",
        }
    }

    return con.db.xapi_statements.aggregate([query, projection])


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