import random

# https://moodle.ikarion-projekt.de/mod/forum/view.php?id={}
ARTEFACT_TEMPLATE = "https://moodle.test-data.de/mod/{}/view.php?id={}"


def fill_user_model(uid, course, active_days, n_artifacts, *,
                    updated_at=1416649608,
                    base_time=1517443200.0,
                    num_actions=1,
                    randomized=False):
    skeleton = create_user_skeleton()
    skeleton["uid"] = str(uid)
    skeleton["course"] = str(course)
    skeleton["updated_at"] = str(updated_at)
    skeleton["active_days"] = active_days

    artifacts_actions = {"videos": ["viewed"],
                         "literature": ["viewed"],
                         "forum_posts": ["viewed", "created"],
                         "quizzes": ["taken"],
                         "wiki_articles": ["viewed", "updated"]}

    for artifact_type, action_types in artifacts_actions.items():
        for action_type in action_types:
            for n in range(n_artifacts):
                action_id = ARTEFACT_TEMPLATE.format(artifact_type, n)
                for n_actions in range(num_actions):
                    if randomized:
                        added_time = random.random()*(n_actions * 3600)
                    else:
                        added_time = (n_actions * 3600)
                    time_stamp = base_time + added_time
                    action_data = create_action(action_id, time_stamp)
                    add_action(skeleton, artifact_type, action_type, action_data)

    return skeleton


def create_user_skeleton():
    skeleton = {
        "uid": "user_id",
        "course": "course_id",
        "updated_at": "last_update_timestamp",
        "active_days": [1, 2],
        "artifacts": {
            "videos": {
                "viewed": []
            },
            "literature": {
                "viewed": []
            },
            "forum_posts": {
                "viewed": [],
                "created": []
            },
            "quizzes": {
                "taken": []
            },
            "wiki_articles": {
                "viewed": [],
                "updated": []
            }
        }
    }
    return skeleton


def add_action(user_model, artifact_type, action, action_data):
    user_model["artifacts"][artifact_type][action] = action_data


def create_action(action_id, time, **kwargs):
    action_data = {
        "id": action_id,
        "time": time,
    }
    return {**action_data, **kwargs}




