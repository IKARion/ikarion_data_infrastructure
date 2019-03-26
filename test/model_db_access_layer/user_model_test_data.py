import random
import ikarion_data_management.log_aggregator.statement_processing as sp
import json

# https://moodle.ikarion-projekt.de/mod/forum/view.php?id={}
ARTEFACT_TEMPLATE = "https://moodle.test-data.de/mod/{}/view.php?id={}"


def generate_xapi_statement(*, user, course, time, verb, artefact, group=None, process=True):
    statement = {
        "authority": {
            "objectType": "Agent",
            "name": "New Client",
            "mbox": "mailto:hello@learninglocker.net"
        },
        "stored": "2018-05-17T12:40:39.420Z",
        "context": {
            "extensions": {
                "http://collide.info/extensions/group": {
                    group: {
                        "timemodified": "1525691977",
                        "timecreated": "1525691046",
                        "description": "none",
                        "name": "Gruppe 4",
                        "id": group
                    }
                },
                "http://lrs.learninglocker.net/define/extensions/info": {
                    "https://moodle.org/": "3.2.3+ (Build: 20170509)"
                },
                "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log": {
                    "realuserid": None,
                    "eventname": "\\mod_forum\\event\\discussion_viewed",
                    "userid": "68",
                    "origin": "web",
                    "ip": "134.91.34.237",
                    "contextid": 254,
                    "anonymous": 0,
                    "edulevel": 2,
                    "objecttable": "forum_discussions",
                    "other": "N;",
                    "target": "discussion",
                    "relateduserid": None,
                    "contextlevel": 70,
                    "action": "viewed",
                    "courseid": course,
                    "objectid": "83",
                    "timecreated": 1526560839,
                    "component": "mod_forum",
                    "crud": "r",
                    "contextinstanceid": "73"
                }
            },
            "language": "de",
            "platform": "Moodle",
            "contextActivities": {
                "grouping": [
                    {
                        "definition": {
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_course": {
                                    "cacherev": "1525772347",
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
                                    "timemodified": "1524571833",
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
                                "de": "IKARion Projekt"
                            },
                            "name": {
                                "de": "IKARion Projekt"
                            },
                            "type": "http://id.tincanapi.com/activitytype/site"
                        },
                        "id": "https://moodle.ikarion-projekt.de",
                        "objectType": "Activity"
                    },
                    {
                        "definition": {
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_course": {
                                    "cacherev": "1526558295",
                                    "showreports": "1",
                                    "groupmode": "0",
                                    "idnumber": "",
                                    "completionnotify": "0",
                                    "summary": "<p>Dieser kurze Online Kurs gibt den Teilnehmern einen Überblick über die Entwicklung von Webapplikationen mittels diverser moderner Javascript Frameworks. Neben der Vermittlung von Grundlagen und Praxiswissen, erarbeiten die Teilnehmer in Kleingruppen selbständig kleinere Beispielapplikationen.</p><p>Bei Fragen bitte per Email wenden an:</p><ul><li>Tobias Hecking (hecking@collide.info)</li><li>Dorian Doberstein (doberstein@collide.info)</li><li>Lydia Harbarth (harbarth@collide.info)</li></ul><p>(Betreff: \"Frage zum Mikrokurs\")<br></p>",
                                    "shortname": "modweb",
                                    "maxbytes": "0",
                                    "theme": "",
                                    "enddate": "0",
                                    "groupmodeforce": "0",
                                    "newsitems": "5",
                                    "legacyfiles": "0",
                                    "lang": "de",
                                    "requested": "0",
                                    "url": "https://moodle.ikarion-projekt.de/course/view.php?id={}".format(course),
                                    "sortorder": "10001",
                                    "startdate": "1525042800",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1525101857",
                                    "format": "topics",
                                    "calendartype": "",
                                    "showgrades": "1",
                                    "marker": "0",
                                    "fullname": "Moderne Webtechnologien (Microcourse)",
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
                                "de": "Dieser kurze Online Kurs gibt den Teilnehmern einen Überblick über die Entwicklung von Webapplikationen mittels diverser moderner Javascript Frameworks. Neben der Vermittlung von Grundlagen und Praxiswissen, erarbeiten die Teilnehmer in Kleingruppen selbständig kleinere Beispielapplikationen.Bei Fragen bitte per Email wenden an:Tobias Hecking (hecking@collide.info)Dorian Doberstein (doberstein@collide.info)Lydia Harbarth (harbarth@collide.info)(Betreff: \"Frage zum Mikrokurs\")"
                            },
                            "name": {
                                "de": "Moderne Webtechnologien (Microcourse)"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/course"
                        },
                        "id": "https://moodle.ikarion-projekt.de/course/view.php?id={}".format(course),
                        "objectType": "Activity"
                    },
                    {
                        "definition": {
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_module": {
                                    "introformat": "0",
                                    "displaywordcount": "0",
                                    "assessed": "0",
                                    "assesstimefinish": "0",
                                    "maxbytes": "0",
                                    "lockdiscussionafter": "0",
                                    "scale": "0",
                                    "name": "Nachrichtenforum",
                                    "rsstype": "0",
                                    "completionreplies": "0",
                                    "intro": "In diesem Forum werden verschiedene Kursinformationen und Ankündigungen durch den Kursleiter veröffentlicht.",
                                    "maxattachments": "1",
                                    "blockperiod": "0",
                                    "blockafter": "0",
                                    "url": "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=73",
                                    "rssarticles": "0",
                                    "completiondiscussions": "0",
                                    "trackingtype": "1",
                                    "assesstimestart": "0",
                                    "timemodified": "1518683250",
                                    "warnafter": "0",
                                    "completionposts": "0",
                                    "type": "forum",
                                    "course": "7",
                                    "id": "16",
                                    "forcesubscribe": "1"
                                }
                            },
                            "description": {
                                "de": "In diesem Forum werden verschiedene Kursinformationen und Ankündigungen durch den Kursleiter veröffentlicht."
                            },
                            "name": {
                                "de": "Nachrichtenforum"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/forum"
                        },
                        "id": "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=73",
                        "objectType": "Activity"
                    }
                ],
                "category": [
                    {
                        "definition": {
                            "description": {
                                "de": "Moodle is a open source learning platform designed to provide educators, administrators and learners with a single robust, secure and integrated system to create personalised learning environments."
                            },
                            "name": {
                                "de": "Moodle"
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
                "name": "68"
            },
            "name": user,
            "objectType": "Agent"
        },
        "timestamp": time,
        "version": "1.0.0",
        "id": "b7ed4996-2688-474e-bb57-506fca4b6e47",
        "verb": {
            "display": {
                "en": "viewed"
            },
            "id": verb
        },
        "object": {
            "definition": {
                "extensions": {
                    "http://lrs.learninglocker.net/define/extensions/moodle_discussion": {
                        "forum": "16",
                        "assessed": "0",
                        "userid": "12",
                        "name": "Beginn Woche 2",
                        "timeend": "0",
                        "url": "https://moodle.ikarion-projekt.de/mod/forum/discuss.php?d=83",
                        "firstpost": "111",
                        "usermodified": "12",
                        "timestart": "1525727100",
                        "timemodified": "1525705088",
                        "pinned": "0",
                        "type": "forum_discussions",
                        "groupid": "-1",
                        "course": "7",
                        "id": "83"
                    }
                },
                "description": {
                    "de": "A Moodle discussion."
                },
                "name": {
                    "de": "Beginn Woche 2"
                },
                "type": 'http://id.tincanapi.com/activitytype/forum-topic',
            },
            "id": artefact,
            "objectType": "Activity"
        }
    }
    if process:
        sp.process_statement(statement)

    return statement


def generate_xapi_statement2(*, user, course, time, verb, artefact, group=None, process=True):
    statement = {
        "authority": {
            "objectType": "Agent",
            "name": "New Client",
            "mbox": "mailto:hello@learninglocker.net"
        },
        "stored": "2018-09-06T10:20:49.931Z",
        "context": {
            "extensions": {
                "http://collide.info/extensions/group": {
                    "29": {
                        "group_members": [
                            {
                                "fullname": "test_firstname_3 test_lastname_3",
                                "email": "test_email_3@abc.invalid",
                                "username": "test_user_3"
                            },
                            {
                                "fullname": "test_firstname_5 test_lastname_5",
                                "email": "test_email_5@abc.invalid",
                                "username": "test_user_5"
                            },
                            {
                                "fullname": "test_firstname_7 test_lastname_7",
                                "email": "test_email_7@abc.invalid",
                                "username": "test_user_7"
                            },
                            {
                                "fullname": "test_firstname_8 test_lastname_8",
                                "email": "test_email_8@abc.invalid",
                                "username": "test_user_8"
                            },
                            {
                                "fullname": "test_firstname_11 test_lastname_11",
                                "email": "test_email_11@abc.invalid",
                                "username": "test_user_11"
                            },
                            {
                                "fullname": "test_firstname_18 test_lastname_18",
                                "email": "test_email_18@abc.invalid",
                                "username": "test_user_18"
                            },
                            {
                                "fullname": "test_firstname_19 test_lastname_19",
                                "email": "test_email_19@abc.invalid",
                                "username": "test_user_19"
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "http://localhost/ikarion_moodle/mod/assign/view.php?id=3",
                                "http://localhost/ikarion_moodle/mod/forum/view.php?id=4"
                            ],
                            "task_type": "collaborative programming",
                            "task_end": "1536751800",
                            "task_start": "1536147000",
                            "task_name": "the new task",
                            "task_id": "2"
                        },
                        "timemodified": "1536147081",
                        "timecreated": "1536147081",
                        "description": "none",
                        "name": "Group A",
                        "id": group
                    }
                },
                "http://lrs.learninglocker.net/define/extensions/info": {
                    "https://moodle.org/": "3.2.3+ (Build: 20170509)"
                },
                "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log": {
                    "realuserid": "2",
                    "eventname": "\\mod_forum\\event\\discussion_viewed",
                    "userid": "21",
                    "origin": "web",
                    "ip": "0:0:0:0:0:0:0:1",
                    "contextid": 47,
                    "anonymous": 0,
                    "edulevel": 2,
                    "objecttable": "forum_discussions",
                    "other": "N;",
                    "target": "discussion",
                    "relateduserid": None,
                    "contextlevel": 70,
                    "action": "viewed",
                    "courseid": course,
                    "objectid": "1",
                    "timecreated": 1536229245,
                    "component": "mod_forum",
                    "crud": "r",
                    "contextinstanceid": "4"
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
                                    "cacherev": "1536148778",
                                    "showreports": "0",
                                    "groupmode": "0",
                                    "idnumber": "",
                                    "completionnotify": "0",
                                    "summary": "<p>hello to ikarion moodle<br></p>",
                                    "shortname": "ikarion",
                                    "maxbytes": "0",
                                    "theme": "",
                                    "enddate": "0",
                                    "groupmodeforce": "0",
                                    "newsitems": "3",
                                    "legacyfiles": "0",
                                    "lang": "",
                                    "requested": "0",
                                    "url": "http://localhost/ikarion_moodle",
                                    "sortorder": "1",
                                    "startdate": "0",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1533818889",
                                    "format": "site",
                                    "calendartype": "",
                                    "showgrades": "1",
                                    "marker": "0",
                                    "fullname": "ikarion_moodle",
                                    "type": "site",
                                    "id": 1,
                                    "timecreated": "1533818161",
                                    "summaryformat": "0",
                                    "category": "0",
                                    "enablecompletion": "0",
                                    "defaultgroupingid": "0"
                                }
                            },
                            "description": {
                                "en": "hello to ikarion moodle"
                            },
                            "name": {
                                "en": "ikarion_moodle"
                            },
                            "type": "http://id.tincanapi.com/activitytype/site"
                        },
                        "id": "http://localhost/ikarion_moodle",
                        "objectType": "Activity"
                    },
                    {
                        "definition": {
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_course": {
                                    "cacherev": "1536148778",
                                    "showreports": "0",
                                    "groupmode": "0",
                                    "idnumber": "",
                                    "completionnotify": "0",
                                    "summary": "<p>bla blub<br></p>",
                                    "shortname": "gen_test",
                                    "maxbytes": "0",
                                    "theme": "",
                                    "enddate": "0",
                                    "groupmodeforce": "0",
                                    "newsitems": "0",
                                    "legacyfiles": "0",
                                    "lang": "",
                                    "requested": "0",
                                    "url": "http://localhost/ikarion_moodle/course/view.php?id={}".format(course),
                                    "sortorder": "10001",
                                    "startdate": "1534111200",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1534169038",
                                    "format": "topics",
                                    "calendartype": "",
                                    "showgrades": "1",
                                    "marker": "0",
                                    "fullname": "generated_test_course",
                                    "type": "course",
                                    "id": "3",
                                    "timecreated": "1534169038",
                                    "summaryformat": "0",
                                    "category": "1",
                                    "enablecompletion": "0",
                                    "defaultgroupingid": "0"
                                }
                            },
                            "description": {
                                "en": "bla blub"
                            },
                            "name": {
                                "en": "generated_test_course"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/course"
                        },
                        "id": "http://localhost/ikarion_moodle/course/view.php?id={}".format(course),
                        "objectType": "Activity"
                    },
                    {
                        "definition": {
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_module": {
                                    "introformat": "1",
                                    "displaywordcount": "0",
                                    "assessed": "0",
                                    "assesstimefinish": "0",
                                    "maxbytes": "512000",
                                    "lockdiscussionafter": "0",
                                    "scale": "100",
                                    "name": "testforum",
                                    "rsstype": "0",
                                    "completionreplies": "0",
                                    "intro": "<p>blablabalbl<br></p>",
                                    "maxattachments": "9",
                                    "blockperiod": "0",
                                    "blockafter": "0",
                                    "url": "http://localhost/ikarion_moodle/mod/forum/view.php?id=4",
                                    "rssarticles": "0",
                                    "completiondiscussions": "0",
                                    "trackingtype": "1",
                                    "assesstimestart": "0",
                                    "timemodified": "1535723483",
                                    "warnafter": "0",
                                    "completionposts": "0",
                                    "type": "forum",
                                    "course": "3",
                                    "id": "2",
                                    "forcesubscribe": "0"
                                }
                            },
                            "description": {
                                "en": "<p>blablabalbl<br></p>"
                            },
                            "name": {
                                "en": "testforum"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/forum"
                        },
                        "id": "http://localhost/ikarion_moodle/mod/forum/view.php?id=4",
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
                "homePage": "http://localhost/ikarion_moodle",
                "name": "21"
            },
            "name": user,
            "objectType": "Agent"
        },
        "timestamp": time,
        "version": "1.0.0",
        "id": "c734d8a5-3c15-48d3-97d7-e6b1597f4753",
        "verb": {
            "display": {
                "en": "viewed"
            },
            "id": verb
        },
        "object": {
            "definition": {
                "extensions": {
                    "http://lrs.learninglocker.net/define/extensions/moodle_discussion": {
                        "forum": "2",
                        "assessed": "0",
                        "userid": "19",
                        "name": "testsubject_context",
                        "timeend": "0",
                        "url": "http://localhost/ikarion_moodle/mod/forum/discuss.php?d=1",
                        "firstpost": "1",
                        "usermodified": "21",
                        "timestart": "0",
                        "timemodified": "1536229244",
                        "pinned": "0",
                        "type": "forum_discussions",
                        "groupid": "-1",
                        "course": "3",
                        "id": "1"
                    }
                },
                "description": {
                    "en": "A Moodle discussion."
                },
                "name": {
                    "en": "testsubject_context"
                },
                "type": "http://id.tincanapi.com/activitytype/forum-topic"
            },
            "id": artefact,
            "objectType": "Activity"
        }
    }
    if process:
        sp.process_statement(statement)
    return statement


def generate_xapi_statement3(*, user, course, time, verb, artefact, group=None, process=True):
    statement = {
        "authority": {
            "objectType": "Agent",
            "name": "New Client",
            "mbox": "mailto:hello@learninglocker.net"
        },
        "stored": "2019-02-18T08:47:46.111Z",
        "context": {
            "extensions": {
                "http://collide.info/extensions/group": {
                    group: {
                        "group_members": [
                            {
                                "name": "nlrrOSj7CO4Pk21IIcDnog==",
                                "fullname": "1KgfBuaHozTVQrBTRvWP4Q==",
                                "email": "/nIg1zgiveWGp+RDMAwtvQ==",
                                "username": "n8BzisYpc/UDLu7B8Mkbaw=="
                            },
                            {
                                "name": "tLbffKo5+/MJtqFFCnIWEg==",
                                "fullname": "enE6kWpAN3/yrrtAsBAaSg==",
                                "email": "Wro71ckSGFsrQJLxxWAWTA==",
                                "username": "iFtPkItpO9yq2DeDyGZ28A=="
                            },
                            {
                                "name": "wdqshw4nFEYjiBA+UokJ5w==",
                                "fullname": "fueZPE9k8NiCAVLYXgaR/A==",
                                "email": "yyWen1z/5ULLRnyUavzoDA==",
                                "username": "zXytLGVx49tOZ8sIlRsJXw=="
                            },
                            {
                                "name": "EA12iYsCduiMrz+xSdFQjQ==",
                                "fullname": "wDzP6tmGLzWycKKwOr3WrA==",
                                "email": "DTZXo6TQk++n08GnsWFLTg==",
                                "username": "t9KB3PX9sr3tMcNTUFq/9g=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1210",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1211"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1550651700",
                            "task_start": "1550478900",
                            "task_name": "EM_T1",
                            "task_id": "66"
                        },
                        "timemodified": "1550479289",
                        "timecreated": "1550479289",
                        "description": "none",
                        "name": "EM_1",
                        "id": group
                    }
                },
                "http://lrs.learninglocker.net/define/extensions/info": {
                    "https://moodle.org/": "3.2.3+ (Build: 20170509)"
                },
                "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log": {
                    "realuserid": "dTuHTrIhox5BeFGLlQ9snQ==",
                    "eventname": "\\core\\event\\course_viewed",
                    "userid": "nlrrOSj7CO4Pk21IIcDnog==",
                    "origin": "web",
                    "ip": "134.91.34.179",
                    "contextid": 2295,
                    "anonymous": 0,
                    "edulevel": 2,
                    "objecttable": None,
                    "other": "N;",
                    "target": "course",
                    "relateduserid": None,
                    "contextlevel": 50,
                    "action": "viewed",
                    "courseid": course,
                    "objectid": None,
                    "timecreated": 1550479665,
                    "component": "core",
                    "crud": "r",
                    "contextinstanceid": "18"
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
                                    "cacherev": "1550247141",
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
                                    "timemodified": "1524571833",
                                    "format": "site",
                                    "calendartype": "",
                                    "showgrades": "1",
                                    "marker": "0",
                                    "fullname": "IKARion Projekt",
                                    "type": "site",
                                    "id": course,
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
                    },
                    {
                        "objectType": "Activity",
                        "id": "https://moodle.ikarion-projekt.de/course/view.php?id=11",
                        "definition": {
                            "type": "http://lrs.learninglocker.net/define/type/moodle/course",
                            "name": {
                                "en": "Super Awesome Course {}".format(course)
                            },
                            "description": {
                                "en": "Inhalte\r\nWie verändert sich die Kommunikation, wenn statt face-to-face mit anderen\r\nMenschen computerbasiert, z. B. über das Internet, kommuniziert wird? Welchen\r\nEinfluss hat dies auf das Lernen und Lehren? Im Rahmen der Veranstaltung werden\r\nzunächst klassische Theorien der computervermittelten Kommunikation besprochen,\r\num ein Verständnis der durch die Medienvermittlung auftretenden Veränderungen\r\nzu erreichen. Dann werden die Erkenntnisse spezifischer auf den Bereich des\r\nLehrens und Lernens angewandt und u. a. im Kontext von Web 2.0 Plattformen wie\r\nz. B. Wikis diskutiert, die das Lernen unterstützen können.\r\n\r\nNutzungsbedingungen\r\nIn diesem reinen\r\nOnline-Kurs gibt es keine fixen\r\nPräsenzzeiten. Die aktive ortsunabhängige Mitarbeit wird stattdessen über ein eigens\r\neingerichtetes Moodle-Konto ablaufen. Darüber müssen innerhalb festgelegter Zeiträume\r\nArbeiten geleistet werden, um im Anschluss eine Prüfungsleistung erbringen und Credit Points (CP) erhalten zu können. \r\n\r\nDie aktive\r\nPartizipation und Auseinandersetzung mit den Inhalten und (Gruppen-)Übungen\r\ninnerhalb des Moodles ist dementsprechend die Voraussetzung, um eine Prüfungsleistung erbringen zu können.Im Namen der Wissenschaft - du gestaltest die Online-Kurse der Zukunft mit. Wie? Indem du ein Häkchen setzt, d.h. dich bereit erklärst an der Begleitforschung zu diesem Kurs teilzunehmen, und uns gelegentlich deine Meinung sagst.\r\n\r\nBitte beachte: zur Prüfungsleistung bist du innerhalb des Onlinekurses mit deinem richtigen Namen identifizierbar.\r\n\r\n\r\n\r\nViel Erfolg und gutes Gelingen!\r\n\r\nSebastian Strauß\r\nFilipa Stoyanova\r\n"
                            },
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_course": {
                                    "cacherev": "1552995989",
                                    "showreports": "0",
                                    "groupmode": "1",
                                    "idnumber": "",
                                    "completionnotify": "0",
                                    "summary": "<p><b>Inhalte</b><br>\r\nWie verändert sich die Kommunikation, wenn statt face-to-face mit anderen\r\nMenschen computerbasiert, z. B. über das Internet, kommuniziert wird? Welchen\r\nEinfluss hat dies auf das Lernen und Lehren? Im Rahmen der Veranstaltung werden\r\nzunächst klassische Theorien der computervermittelten Kommunikation besprochen,\r\num ein Verständnis der durch die Medienvermittlung auftretenden Veränderungen\r\nzu erreichen. Dann werden die Erkenntnisse spezifischer auf den Bereich des\r\nLehrens und Lernens angewandt und u. a. im Kontext von Web 2.0 Plattformen wie\r\nz. B. Wikis diskutiert, die das Lernen unterstützen können.</p>\r\n\r\n<p><b>Nutzungsbedingungen</b><br>\r\n</p><p>In diesem<span lang=\"DE\"> reinen\r\nOnline-Kurs gibt es <b>keine fixen\r\nPräsenzzeiten</b>. Die aktive <b>ortsunabhängige</b> Mitarbeit wird stattdessen über ein eigens\r\neingerichtetes Moodle-Konto ablaufen. Darüber müssen innerhalb festgelegter Zeiträume\r\nArbeiten geleistet werden, um im Anschluss eine Prüfungsleistung erbringen und Credit Points (CP) erhalten zu können. <br></span></p><p><span lang=\"DE\"></span>\r\n\r\n<span lang=\"DE\">Die <b>aktive\r\nPartizipation und Auseinandersetzung</b> mit den Inhalten und (Gruppen-)Übungen\r\ninnerhalb des Moodles ist dementsprechend die Voraussetzung, um eine Prüfungsleistung erbringen zu können.</span></p><p><span lang=\"DE\"><b>Im Namen der Wissenschaft</b> - du gestaltest die Online-Kurse der Zukunft mit. Wie? Indem du ein Häkchen setzt, d.h. dich bereit erklärst an der <a href=\"https://moodle.ikarion-projekt.de/pluginfile.php/1340/mod_label/intro/Begleitforschung%20Details%20%281%29.pdf\"><b>Begleitforschung</b></a> zu diesem Kurs teilzunehmen, und uns gelegentlich <span lang=\"DE\"></span>deine Meinung sagst.<br></span></p><p>\r\n\r\n</p><span lang=\"DE\"></span><p></p><p><b>Bitte beachte: zur Prüfungsleistung bist du innerhalb des Onlinekurses mit deinem richtigen Namen identifizierbar.</b><br>\r\n<!--[if !supportLineBreakNewLine]--><br>\r\n<!--[endif]--></p>\r\n\r\n<p>Viel Erfolg und gutes Gelingen!<br>\r\n<br>\r\nSebastian Strauß<br>\r\nFilipa Stoyanova<br>\r\n<!--[endif]--></p>",
                                    "shortname": "CvK WS 2018/2019",
                                    "maxbytes": "0",
                                    "theme": "",
                                    "enddate": "1553986800",
                                    "groupmodeforce": "0",
                                    "newsitems": "5",
                                    "legacyfiles": "0",
                                    "lang": "",
                                    "requested": "0",
                                    "url": "https://moodle.ikarion-projekt.de/course/view.php?id=11",
                                    "sortorder": "10008",
                                    "startdate": "1538949600",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1539075016",
                                    "format": "topics",
                                    "calendartype": "",
                                    "showgrades": "1",
                                    "marker": "11",
                                    "fullname": "Psychologische Grundlagen computervermittelter Kommunikation: Lernen und Lehren",
                                    "type": "course",
                                    "id": "11",
                                    "timecreated": "1531922700",
                                    "summaryformat": "1",
                                    "category": "1",
                                    "enablecompletion": "1",
                                    "defaultgroupingid": "0"
                                }
                            }
                        }
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
                "name": user
            },
            "name": user,
            "objectType": "Agent"
        },
        "timestamp": time,
        "version": "1.0.0",
        "id": "45a0477a-9e94-4732-9b5c-39efb320dfea",
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
                        "cacherev": "1550479640",
                        "showreports": "0",
                        "groupmode": "1",
                        "idnumber": "",
                        "completionnotify": "0",
                        "summary": "",
                        "shortname": "k_k",
                        "maxbytes": "0",
                        "theme": "",
                        "enddate": "1571349600",
                        "groupmodeforce": "0",
                        "newsitems": "5",
                        "legacyfiles": "0",
                        "lang": "",
                        "requested": "0",
                        "url": "https://moodle.ikarion-projekt.de/course/view.php?id=18",
                        "sortorder": "10001",
                        "startdate": "1539813600",
                        "visible": "1",
                        "visibleold": "1",
                        "timemodified": "1550479639",
                        "format": "topics",
                        "calendartype": "",
                        "showgrades": "1",
                        "marker": "0",
                        "fullname": "K",
                        "type": "course",
                        "id": "18",
                        "timecreated": "1539764877",
                        "summaryformat": "1",
                        "category": "1",
                        "enablecompletion": "1",
                        "defaultgroupingid": "0"
                    }
                },
                "description": {
                    "en": "A Moodle course"
                },
                "name": {
                    "en": "K"
                },
                "type": 'http://id.tincanapi.com/activitytype/forum-topic',
            },
            "id": artefact,
            "objectType": "Activity"
        }
    }

    if process:
        sp.process_statement(statement)
    # json_s = json.dumps(statement)
    # json_s.replace("forum", "blabla")
    # statement = json.loads(json_s)

    return statement


generate_xapi_statement2 = generate_xapi_statement3




def generate_xapi_self_assessment_statement(*, user, course, time, verb, artefact, group=None, process=True):
    course_full = "https://moodle.ikarion-projekt.de/course/view.php?id={}".format(course)
    statement = {
        "authority": {
            "objectType": "Agent",
            "name": "New Client",
            "mbox": "mailto:hello@learninglocker.net"
        },
        "stored": "2019-02-18T08:47:46.111Z",
        "context": {
            "extensions": {
                "http://collide.info/extensions/group": {
                    group: {
                        "group_members": [
                            {
                                "name": "nlrrOSj7CO4Pk21IIcDnog==",
                                "fullname": "1KgfBuaHozTVQrBTRvWP4Q==",
                                "email": "/nIg1zgiveWGp+RDMAwtvQ==",
                                "username": "n8BzisYpc/UDLu7B8Mkbaw=="
                            },
                            {
                                "name": "tLbffKo5+/MJtqFFCnIWEg==",
                                "fullname": "enE6kWpAN3/yrrtAsBAaSg==",
                                "email": "Wro71ckSGFsrQJLxxWAWTA==",
                                "username": "iFtPkItpO9yq2DeDyGZ28A=="
                            },
                            {
                                "name": "wdqshw4nFEYjiBA+UokJ5w==",
                                "fullname": "fueZPE9k8NiCAVLYXgaR/A==",
                                "email": "yyWen1z/5ULLRnyUavzoDA==",
                                "username": "zXytLGVx49tOZ8sIlRsJXw=="
                            },
                            {
                                "name": "EA12iYsCduiMrz+xSdFQjQ==",
                                "fullname": "wDzP6tmGLzWycKKwOr3WrA==",
                                "email": "DTZXo6TQk++n08GnsWFLTg==",
                                "username": "t9KB3PX9sr3tMcNTUFq/9g=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1210",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1211"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1550651700",
                            "task_start": "1550478900",
                            "task_name": "EM_T1",
                            "task_id": "66"
                        },
                        "timemodified": "1550479289",
                        "timecreated": "1550479289",
                        "description": "none",
                        "name": "EM_1",
                        "id": group
                    }
                },
                "http://lrs.learninglocker.net/define/extensions/info": {
                    "https://moodle.org/": "3.2.3+ (Build: 20170509)"
                },
                "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log": {
                    "realuserid": "dTuHTrIhox5BeFGLlQ9snQ==",
                    "eventname": "\\core\\event\\course_viewed",
                    "userid": "nlrrOSj7CO4Pk21IIcDnog==",
                    "origin": "web",
                    "ip": "134.91.34.179",
                    "contextid": 2295,
                    "anonymous": 0,
                    "edulevel": 2,
                    "objecttable": None,
                    "other": "N;",
                    "target": "course",
                    "relateduserid": None,
                    "contextlevel": 50,
                    "action": "viewed",
                    "courseid": course,
                    "objectid": None,
                    "timecreated": 1550479665,
                    "component": "core",
                    "crud": "r",
                    "contextinstanceid": "18"
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
                                    "cacherev": "1550247141",
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
                                    "url": course_full,
                                    "sortorder": "1",
                                    "startdate": "0",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1524571833",
                                    "format": "site",
                                    "calendartype": "",
                                    "showgrades": "1",
                                    "marker": "0",
                                    "fullname": "IKARion Projekt",
                                    "type": "site",
                                    "id": course,
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
                "name": user
            },
            "name": user,
            "objectType": "Agent"
        },
        "timestamp": time,
        "version": "1.0.0",
        "id": "45a0477a-9e94-4732-9b5c-39efb320dfea",
        "verb": {
            "display": {
                "en": "viewed"
            },
            "id": verb
        },
        "object": {
            "id": artefact,
            "definition": {
                "type": "https://moodle.ikarion-projekt.de/define/type/moodle/block_groupactivity",
                "name": {
                    "en": "Groupactivity self assessment"
                },
                "description": {
                    "en": "Groupactivity self assessment completed"
                },
                "extensions": {
                    "http://lrs.learninglocker.net/define/extensions/moodle_block": {
                        "component": "block_groupactivity",
                        "contextinstanceid": "573",
                        "items": [
                            {
                                "id": "7",
                                "value": "0"
                            },
                            {
                                "id": "8",
                                "value": "3"
                            },
                            {
                                "id": "9",
                                "value": "2"
                            }
                        ]
                    }
                }
            }
        }
    }

    if process:
        sp.process_statement(statement)

    return statement
