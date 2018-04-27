import random
import ikarion_data_management.log_aggregator.statement_processing as sp

# https://moodle.ikarion-projekt.de/mod/forum/view.php?id={}
ARTEFACT_TEMPLATE = "https://moodle.test-data.de/mod/{}/view.php?id={}"


# def fill_user_model(uid, course, active_days, n_artifacts, *,
#                     updated_at=1416649608,
#                     base_time=1517443200.0,
#                     num_actions=1,
#                     randomized=False):
#     skeleton = create_user_skeleton()
#     skeleton["uid"] = str(uid)
#     skeleton["course"] = str(course)
#     skeleton["updated_at"] = str(updated_at)
#     skeleton["active_days"] = active_days
#
#     artifacts_actions = {"videos": ["viewed"],
#                          "literature": ["viewed"],
#                          "forum_posts": ["viewed", "created"],
#                          "quizzes": ["taken"],
#                          "wiki_articles": ["viewed", "updated"]}
#
#     for artifact_type, action_types in artifacts_actions.items():
#         for action_type in action_types:
#             for n in range(n_artifacts):
#                 action_id = ARTEFACT_TEMPLATE.format(artifact_type, n)
#                 for n_actions in range(num_actions):
#                     if randomized:
#                         added_time = random.random()*(n_actions * 3600)
#                     else:
#                         added_time = (n_actions * 3600)
#                     time_stamp = base_time + added_time
#                     action_data = create_action(action_id, time_stamp)
#                     add_action(skeleton, artifact_type, action_type, action_data)
#
#     return skeleton
#
#
# def create_user_skeleton():
#     skeleton = {
#         "uid": "user_id",
#         "course": "course_id",
#         "updated_at": "last_update_timestamp",
#         "active_days": [1, 2],
#         "artifacts": {
#             "videos": {
#                 "viewed": []
#             },
#             "literature": {
#                 "viewed": []
#             },
#             "forum_posts": {
#                 "viewed": [],
#                 "created": []
#             },
#             "quizzes": {
#                 "taken": []
#             },
#             "wiki_articles": {
#                 "viewed": [],
#                 "updated": []
#             }
#         }
#     }
#     return skeleton
#
#
# def add_action(user_model, artifact_type, action, action_data):
#     user_model["artifacts"][artifact_type][action] = action_data
#
#
# def create_action(action_id, time, **kwargs):
#     action_data = {
#         "id": action_id,
#         "time": time,
#     }
#     return {**action_data, **kwargs}


def generate_xapi_statement(*, user, course, time, verb, artefact, group=None, process=True):
    statement = {
        "stored": "2018-03-15T12:19:47.424Z",
        "context": {
            "extensions": {
                "http://lrs.learninglocker.net/define/extensions/info": {
                    "https://moodle.org/": "3.2.3+ (Build: 20170509)"
                },
                "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log": {
                    "realuserid": None,
                    "eventname": "\\core\\event\\course_viewed",
                    "userid": "22",
                    "origin": "web",
                    "ip": "134.91.34.168",
                    "contextid": 212,
                    "anonymous": 0,
                    "edulevel": 2,
                    "objecttable": None,
                    "other": "N;",
                    "target": "course",
                    "relateduserid": None,
                    "contextlevel": 50,
                    "action": "viewed",
                    "courseid": course,
                    "groupid": group,
                    "objectid": None,
                    "timecreated": 1521116387,
                    "component": "core",
                    "crud": "r",
                    "contextinstanceid": "7"
                }
            },
            "language": "en",
            "platform": "Moodle",
            "contextActivities": {
                "grouping": [
                    {
                        "definition": {
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_course": {
                                    "cacherev": "1518181284",
                                    "showreports": "0",
                                    "groupmode": "0",
                                    "idnumber": "",
                                    "completionnotify": "0",
                                    "summary": "",
                                    "shortname": "IKARion Projekt",
                                    "maxbytes": "0",
                                    "theme": "",
                                    "enddate": "0",
                                    "groupmodeforce": "0",
                                    "newsitems": "3",
                                    "legacyfiles": "0",
                                    "lang": "",
                                    "requested": "0",
                                    "url": "https://moodle.ikarion-projekt.de",
                                    "sortorder": "1",
                                    "startdate": "0",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1500014049",
                                    "format": "site",
                                    "calendartype": "",
                                    "showgrades": "1",
                                    "marker": "0",
                                    "fullname": "IKARion Projekt",
                                    "type": "site",
                                    "id": "1",
                                    "timecreated": "1500013772",
                                    "summaryformat": "0",
                                    "category": "0",
                                    "enablecompletion": "0",
                                    "defaultgroupingid": "0"
                                }
                            },
                            "description": {
                                "en": "IKARion Projekt"
                            },
                            "name": {
                                "en": "IKARion Projekt"
                            },
                            "type": "http://id.tincanapi.com/activitytype/site"
                        },
                        "id": "https://moodle.ikarion-projekt.de",
                        "objectType": "Activity"
                    }
                ],
                "category": [
                    {
                        "definition": {
                            "description": {
                                "en": "Moodle is a open source learning platform designed to provide educators, administrators and learners with a single robust, secure and integrated system to create personalised learning environments."
                            },
                            "name": {
                                "en": "Moodle"
                            },
                            "type": "http://id.tincanapi.com/activitytype/source"
                        },
                        "id": "http://moodle.org",
                        "objectType": "Activity"
                    }
                ]
            }
        },
        "actor": {
            "account": {
                "homePage": "https://moodle.ikarion-projekt.de",
                "name": "22"
            },
            "name": user,
            "objectType": "Agent"
        },
        "timestamp": time,
        "version": "1.0.0",
        "id": "f6ece7a5-97c1-4e9a-8694-1c52422539fa",
        "verb": {

            "display": {
                "en": "viewed"
            },
            "id": verb
        },
        "object": {
            "definition": {
                "extensions": {
                    "http://lrs.learninglocker.net/define/extensions/moodle_course": {
                        "cacherev": "1521116362",
                        "showreports": "0",
                        "groupmode": "0",
                        "idnumber": "",
                        "completionnotify": "0",
                        "summary": "<p>Dieser kurze Online Kurs gibt den Teilnehmern einen Überblick über die Entwicklung von Webapplikationen mittels diverser moderner Javascript Frameworks. Neben der Vermittlung von Grundlagen und Praxiswissen, erarbeiten die Teilnehmer in Kleingruppen selbständig kleinere Beispielapplikationen.<br></p>",
                        "shortname": "modweb",
                        "maxbytes": "0",
                        "theme": "",
                        "enddate": "0",
                        "groupmodeforce": "0",
                        "newsitems": "5",
                        "legacyfiles": "0",
                        "lang": "",
                        "requested": "0",
                        "url": "https://moodle.ikarion-projekt.de/course/view.php?id=7",
                        "sortorder": "10002",
                        "startdate": "1519862400",
                        "visible": "1",
                        "visibleold": "1",
                        "timemodified": "1521113627",
                        "format": "topics",
                        "calendartype": "",
                        "showgrades": "1",
                        "marker": "0",
                        "fullname": "Moderne Webframeworks (Microcourse)",
                        "type": "course",
                        "id": "7",
                        "timecreated": "1515428730",
                        "summaryformat": "1",
                        "category": "1",
                        "enablecompletion": "1",
                        "defaultgroupingid": "0"
                    }
                },
                "description": {
                    "en": "Dieser kurze Online Kurs gibt den Teilnehmern einen Überblick über die Entwicklung von Webapplikationen mittels diverser moderner Javascript Frameworks. Neben der Vermittlung von Grundlagen und Praxiswissen, erarbeiten die Teilnehmer in Kleingruppen selbständig kleinere Beispielapplikationen."
                },
                "name": {
                    "en": "Moderne Webframeworks (Microcourse)"
                },
                "type": "http://lrs.learninglocker.net/define/type/moodle/course"
            },
            "id": artefact,
            "objectType": "Activity"
        }
    }
    if process:
        sp.process_statement(statement)

    return statement
