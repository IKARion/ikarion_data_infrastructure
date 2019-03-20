# Standart queries
course_list_query = [
    {"$match": {
        "context.contextActivities.grouping": {
            "$elemMatch": {"definition.type": "http://lrs.learninglocker.net/define/type/moodle/course"}
        }
    }},
    {"$project": {
        "course": {
            "$filter": {
                "input": "$context.contextActivities.grouping",
                "as": "item",
                "cond": {"$eq": ["$$item.definition.type", "http://lrs.learninglocker.net/define/type/moodle/course"]}
            }
        }
    }},
    {"$unwind": "$course"},
    {"$unwind": "$course.definition.extensions"},
    {"$group": {
        "_id": {"courseid": "$course.definition.extensions.url", "name": "$course.definition.extensions.fullname"}
    }},
    {"$project": {
        "_id": 0, "courseid": "$_id.courseid", "name": "$_id.name"
    }}
]


def course_query(course):
    # if course is None:
    #     return {}
    # else:
    #     query = {
    #         "context.contextActivities.grouping" : {
    #             "$elemMatch" : {
    #                 "definition.type" : "http://lrs.learninglocker.net/define/type/moodle/course",
    #                 "definition.extensions" : {
    #                     "$elemMatch" : {"url" : course}
    #                 }
    #             }
    #         }
    #     }
    query = {"course_id": course}
    return query
