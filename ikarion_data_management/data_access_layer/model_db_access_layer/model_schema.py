
user_model_schema = {
    "uid": "user_id",
    "course": "course_id",
    "updated_at": "last_update_timestamp",
    "active_days": [1, 2],
    "artifacts": {
        "videos": {
            "viewed": [{
                "id": "xapi_id",
                "name": "opt_name",
                "#views": 10
            }]
        },
        "literature": {
            "viewed": [{
                "id": "xapi_id",
                "name": "opt_name",
                "#views": 10
            }]
        },
        "forum_posts": {
            "viewed": [{
                "id": "xapi_id",
                "name": "opt_name",
                "#views": 10,
                "forum": "forum_id"
            }],
            "created": [{
                "id": "xapi_id",
                "name": "opt_name"
            }]
        },
        "quizzes": {
            "taken": [{
                "id": "xapi_id",
                "name": "opt_name"
            }]
        },
        "wiki_articles": {
            "viewed": [{
                "id": "xapi_id",
                "name": "opt_name",
                "#views": 10
            }],
            "updated": [{
                "id": "xapi_id",
                "name": "opt_name"
            }]
        }
    }
}

group_model_schema = {
    "groupid": "group_id",
    "course": "course_id",
    "group_members"
    "updated_at": "last_update_timestamp",
    "concepts_used":"list of used concepts",
    "concept_coverage":"proportion covered to overall concepts",
    "text_length":"length of produced text",
    "artifacts": {
        "videos": {
            "viewed": [{
                "id": "xapi_id",
                "name": "opt_name",
                "#views": 10
            }]
        },
        "literature": {
            "viewed": [{
                "id": "xapi_id",
                "name": "opt_name",
                "#views": 10
            }]
        },
        "forum_posts": {
            "viewed": [{
                "id": "xapi_id",
                "name": "opt_name",
                "#views": 10,
                "forum": "forum_id"
            }],
            "created": [{
                "id": "xapi_id",
                "name": "opt_name"
            }]
        },
        "quizzes": {
            "taken": [{
                "id": "xapi_id",
                "name": "opt_name"
            }]
        },
        "wiki_articles": {
            "viewed": [{
                "id": "xapi_id",
                "name": "opt_name",
                "#views": 10
            }],
            "updated": [{
                "id": "xapi_id",
                "name": "opt_name"
            }]
        }
    }
}
