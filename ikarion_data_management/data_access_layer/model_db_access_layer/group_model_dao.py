from .. import modelDBConnection as con
from .util import *
from .queries import course_list_query, course_query
from .nlp import concept_match
import json
from collections import defaultdict

assessment_type_id = "https://moodle.ikarion-projekt.de/define/type/moodle/block_groupactivity"


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
    all_latencies = list()  # list of latencies between all activities

    for i in range(len(action_sequence)):
        if i == 0:
            # do nothing for first activity
            first_activity = action_sequence[i]['start']
        else:
            # calculate time between current and previous activity
            current = action_sequence[i]
            previous = action_sequence[i - 1]
            latency = int(current['start']) - int(previous['start'])
            all_latencies.append(latency)
            overall_latency = overall_latency + latency

    # calculate average latency
    average_latency = round(overall_latency / (elem_count - 1))

    return average_latency, all_latencies


def get_groups_users_for_task(task):
    query = {"task.task_id": task}
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
        "object_name": "$object.definition.name",
        "content": "$object.definition.extensions.message"

    }
    forum_query = merge_query(course_query(course), group_query(group), forumQuery, *constraints)
    forumPosts = list(

        con.db.xapi_statements.aggregate([
            {"$match": forum_query},
            {"$unwind": "$object.definition.extensions"},
            {"$project": merge_query(projection, forumContentProjection)}
        ])
    )

    wiki_query = merge_query(course_query(course), group_query(group), wikiQuery, *constraints)
    wikiEdits = list(
        con.db.xapi_statements.aggregate([
            {"$match": wiki_query},
            {"$unwind": "$object.definition.extensions"},
            {"$project": merge_query(projection, wikiContentProjection)}
        ])
    )
    combList = (wikiEdits + forumPosts)
    combList.sort(key=lambda x: x["timestamp"], reverse=True)
    for item in combList:
        o_n = item["object_name"]
        item["object_name"] = list(o_n.values())[0]

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

def get_group_weighted_wiki_count_for_task(course, group, task_id, timestamp, *constraints):
    return get_group_weighted_wiki_word_count(course, group, timestamp, group_task_query(task_id))


def get_group_interventions_for_task(course, group_id, task_id, timestamp, *constraints):


    task_query = {
        "task_id": task_id,
        "courseid": course,
    }
    task = con.db.grouptasks.find_one(task_query)
    task_start = int(task["task_start"])
    task_end = int(task["task_end"])

    intervention_latency_query = {
        "verb.id": "http://id.tincanapi.com/verb/viewed",
        "object.definition.type": "https://moodle.ikarion-projekt.de/define/type/moodle/block_grouplatency"
    }

    intervention_activity_query = {
        "verb.id": "http://id.tincanapi.com/verb/viewed",
        "object.definition.type": "https://moodle.ikarion-projekt.de/define/type/moodle/block_groupactivity"
    }

    projection = {
        "_id": 0,
        "user_id": "$" + user_schema,
        "verb_id": "$verb.id",
        "object_id": "$object.id",
        "timestamp": "$timestamp",
        "object_type": "$object.definition.type",
        "object_name": "$object.definition.name",
        "content": "$object.definition.extensions.promptmessage",
    }

    latency_query = merge_query(course_query(course), group_query(group_id),
                                intervention_latency_query, *constraints)

    activity_query = merge_query(course_query(course), group_query(group_id),
                                 intervention_activity_query, *constraints)

    latency_prompts = list(
        con.db.xapi_statements.aggregate([
            {"$match": latency_query},
            {"$unwind": "$object.definition.extensions"},
            {"$project": projection}
        ])
    )
    latency_prompts = [item for item in latency_prompts if item["timestamp"] <= timestamp]

    activity_prompts = list(
        con.db.xapi_statements.aggregate([
            {"$match": activity_query},
            {"$unwind": "$object.definition.extensions"},
            {"$project": projection}
        ])
    )
    activity_prompts = [item for item in activity_prompts if item["timestamp"] <= timestamp]

    combList = (latency_prompts + activity_prompts)
    combList = [item for item in combList if task_start <= item["timestamp"] <= task_end]
    combList.sort(key=lambda x: x["timestamp"], reverse=True)
    for item in combList:
        o_n = item["object_name"]
        item["object_name"] = list(o_n.values())[0]

    return combList


def get_group_weighted_wiki_word_count(course, group_id, timestamp, *constraints):
    group = con.db.groups.find_one({"id": group_id, "courseid": course})
    user_names = []
    for g_member in group["group_members"]:
        user_name = g_member["name"]
        user_names.append(user_name)

    try:
        # wiki edits
        wikiQuery = {
            "verb.id": "http://id.tincanapi.com/verb/updated",
            "object.definition.type": "http://collide.info/moodle_wiki_page"
        }
        wikiContentProjection = {"content": "$object.definition.extensions.content_clean"}

        projection = {
            "_id": 0,
            "user_id": "$" + user_schema,
            "verb_id": "$verb.id",
            "object_id": "$object.id",
            "timestamp": "$timestamp",
            "object_type": "$object.definition.type",
            "object_name": "$object.definition.name",
            "content": "$object.definition.extensions.message",
            "wiki_concepts": "$wiki_concepts",

        }

        wiki_query = merge_query(course_query(course), group_query(group_id), wikiQuery, *constraints)
        wiki_edits = list(
            con.db.xapi_statements.aggregate([
                {"$match": wiki_query},
                {"$unwind": "$object.definition.extensions"},
                {"$project": merge_query(projection, wikiContentProjection)}
            ])
        )
        wiki_edits = [item for item in wiki_edits if item["timestamp"] < timestamp]
        wiki_edits.sort(key=lambda x: x["timestamp"])
        wiki_edits = [item for item in wiki_edits if "wiki_concepts" in item]
        wiki_start = {
            "user_id": "wiki_start",
            "wiki_concepts": [],
        }
        wiki_edits.insert(0, wiki_start)
        user_concept_additions = {user_name: [] for user_name in user_names}
        wiki_concepts_per_user = []
        for item_1, item_2 in zip(wiki_edits[:-1], wiki_edits[1:]):
            # user_before = item_1["user_id"]
            concepts_before = item_1["wiki_concepts"]
            c_count_before = sum([cc["score"] * cc["count"] for cc in concepts_before])
            user_after = item_2["user_id"]
            concepts_after = item_2["wiki_concepts"]
            c_count_after = sum([cc["score"] * cc["count"] for cc in concepts_after])
            wiki_concepts_per_user.append({"user_id": user_after, "concepts": concepts_after})
            if c_count_after > c_count_before:
                added_concept_count = c_count_after - c_count_before
            else:
                added_concept_count = 0
            user_concept_additions[user_after].append(added_concept_count)

        user_concept_counts = {user_id: sum(concept_additions)
                               for user_id, concept_additions in user_concept_additions.items()}

        concept_sum = sum([item for item in user_concept_counts.values()])
        if concept_sum == 0:
            user_concept_counts_norm = [{
                "user": user_id,
                "weighted_wiki_wordcount": 0,
                "group_id": group_id,
            }
                for user_id, concept_count in user_concept_counts.items()]
        else:
            user_concept_counts_norm = [{
                "user": user_id,
                "weighted_wiki_wordcount": concept_count / concept_sum,
                "group_id": group_id,
            }
                for user_id, concept_count in user_concept_counts.items()]
    except:
        wiki_concepts_per_user = []
        user_concept_counts_norm = [{
            "user": user_id,
            "weighted_wiki_wordcount": 0,
            "group_id": group_id,
        }
            for user_id in user_names]

    return user_concept_counts_norm, wiki_concepts_per_user


def get_group_self_assesment(course, group_id, task_id, timestamp):
    group = con.db.groups.find_one({"id": group_id})
    user_assessments = []
    for g_member in group["group_members"]:
        user_name = g_member["name"]
        query = merge_query(
            group_task_query(task_id),
            {"relevant_group_task.courseid": course},
            group_query(group_id),
            {"object.definition.type": assessment_type_id},
            {user_schema: user_name},
            {"timestamp": {"$lt": timestamp}},
        )

        query = {"$match": query}

        projection = {
            "$project": {
                "_id": 0,
                "group_id": "relevant_group_task.id",
                "user_id": "$" + user_schema,
                "verb_id": "$verb.id",
                "object_id": "$object.id",
                "timestamp": "$timestamp",
                "object_type": "$object.definition.type",
                "object_name": "$object.definition.name",
                "object": "$object",
            }
        }
        sorting = {
            "$sort": {"timestamp": -1}
        }
        limit = {
            "$limit": 10
        }
        pipeline = [query, projection, sorting, limit]
        # pipeline = [projection, sorting, limit]

        user_assesment_statements = list(con.db.xapi_statements.aggregate(pipeline))
        if len(user_assesment_statements) == 0:
            continue
        user_assesment_statement = user_assesment_statements[0]

        extensions = user_assesment_statement["object"]["definition"]["extensions"]
        for ext in extensions:
            if ext["id"] == "http://lrs.learninglocker.net/define/extensions/moodle_block":
                data = {
                    "group_id": group_id,
                    "user_id": g_member["name"],
                    "timestamp": user_assesment_statement["timestamp"]
                }
                for i, item in enumerate(ext["items"]):
                    data["item{}".format(i + 1)] = item["value"]
                user_assessments.append(data)
    return user_assessments


def calc_wiki_concepts(wiki_text, task_name):
    split_name = task_name.split("_")
    task_prefix = "_".join(split_name[:2])
    task_concepts_list = list(con.db.task_concepts.find({"task_prefix": task_prefix}))
    if task_concepts_list:
        task_concepts = task_concepts_list[0]
        concept_list = task_concepts["concepts"]
    else:
        concept_list = []

    matched_concepts = concept_match(concept_list, wiki_text)
    return matched_concepts


def update_group(group, course):
    db_group = con.db.groups.find_one({"id": group["id"], "courseid": course})
    if db_group is None:
        con.db.groups.replace_one({"id": group["id"], "courseid": course}, group, upsert=True)
    else:
        n_members_db = len(db_group["group_members"])
        n_members = len(group["group_members"])
        if n_members > n_members_db:
            con.db.groups.replace_one({"id": group["id"], "courseid": course}, group, upsert=True)


def update_group_task(task, course):
    con.db.grouptasks.replace_one({"task_id": task["task_id"], "courseid": course}, task, upsert=True)
