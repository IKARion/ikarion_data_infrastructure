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


def generate_xapi_statement_wiki_mod(*, user, user_i, statement_i, course, time, verb, artefact, group=None,
                                     process=True):
    task_name = "Test_Wiki_Bla"
    course_full = "https://moodle.ikarion-projekt.de/course/view.php?id={}".format(course)
    content_clean = "Inhaltsübersicht1. Hinweise zur gemeinsamen Arbeit im Wiki [Bearbeiten]2. Frage 1 & 2 - Kognitive Entwicklung nach Piaget "
    content_clean_user = content_clean * (user_i + 1) ** 2
    statement = {
        "authority": {
            "objectType": "Agent",
            "name": "New Client",
            "mbox": "mailto:hello@learninglocker.net"
        },
        "stored": "2019-03-12T13:21:38.227Z",
        "context": {
            "extensions": {
                "http://collide.info/extensions/group": {
                    "311": {
                        "group_members": [
                            {
                                "name": "YAjW/wX68/Gmk+QtjpzCWg==",
                                "fullname": "cP4ZrroHA4OC7OLBPO1IChBPE9plkknnLOnqpKcD86g=",
                                "email": "P43D/ObyLlfj6bIYlyXXhvhBJiQDx4r8UWsWony3QincX/tdU/qtECWyvsksHioj",
                                "username": "+wRs4ylcVy2CaGbnAMs4NA=="
                            },
                            {
                                "name": "GA32Uf83DXlTfuu1FSeMFg==",
                                "fullname": "rJkxGM9yVOIpAjVoXJ1ZhA==",
                                "email": "1HGFKeWcPwguIY/Gbs23w9xf+11T+q0QJbK+ySweKiM=",
                                "username": "aROGBNUR1kyIIlRppuoF7w=="
                            },
                            {
                                "name": "1w21eIbpkSXstgIbXjb5MQ==",
                                "fullname": "lfy4EcVwvwQ5U5MODdRx/hBPE9plkknnLOnqpKcD86g=",
                                "email": "DD942q+B5EQJzH9XbE8GWApV/gzOdER6YUQhgms4zWw=",
                                "username": "kAGQl/YDZZJ/TagPxQmkaQ=="
                            },
                            {
                                "name": "h0sSOJhMJsrbKuSRR3qlsA==",
                                "fullname": "Nia47n6HXjJRb+KHo4yKWQ==",
                                "email": "v7a1dQ33BJ96n5Rl1gLsowta1hfiAs+An/K03OI8+Gc=",
                                "username": "WP/hHPNTh0zJeTwtDwQRUQ=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1228",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1229"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1551654300",
                            "task_start": "1551092400",
                            "task_name": "Woche 1 Mirroring",
                            "task_id": "71"
                        },
                        "timemodified": "1550828859",
                        "timecreated": "1550828859",
                        "description": "none",
                        "name": "W1Gruppe-1",
                        "id": "311"
                    },
                    group: {
                        "group_members": [
                            {
                                "name": "YAjW/wX68/Gmk+QtjpzCWg==",
                                "fullname": "cP4ZrroHA4OC7OLBPO1IChBPE9plkknnLOnqpKcD86g=",
                                "email": "P43D/ObyLlfj6bIYlyXXhvhBJiQDx4r8UWsWony3QincX/tdU/qtECWyvsksHioj",
                                "username": "+wRs4ylcVy2CaGbnAMs4NA=="
                            },
                            {
                                "name": "oxP3yJF/mny+oup/jprHJA==",
                                "fullname": "u4KufSmYeAF6O/EoY8OSlA==",
                                "email": "Uzw5Tt5eRMx503wEsCAy760fSrEyVN1nAKbVT1zoSjM=",
                                "username": "rxaXTX6920qtC2UwOhLhZw=="
                            },
                            {
                                "name": "h0sSOJhMJsrbKuSRR3qlsA==",
                                "fullname": "Nia47n6HXjJRb+KHo4yKWQ==",
                                "email": "v7a1dQ33BJ96n5Rl1gLsowta1hfiAs+An/K03OI8+Gc=",
                                "username": "WP/hHPNTh0zJeTwtDwQRUQ=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1202",
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1261"
                            ],
                            "task_type": "Test_Wiki_Le",
                            "task_end": "1552259100",
                            "task_start": "1551697200",
                            "task_name": task_name,
                            "task_id": "78"
                        },
                        "timemodified": "1551690322",
                        "timecreated": "1551690322",
                        "description": "none",
                        "name": "W2 Gruppe-1",
                        "id": group
                    }
                },
                "http://lrs.learninglocker.net/define/extensions/info": {
                    "https://moodle.org/": "3.2.3+ (Build: 20170509)"
                },
                "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log": {
                    "realuserid": None,
                    "eventname": "\\mod_wiki\\event\\page_updated",
                    "userid": "h0sSOJhMJsrbKuSRR3qlsA==",
                    "origin": "web",
                    "ip": "178.8.234.87",
                    "contextid": "2647",
                    "anonymous": "0",
                    "edulevel": "2",
                    "objecttable": "wiki_pages",
                    "other": "a:1:{s:10:\"newcontent\";s:14932:\"<h3><span xml:lang=\"de\" lang=\"de\">Hinweise zur gemeinsamen Arbeit im Wiki</span></h3>\n\n<p align=\"justify\">Bitte beachten Sie folgende Hinweise zur gemeinsamen Arbeit mit Wiki.<br>\nWikis sind asynchron, es kann also nur unter bestimmten Umständen gleichzeitig daran gearbeitet werden. Um zu vermeiden, dass eine parallele Bearbeitung der Wikis gestört wird, achten Sie bitte dringend darauf, dass Sie die einzelnen Wikis <u>nicht auf der obersten Ebene bearbeiten</u> (s. oben: Anzeige –Bearbeiten – Kommentare usw.), sondern in den einzelnen Kapiteln (siehe [Bearbeiten] rechts neben den Kapiteln).</p>\n\n<p align=\"justify\">Zur Information: Die Überschriften der Wikis (z.B. Frage 1 – Kognitive Entwicklung nach Piaget) wurden von uns als „Überschrift groß“ formatiert.\nBitte ändern Sie diese Überschrift nicht. Der Fließtext für die Fragen (z.B. Fragetext für die erste Frage: „…“) wurde als „Absatz“ formatiert.</p>\n\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p>\n\n<h3><span xml:lang=\"de\" lang=\"de\">Frage 1 &amp; 2 - Kognitive Entwicklung nach Piaget</span></h3>_________________________________________________________<p></p>\n\n<p align=\"justify\"><i>Welche der folgenden Aussagen <u>treffen zu</u> und welche <u>treffen nicht zu</u>?</i></p>\n\n<p><b><span xml:lang=\"de\" lang=\"de\">1.</span></b></p><p align=\"justify\"> Die nächste Aufgabe der Mathearbeit sieht wirklich schwierig aus. Gar nicht so, wie die anderen Aufgaben, die sie im Unterricht geübt haben! Lars probiert eine Weile an der Aufgabe herum. Kurz darauf merkt er, dass er diese Aufgabe doch mit der Lösung aus dem Unterricht lösen kann. Er fragt sich, wie er das nur übersehen könnte. Die Aufgabe kann Lars zügig lösen.</p>\n\n<p><span xml:lang=\"de\" lang=\"de\">Diese Situation zeigt das Fehlschlagen der Assimilation.</span></p>\n\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p>\n\n<p><b><span xml:lang=\"de\" lang=\"de\">2.</span></b></p>\n<p align=\"justify\"> Herr M. war bereits in vielen teuren Restaurants.\nZum ersten Mal besucht er nun ein McBurger. Wie gewohnt setzt er sich auf einen der freien Plätze und wartet darauf, dass die Bedienung die Speisekarte bringt. Er wartet vergeblich - es kommt keine Bedienung an den Tisch. Als Antwort auf einen verwirrten Blick und den Ruf der Bedienung kommt vom Tresen: \"Wir bedienen Sie nicht am Tisch. Kommen Sie her.\"</p>\n\n<p><span xml:lang=\"de\" lang=\"de\">Die Erfahrung führt zu einer Akkomodation.</span></p>\n\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p><p>Unter <b>Assimilation</b> versteht man, dass die Umwelt anhand schon vorhandener Denkmuster interpretiert und erfasst wird. Bekannt dazu ist das wau-wau Schemata; ein kleines Kind nennt einen Hund wau-wau. Nun sieht es eine Katze, die ebenso wie der Hund, Fell besitzt, einen Schwanz hat, auf vier Beinen läuft, und nennt jene Katze auch wau-wau.</p><p>Ein&nbsp;<b>Fehlschlagen der Assimilation</b>&nbsp;bedeutet, dass neu erfahrene Vorkommnisse in der Umwelt nicht den eigenen Denkstrukturen zugeordnet werden können. In dem Fallbeispiel scheitert Lars zwar im ersten Moment daran, jedoch benötigt er nur einige Zeit bis die Assimilation stattfindet, und ähnliche Matheaufgaben ins Gedächtnis gerufen werden.<br></p><p><b>Akkomodation</b> beschreibt nun den Prozess, dass das eigene Denkmuster der Umwelt angepasst wird. Das heißt, in diesem Fall z.B. lernt das Kind, dass die Katze zwar ähnliche Eigenschaften wie der Hund (wauwau) besitzt, jedoch ein anderen Tiergattung angehört. Sie macht nicht wauwau, sie miaut.</p><p>In dem Fallbeispiel findet eine Akkomodation statt, indem Herr M. herausfindet, dass die Bedienung in jenem Restaurant anders gehandhabt wird, als in ihm schon bekannten Restaurants.</p><p><span xml:lang=\"de\" lang=\"de\"><br></span></p><h3><span xml:lang=\"de\" lang=\"de\">Frage 3 - Kognitive Entwicklung nach Wygotski</span></h3>_________________________________________________________<p></p>\n\n<p><i><span xml:lang=\"de\" lang=\"de\">Trifft die Aussage zu</span></i><span xml:lang=\"de\" lang=\"de\">?</span></p>\n\n<p align=\"justify\">Mithilfe einer Lern-App schafft es Markus, sich Spanisch beizubringen und in einem Kurs die Sprachstufe A1/A2 zertifiziert zu bekommen. </p>\n\n<p align=\"justify\">Die Lern-App war demnach ein Werkzeug, welches Markus dabei unterstützt hat, in die Zone der proximalen Entwicklung zu kommen.</p>\n\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p>\n\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p><h3><span lang=\"de\" lang=\"de\" xml:lang=\"de\">Frage 4 - Wissensarten</span></h3>_________________________________________________________<p></p>\r\n\r\n<p align=\"justify\"><i>Bitte ordnen Sie jede der folgenden drei Szenen\r\njeweils einer Wissensart zu. Jede Wissensart wird genau einmal benötigt.\r\nBeachten Sie, dass nicht alle der aufgeführten Wissensarten benötigt werden.</i></p><i>\r\n\r\n</i><p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">1.</span></b></p><p align=\"justify\"> Ein fünfjähriges Mädchen bekommt von seiner Großmutter ein Fahrrad geschenkt. Als die Großmutter nach einiger Zeit zu Besuch kommt, fährt das Mädchen ihr im Garten auf dem Fahrrad entgegen und ruft: „Schau, ich kann schon Rad fahren.“</p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\r\n\r\n<p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">2.</span></b></p><p align=\"justify\"> Nina hat ihre Hausarbeit bereits zu lange aufgeschoben. Heute muss sie wirklich anfangen. Aber in der WG ist es einfach immer zu laut. Daher entscheidet sie sich dazu, zur Uni zu fahren und die Hausarbeit in der Bibliothek zu schreiben.</p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\r\n\r\n<p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">3.</span></b></p><p align=\"justify\"> In der Nachhilfestunde soll Max eine Aufgabe lösen, die der Lehrer im Unterricht vorgestellt hat. Bevor Max jedoch die Aufgabe löst, soll er erklären, warum die Formel zur Lösung eingesetzt wird.</p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\r\n\r\n<p><b></b></p><p align=\"justify\"><b>Prozedurales Wissen - Selbstregulationswissen - Konzeptuelles Wissen - Situationales Wissen</b></p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">_________________________________________________________<br>\r\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Prozedurales Wissen</b>, auch Handlungswissen genannt beschreibt, dass Handlungen und/oder auch Lösungsstrategien sich anhand schon erfahrener Strategien und vollendeten Handlungen orientieren. D.h. man führt eine Handlung nach schon bekanntem Prozedere aus ?</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Selbstregulationswissen</b> beschreibt den regulierten Vorgang seine eigenen Empfindungen, und Emotionen zu bändigen, bzw. der Situation anzupassen. Eventuell auch eigene Lernstrategien zu überdenken, und zu reflektieren. Im Fallbeispiel 2 kann man so eventuell von Selbstregulationswissen sprechen, da Nina sich dessen bewusst ist, wie sie ihre Aufmerksamkeit am besten auf die Fertigstellung ihrer Hausarbeit lenkt.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Konzeptuelles Wissen </b>beschreibt hierbei, dass Wissen anhand von Konzepten, eventuell Formeln, Kategorien, und Oberbegriffen gebündelt und angewandt wird. Im Fallbeispiel 3 kann man von konzeptuellen Wissen sprechen, da Max seine Matheaufgabe nach ihm schon bekannten (und auch allgemeinen) Lösungswegen (einem Konzept) löst.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Situationales Wissen</b> beschreibt Wissen, das innerhalb einer sozialen Situation erworben, angewandt, und/oder gefestigt wird. Das kann durch soziale Interaktion und Kommunikation an sich passieren. Dabei kann ebenso die Motivation aus dem sozialen Umfeld, als auch Hilfestellung, Unterstützung und soziale Anerkennung dazu beitragen. Im ersten Fallbeispiel kann man somit von situationalem Wissen sprechen, da die Kleine Fahrrad fahren lernt, während ihre Großmutter ihr dabei über die Schultern schaut, und ihr Anerkennung dafür zeigt.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">1) Bei diesem Fall handelt es sich um das situationale Wissen. Das situationale Wissen beschreibt das Wissen über Anforderungen und Merkmale von Problemen in bestimmten Situationen. Anhand dieses Wissens kann anschließend die Aufmerksamkeit auf die Aspekte gelenkt werden, die relevant für die Problemlösung sind. Dabei wird oft auf Erfahrungen oder Erinnerungen zurückgegriffen. Wenn dem Individuum noch keine Lösung für die Situation bekannt ist, greift es oft auf ähnliche Situationen mittels seiner Erinnerung zurück, und nutzt die Problemlösung der damaligen Situation für die der jetzigen.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">2) Bei diesem Fall handelt es sich um das Selbstregulationswissen. Beim Selbstregulationswissen ergreift der/die Lernende Selbststeuerungsmaßnahmen und überwacht somit selbstständig seinen Lernprozess. Da Nina in der vorliegenden Situation eigenständig die Entscheidung trifft zur Uni zu fahren und somit über ihren Lernprozess bestimmt, kann man hier von Selbstregulationswissen sprechen.&nbsp;</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">3) Bei diesem Fall kann man vom konzeptuellem Wissen sprechen. Das konzeptuelle Wissen wird auch als \"semantisches Wissen\" bezeichnet und bezeichnet das Wissen über Fakten, Begriffe, Schemata und Prinzipien. Das konzeptuelle Wissen ermöglicht dem Individuum Beziehungen zwischen dem bereits vorhandenen und dem neuen Wissen herzustellen. In der vorliegenden Situation soll Max auf sein Wissen über ein bestimmtes Schemata (die Formel) zurückgreifen. Unteranderem stellt er mit der Erklärung, warum die Formel benötigt wird, eine Beziehung zwischen der Formel (vorhandenes Wissen) und der Lösung der Aufgabe (neues Wissen) her.&nbsp;</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><br></span></p><h3><span xml:lang=\"de\" lang=\"de\">Frage 5 - Konstruktivismus &amp; Situiertes Lernen</span></h3>_________________________________________________________<p></p><p align=\"justify\"><i>Lesen Sie die folgende Kursbeschreibung und entscheiden Sie, welche der aufgeführten Gestaltungsmerkmalen verschiedener situierter Lernarrangements in diesem Kurs vorhanden sind.</i></p>\n\n<p align=\"justify\">SchülerInnen nehmen an einem Workshop teil, in dem das Konzept „Graphentheorien“ (Informatik) vermittelt werden soll. Dieser findet in einem außerschulischen Lernlabor statt.</p>\n\n<p align=\"justify\">Die Teilnehmenden des Workshops sollen die Organisatoren eines Jahrmarkts – einen Juristen, einen Schatzmeister und einen Magier – bei der Planung des Jahrmarkts unterstützen. Jeder der Organisatoren ist für einen bestimmten Bereich der Planung verantwortlich. Aufgabe für die Teilnehmenden ist es, die Organisation des Jahrmarkts als ExpertInnen zu unterstützen, indem sie deren spezifischen Probleme lösen. Diese Geschichte wird in einem animierten Film\npräsentiert.</p>\n\n<p align=\"justify\">Die Teilnehmenden werden auf drei Gruppen aufgeteilt, die jeweils einem Betreuer, der einen Organisator spielt, zugeteilt sind. Die Teilnehmenden sollen die Aufgabe jeweils in ihrer Gruppe lösen und sich dort gegenseitig bei der Arbeit unterstützen, laut denken, wie sie gerade vorgehen.</p>\n\n<p align=\"justify\">Eine Gruppe steht beispielsweise vor dem Problem, dass innerhalb der Geisterbahn alle Attraktionen mit Kabeln verbunden werden, wobei zur Einsparung von Geld möglichst wenig Kabel-Material verwendet werden sollen. Dieses Problem lässt sich mit <b>Algorithmen zur Suche des minimalen Spannbaums</b> lösen. Die Organisatoren geben jedoch<b> nur wenig Unterstützung</b> bei der Bearbeitung der Probleme, da etwa ein Jurist nicht mit Prinzipien der Informatik vertraut ist. Zur Unterstützung sind allerdings <i>in einem Kiosk verschiedene relevante und nicht relevante Zeitschriften ausgelegt</i>, die mögliche Lösungsansätze für die verschiedenen Probleme der Szenarien schülergerecht vorstellen. Zusätzlich dienen die Zeitschriften dazu, einen <b>Alltagsbezug der verwendeten informatischen Strategien vorzustellen</b>.</p>\n\n<p align=\"justify\">Haben die Teilnehmenden die Planung erfolgreich abgeschlossen, wird ihnen ein Abschlussfilm vorgespielt, der das erfolgreiche Stadtfest zeigt.</p>\n\n<p><b></b></p><p align=\"justify\"><b>Articulation – Scaffolding – Eingebettete Daten – Paar verwandter Aufgaben</b></p>\n\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p><p>In der <b>konstruktivistischen Lerntheorie</b> geht es darum, dem Lernenden die Freiheit zu erschaffen, dass er sich sein eigenes Wissen konstruieren kann. Dem liegt die erkenntnistheoretische Auffassung zugrunde, dass Wissen nunmal subjektiv und individuell konstruiert wird.</p><p><br>Dazu gibt es diverse Modelle, anhand das Lernen und Lehren stattfindet, bzw. stattfinden sollte.</p><p>Zum einen gibt es den <b>Cognitive Apprenticeship </b>werden verschiedene Stufen beim Lernprozess dargestellt, und berücksichtigt. Zum einen gehört hierzu&nbsp;&nbsp;<b>Scaffolding, Coaching, und Articulation.</b>&nbsp;</p><p><b>Coaching</b> beschreibt, dass dem Lernenden z.B. vor dem Beginn der eigenen Projektarbeit Aufgaben vorgeführt werden, Modellvorlagen eines Protokolls, etc. zur Verfügung stehen. Dazu können auch verwandte Aufgaben zählen, nach deren Schemata die vorliegende Aufgabe gelöst werden kann.</p><p>Das Coaching, in diesem fall die verwandten Aufgaben sind indirekt in dem Lernprozess eingebettet. <b>Verwandte Aufgaben</b>, und somit Modelle von Lösungstrategien, die eventuell angewandt werden können, sind zugriffsbereit, werden jedoch nicht direkt vorgeführt. Also sind verwandte Aufgaben vorhanden, jedoch befinden sich die Schüler eher im Fading (Lehrpersonen verschwinden aus dem Lernprozess.)</p><p><b>Scaffolding </b>bedeutet, dass eine Lehrperson (oder ein Experte) im Hintergrund präsent ist, und als Ansprechperson bereit steht, um weitere Fragen zu beantworten.&nbsp;</p><p>Ein Scaffolding findet in dem Fallbeispiel nicht statt, da die Lehrpersonen keine Unterstützung leisten, sondern sich zurückhalten (Fading).</p><p><b>Articulation </b>beschreibt, dass der Lernende nach erfolgreicher Beendigung der Aufgabe seinen eigenen Lösungsweg reflektieren, und darstellen kann (bzw. ausformuliert).</p><p>Die Stufe der Articulation findet ebenfalls nicht in dem Fallbeispiel statt, da die Lernenden gar nicht an dem Punkt ankommen ihre Lösungen zusammenzutragen, und zu reflektieren.</p><p>Eingebettete Daten ?&nbsp;</p>\n\n\";}",
                    "target": "page",
                    "relateduserid": "h0sSOJhMJsrbKuSRR3qlsA==",
                    "contextlevel": "70",
                    "action": "updated",
                    "courseid": course,
                    "objectid": "274",
                    "id": "1711",
                    "timecreated": "1552222184",
                    "component": "mod_wiki",
                    "crud": "u",
                    "contextinstanceid": "1202"
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
                                    "cacherev": "1552313136",
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
                                    "cacherev": "1552319780",
                                    "showreports": "0",
                                    "groupmode": "1",
                                    "idnumber": "",
                                    "completionnotify": "0",
                                    "summary": "",
                                    "shortname": "MAP Vorbereitung (Bochum)",
                                    "maxbytes": "0",
                                    "theme": "",
                                    "enddate": "0",
                                    "groupmodeforce": "0",
                                    "newsitems": "5",
                                    "legacyfiles": "0",
                                    "lang": "de",
                                    "requested": "0",
                                    "url": course_full,
                                    "sortorder": "10010",
                                    "startdate": "1549839600",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1551692549",
                                    "format": "topics",
                                    "calendartype": "",
                                    "showgrades": "0",
                                    "marker": "8",
                                    "fullname": "MAP Vorbereitungskurs GM2",
                                    "type": "course",
                                    "id": course,
                                    "timecreated": "1526989731",
                                    "summaryformat": "1",
                                    "category": "1",
                                    "enablecompletion": "1",
                                    "defaultgroupingid": "0"
                                }
                            },
                            "description": {
                                "de": "A Moodle course"
                            },
                            "name": {
                                "de": "MAP Vorbereitungskurs GM2"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/course"
                        },
                        "id": course_full,
                        "objectType": "Activity"
                    },
                    {
                        "definition": {
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_module": {
                                    "forceformat": "0",
                                    "introformat": "1",
                                    "name": "Wiki - Woche 2",
                                    "intro": "<p>In diesem Wiki können Sie die Erläuterungstexte gemeinsam verfassen.<br>Bitte beachten Sie die Hinweise auf der erste Seite im Wiki.<br><br>Die <b>Einreichung </b>der gemeinsam erstellen Erläuterungstexte geschieht am Sonntag, <b>10.03.2019, 23:59 Uhr</b> automatisch. Danach wird das Wiki geschlossen und Sie können keine Änderungen mehr vornehmen.<br></p>",
                                    "url": "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1202",
                                    "editend": "0",
                                    "wikimode": "collaborative",
                                    "timemodified": "1550051204",
                                    "defaultformat": "html",
                                    "firstpagetitle": "Wiki zur Erstellung der Erläuterungstexte",
                                    "type": "wiki",
                                    "course": "9",
                                    "id": "60",
                                    "timecreated": "0",
                                    "editbegin": "0"
                                }
                            },
                            "description": {
                                "de": "<p>In diesem Wiki können Sie die Erläuterungstexte gemeinsam verfassen.<br>Bitte beachten Sie die Hinweise auf der erste Seite im Wiki.<br><br>Die <b>Einreichung </b>der gemeinsam erstellen Erläuterungstexte geschieht am Sonntag, <b>10.03.2019, 23:59 Uhr</b> automatisch. Danach wird das Wiki geschlossen und Sie können keine Änderungen mehr vornehmen.<br></p>"
                            },
                            "name": {
                                "de": "Wiki - Woche 2"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/wiki"
                        },
                        "id": "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1202",
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
                "name": user
            },
            "name": user,
            "objectType": "Agent"
        },
        "timestamp": "2019-03-10T13:49:44+01:00",
        "version": "1.0.0",
        "id": "c16d4842-2daa-48fb-b93f-b82430cac195",
        "verb": {
            "display": {
                "en": "update"
            },
            "id": "http://id.tincanapi.com/verb/updated"
        },
        "object": {
            "definition": {
                "extensions": {
                    "http://collide.info/moodle_wiki_update": {
                        "content_clean": content_clean_user,
                        "content_raw": "<div class=\"wiki-toc\"><p class=\"wiki-toc-title\">Inhaltsübersicht</p><p class=\"wiki-toc-section-1 wiki-toc-section\">1. <a href=\"#toc-1\"><span xml:lang=\"de\" lang=\"de\">Hinweise zur gemeinsamen Arbeit im Wiki</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+xml%3Alang%3D%22de%22+lang%3D%22de%22%3EHinweise+zur+gemeinsamen+Arbeit+im+Wiki%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></a></p><p class=\"wiki-toc-section-1 wiki-toc-section\">2. <a href=\"#toc-2\"><span xml:lang=\"de\" lang=\"de\">Frage 1 &amp; 2 - Kognitive Entwicklung nach Piaget</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+xml%3Alang%3D%22de%22+lang%3D%22de%22%3EFrage+1+%26amp%3B+2+-+Kognitive+Entwicklung+nach+Piaget%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></a></p><p class=\"wiki-toc-section-1 wiki-toc-section\">3. <a href=\"#toc-3\"><span xml:lang=\"de\" lang=\"de\">Frage 3 - Kognitive Entwicklung nach Wygotski</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+xml%3Alang%3D%22de%22+lang%3D%22de%22%3EFrage+3+-+Kognitive+Entwicklung+nach+Wygotski%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></a></p><p class=\"wiki-toc-section-1 wiki-toc-section\">4. <a href=\"#toc-4\"><span lang=\"de\" lang=\"de\" xml:lang=\"de\">Frage 4 - Wissensarten</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+lang%3D%22de%22+lang%3D%22de%22+xml%3Alang%3D%22de%22%3EFrage+4+-+Wissensarten%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></a></p><p class=\"wiki-toc-section-1 wiki-toc-section\">5. <a href=\"#toc-5\"><span xml:lang=\"de\" lang=\"de\">Frage 5 - Konstruktivismus &amp; Situiertes Lernen</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+xml%3Alang%3D%22de%22+lang%3D%22de%22%3EFrage+5+-+Konstruktivismus+%26amp%3B+Situiertes+Lernen%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></a></p></div><h3><a name=\"toc-1\"></a><span xml:lang=\"de\" lang=\"de\">Hinweise zur gemeinsamen Arbeit im Wiki</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+xml%3Alang%3D%22de%22+lang%3D%22de%22%3EHinweise+zur+gemeinsamen+Arbeit+im+Wiki%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></h3>\n<p align=\"justify\">Bitte beachten Sie folgende Hinweise zur gemeinsamen Arbeit mit Wiki.<br>\nWikis sind asynchron, es kann also nur unter bestimmten Umständen gleichzeitig daran gearbeitet werden. Um zu vermeiden, dass eine parallele Bearbeitung der Wikis gestört wird, achten Sie bitte dringend darauf, dass Sie die einzelnen Wikis <u>nicht auf der obersten Ebene bearbeiten</u> (s. oben: Anzeige –Bearbeiten – Kommentare usw.), sondern in den einzelnen Kapiteln (siehe [Bearbeiten] rechts neben den Kapiteln).</p>\n<p align=\"justify\">Zur Information: Die Überschriften der Wikis (z.B. Frage 1 – Kognitive Entwicklung nach Piaget) wurden von uns als „Überschrift groß“ formatiert.\nBitte ändern Sie diese Überschrift nicht. Der Fließtext für die Fragen (z.B. Fragetext für die erste Frage: „…“) wurde als „Absatz“ formatiert.</p>\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p>\n<h3><a name=\"toc-2\"></a><span xml:lang=\"de\" lang=\"de\">Frage 1 &amp; 2 - Kognitive Entwicklung nach Piaget</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+xml%3Alang%3D%22de%22+lang%3D%22de%22%3EFrage+1+%26amp%3B+2+-+Kognitive+Entwicklung+nach+Piaget%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></h3>\n_________________________________________________________<p></p>\n<p align=\"justify\"><i>Welche der folgenden Aussagen <u>treffen zu</u> und welche <u>treffen nicht zu</u>?</i></p>\n<p><b><span xml:lang=\"de\" lang=\"de\">1.</span></b></p><p align=\"justify\"> Die nächste Aufgabe der Mathearbeit sieht wirklich schwierig aus. Gar nicht so, wie die anderen Aufgaben, die sie im Unterricht geübt haben! Lars probiert eine Weile an der Aufgabe herum. Kurz darauf merkt er, dass er diese Aufgabe doch mit der Lösung aus dem Unterricht lösen kann. Er fragt sich, wie er das nur übersehen könnte. Die Aufgabe kann Lars zügig lösen.</p>\n<p><span xml:lang=\"de\" lang=\"de\">Diese Situation zeigt das Fehlschlagen der Assimilation.</span></p>\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p>\n<p><b><span xml:lang=\"de\" lang=\"de\">2.</span></b></p>\n<p align=\"justify\"> Herr M. war bereits in vielen teuren Restaurants.\nZum ersten Mal besucht er nun ein McBurger. Wie gewohnt setzt er sich auf einen der freien Plätze und wartet darauf, dass die Bedienung die Speisekarte bringt. Er wartet vergeblich - es kommt keine Bedienung an den Tisch. Als Antwort auf einen verwirrten Blick und den Ruf der Bedienung kommt vom Tresen: \"Wir bedienen Sie nicht am Tisch. Kommen Sie her.\"</p>\n<p><span xml:lang=\"de\" lang=\"de\">Die Erfahrung führt zu einer Akkomodation.</span></p>\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p><p>Unter <b>Assimilation</b> versteht man, dass die Umwelt anhand schon vorhandener Denkmuster interpretiert und erfasst wird. Bekannt dazu ist das wau-wau Schemata; ein kleines Kind nennt einen Hund wau-wau. Nun sieht es eine Katze, die ebenso wie der Hund, Fell besitzt, einen Schwanz hat, auf vier Beinen läuft, und nennt jene Katze auch wau-wau.</p><p>Ein&nbsp;<b>Fehlschlagen der Assimilation</b>&nbsp;bedeutet, dass neu erfahrene Vorkommnisse in der Umwelt nicht den eigenen Denkstrukturen zugeordnet werden können. In dem Fallbeispiel scheitert Lars zwar im ersten Moment daran, jedoch benötigt er nur einige Zeit bis die Assimilation stattfindet, und ähnliche Matheaufgaben ins Gedächtnis gerufen werden.<br></p><p><b>Akkomodation</b> beschreibt nun den Prozess, dass das eigene Denkmuster der Umwelt angepasst wird. Das heißt, in diesem Fall z.B. lernt das Kind, dass die Katze zwar ähnliche Eigenschaften wie der Hund (wauwau) besitzt, jedoch ein anderen Tiergattung angehört. Sie macht nicht wauwau, sie miaut.</p><p>In dem Fallbeispiel findet eine Akkomodation statt, indem Herr M. herausfindet, dass die Bedienung in jenem Restaurant anders gehandhabt wird, als in ihm schon bekannten Restaurants.</p><p><span xml:lang=\"de\" lang=\"de\"><br></span></p><h3><a name=\"toc-3\"></a><span xml:lang=\"de\" lang=\"de\">Frage 3 - Kognitive Entwicklung nach Wygotski</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+xml%3Alang%3D%22de%22+lang%3D%22de%22%3EFrage+3+-+Kognitive+Entwicklung+nach+Wygotski%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></h3>\n_________________________________________________________<p></p>\n<p><i><span xml:lang=\"de\" lang=\"de\">Trifft die Aussage zu</span></i><span xml:lang=\"de\" lang=\"de\">?</span></p>\n<p align=\"justify\">Mithilfe einer Lern-App schafft es Markus, sich Spanisch beizubringen und in einem Kurs die Sprachstufe A1/A2 zertifiziert zu bekommen. </p>\n<p align=\"justify\">Die Lern-App war demnach ein Werkzeug, welches Markus dabei unterstützt hat, in die Zone der proximalen Entwicklung zu kommen.</p>\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p>\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p><h3><a name=\"toc-4\"></a><span lang=\"de\" lang=\"de\" xml:lang=\"de\">Frage 4 - Wissensarten</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+lang%3D%22de%22+lang%3D%22de%22+xml%3Alang%3D%22de%22%3EFrage+4+-+Wissensarten%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></h3>\n_________________________________________________________<p></p>\n<p align=\"justify\"><i>Bitte ordnen Sie jede der folgenden drei Szenen\njeweils einer Wissensart zu. Jede Wissensart wird genau einmal benötigt.\nBeachten Sie, dass nicht alle der aufgeführten Wissensarten benötigt werden.</i></p><i>\n</i><p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">1.</span></b></p><p align=\"justify\"> Ein fünfjähriges Mädchen bekommt von seiner Großmutter ein Fahrrad geschenkt. Als die Großmutter nach einiger Zeit zu Besuch kommt, fährt das Mädchen ihr im Garten auf dem Fahrrad entgegen und ruft: „Schau, ich kann schon Rad fahren.“</p>\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\n<p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">2.</span></b></p><p align=\"justify\"> Nina hat ihre Hausarbeit bereits zu lange aufgeschoben. Heute muss sie wirklich anfangen. Aber in der WG ist es einfach immer zu laut. Daher entscheidet sie sich dazu, zur Uni zu fahren und die Hausarbeit in der Bibliothek zu schreiben.</p>\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\n<p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">3.</span></b></p><p align=\"justify\"> In der Nachhilfestunde soll Max eine Aufgabe lösen, die der Lehrer im Unterricht vorgestellt hat. Bevor Max jedoch die Aufgabe löst, soll er erklären, warum die Formel zur Lösung eingesetzt wird.</p>\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\n<p><b></b></p><p align=\"justify\"><b>Prozedurales Wissen - Selbstregulationswissen - Konzeptuelles Wissen - Situationales Wissen</b></p>\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p>\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Prozedurales Wissen</b>, auch Handlungswissen genannt beschreibt, dass Handlungen und/oder auch Lösungsstrategien sich anhand schon erfahrener Strategien und vollendeten Handlungen orientieren. D.h. man führt eine Handlung nach schon bekanntem Prozedere aus ?</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Selbstregulationswissen</b> beschreibt den regulierten Vorgang seine eigenen Empfindungen, und Emotionen zu bändigen, bzw. der Situation anzupassen. Eventuell auch eigene Lernstrategien zu überdenken, und zu reflektieren. Im Fallbeispiel 2 kann man so eventuell von Selbstregulationswissen sprechen, da Nina sich dessen bewusst ist, wie sie ihre Aufmerksamkeit am besten auf die Fertigstellung ihrer Hausarbeit lenkt.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Konzeptuelles Wissen </b>beschreibt hierbei, dass Wissen anhand von Konzepten, eventuell Formeln, Kategorien, und Oberbegriffen gebündelt und angewandt wird. Im Fallbeispiel 3 kann man von konzeptuellen Wissen sprechen, da Max seine Matheaufgabe nach ihm schon bekannten (und auch allgemeinen) Lösungswegen (einem Konzept) löst.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Situationales Wissen</b> beschreibt Wissen, das innerhalb einer sozialen Situation erworben, angewandt, und/oder gefestigt wird. Das kann durch soziale Interaktion und Kommunikation an sich passieren. Dabei kann ebenso die Motivation aus dem sozialen Umfeld, als auch Hilfestellung, Unterstützung und soziale Anerkennung dazu beitragen. Im ersten Fallbeispiel kann man somit von situationalem Wissen sprechen, da die Kleine Fahrrad fahren lernt, während ihre Großmutter ihr dabei über die Schultern schaut, und ihr Anerkennung dafür zeigt.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">1) Bei diesem Fall handelt es sich um das situationale Wissen. Das situationale Wissen beschreibt das Wissen über Anforderungen und Merkmale von Problemen in bestimmten Situationen. Anhand dieses Wissens kann anschließend die Aufmerksamkeit auf die Aspekte gelenkt werden, die relevant für die Problemlösung sind. Dabei wird oft auf Erfahrungen oder Erinnerungen zurückgegriffen. Wenn dem Individuum noch keine Lösung für die Situation bekannt ist, greift es oft auf ähnliche Situationen mittels seiner Erinnerung zurück, und nutzt die Problemlösung der damaligen Situation für die der jetzigen.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">2) Bei diesem Fall handelt es sich um das Selbstregulationswissen. Beim Selbstregulationswissen ergreift der/die Lernende Selbststeuerungsmaßnahmen und überwacht somit selbstständig seinen Lernprozess. Da Nina in der vorliegenden Situation eigenständig die Entscheidung trifft zur Uni zu fahren und somit über ihren Lernprozess bestimmt, kann man hier von Selbstregulationswissen sprechen.&nbsp;</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">3) Bei diesem Fall kann man vom konzeptuellem Wissen sprechen. Das konzeptuelle Wissen wird auch als \"semantisches Wissen\" bezeichnet und bezeichnet das Wissen über Fakten, Begriffe, Schemata und Prinzipien. Das konzeptuelle Wissen ermöglicht dem Individuum Beziehungen zwischen dem bereits vorhandenen und dem neuen Wissen herzustellen. In der vorliegenden Situation soll Max auf sein Wissen über ein bestimmtes Schemata (die Formel) zurückgreifen. Unteranderem stellt er mit der Erklärung, warum die Formel benötigt wird, eine Beziehung zwischen der Formel (vorhandenes Wissen) und der Lösung der Aufgabe (neues Wissen) her.&nbsp;</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><br></span></p><h3><a name=\"toc-5\"></a><span xml:lang=\"de\" lang=\"de\">Frage 5 - Konstruktivismus &amp; Situiertes Lernen</span> <a href=\"edit.php?pageid=274&amp;section=%3Cspan+xml%3Alang%3D%22de%22+lang%3D%22de%22%3EFrage+5+-+Konstruktivismus+%26amp%3B+Situiertes+Lernen%3C%2Fspan%3E\" class=\"wiki_edit_section\">[Bearbeiten]</a></h3>\n_________________________________________________________<p></p><p align=\"justify\"><i>Lesen Sie die folgende Kursbeschreibung und entscheiden Sie, welche der aufgeführten Gestaltungsmerkmalen verschiedener situierter Lernarrangements in diesem Kurs vorhanden sind.</i></p>\n<p align=\"justify\">SchülerInnen nehmen an einem Workshop teil, in dem das Konzept „Graphentheorien“ (Informatik) vermittelt werden soll. Dieser findet in einem außerschulischen Lernlabor statt.</p>\n<p align=\"justify\">Die Teilnehmenden des Workshops sollen die Organisatoren eines Jahrmarkts – einen Juristen, einen Schatzmeister und einen Magier – bei der Planung des Jahrmarkts unterstützen. Jeder der Organisatoren ist für einen bestimmten Bereich der Planung verantwortlich. Aufgabe für die Teilnehmenden ist es, die Organisation des Jahrmarkts als ExpertInnen zu unterstützen, indem sie deren spezifischen Probleme lösen. Diese Geschichte wird in einem animierten Film\npräsentiert.</p>\n<p align=\"justify\">Die Teilnehmenden werden auf drei Gruppen aufgeteilt, die jeweils einem Betreuer, der einen Organisator spielt, zugeteilt sind. Die Teilnehmenden sollen die Aufgabe jeweils in ihrer Gruppe lösen und sich dort gegenseitig bei der Arbeit unterstützen, laut denken, wie sie gerade vorgehen.</p>\n<p align=\"justify\">Eine Gruppe steht beispielsweise vor dem Problem, dass innerhalb der Geisterbahn alle Attraktionen mit Kabeln verbunden werden, wobei zur Einsparung von Geld möglichst wenig Kabel-Material verwendet werden sollen. Dieses Problem lässt sich mit <b>Algorithmen zur Suche des minimalen Spannbaums</b> lösen. Die Organisatoren geben jedoch<b> nur wenig Unterstützung</b> bei der Bearbeitung der Probleme, da etwa ein Jurist nicht mit Prinzipien der Informatik vertraut ist. Zur Unterstützung sind allerdings <i>in einem Kiosk verschiedene relevante und nicht relevante Zeitschriften ausgelegt</i>, die mögliche Lösungsansätze für die verschiedenen Probleme der Szenarien schülergerecht vorstellen. Zusätzlich dienen die Zeitschriften dazu, einen <b>Alltagsbezug der verwendeten informatischen Strategien vorzustellen</b>.</p>\n<p align=\"justify\">Haben die Teilnehmenden die Planung erfolgreich abgeschlossen, wird ihnen ein Abschlussfilm vorgespielt, der das erfolgreiche Stadtfest zeigt.</p>\n<p><b></b></p><p align=\"justify\"><b>Articulation – Scaffolding – Eingebettete Daten – Paar verwandter Aufgaben</b></p>\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p><p>In der <b>konstruktivistischen Lerntheorie</b> geht es darum, dem Lernenden die Freiheit zu erschaffen, dass er sich sein eigenes Wissen konstruieren kann. Dem liegt die erkenntnistheoretische Auffassung zugrunde, dass Wissen nunmal subjektiv und individuell konstruiert wird.</p><p><br>Dazu gibt es diverse Modelle, anhand das Lernen und Lehren stattfindet, bzw. stattfinden sollte.</p><p>Zum einen gibt es den <b>Cognitive Apprenticeship </b>werden verschiedene Stufen beim Lernprozess dargestellt, und berücksichtigt. Zum einen gehört hierzu&nbsp;&nbsp;<b>Scaffolding, Coaching, und Articulation.</b>&nbsp;</p><p><b>Coaching</b> beschreibt, dass dem Lernenden z.B. vor dem Beginn der eigenen Projektarbeit Aufgaben vorgeführt werden, Modellvorlagen eines Protokolls, etc. zur Verfügung stehen. Dazu können auch verwandte Aufgaben zählen, nach deren Schemata die vorliegende Aufgabe gelöst werden kann.</p><p>Das Coaching, in diesem fall die verwandten Aufgaben sind indirekt in dem Lernprozess eingebettet. <b>Verwandte Aufgaben</b>, und somit Modelle von Lösungstrategien, die eventuell angewandt werden können, sind zugriffsbereit, werden jedoch nicht direkt vorgeführt. Also sind verwandte Aufgaben vorhanden, jedoch befinden sich die Schüler eher im Fading (Lehrpersonen verschwinden aus dem Lernprozess.)</p><p><b>Scaffolding </b>bedeutet, dass eine Lehrperson (oder ein Experte) im Hintergrund präsent ist, und als Ansprechperson bereit steht, um weitere Fragen zu beantworten.&nbsp;</p><p>Ein Scaffolding findet in dem Fallbeispiel nicht statt, da die Lehrpersonen keine Unterstützung leisten, sondern sich zurückhalten (Fading).</p><p><b>Articulation </b>beschreibt, dass der Lernende nach erfolgreicher Beendigung der Aufgabe seinen eigenen Lösungsweg reflektieren, und darstellen kann (bzw. ausformuliert).</p><p>Die Stufe der Articulation findet ebenfalls nicht in dem Fallbeispiel statt, da die Lernenden gar nicht an dem Punkt ankommen ihre Lösungen zusammenzutragen, und zu reflektieren.</p><p>Eingebettete Daten ?&nbsp;</p>\n"
                    }
                },
                "description": {
                    "de": "Test description"
                },
                "name": {
                    "de": "Wiki zur Erstellung der Erläuterungstexte"
                },
                "type": "http://collide.info/moodle_wiki_page"
            },
            "id": "https://moodle.ikarion-projekt.de/mod/wiki/view.php?pageid=274",
            "objectType": "Activity"
        }
    }

    if process:
        sp.process_statement(statement)
    # json_s = json.dumps(statement)
    # json_s.replace("forum", "blabla")
    # statement = json.loads(json_s)

    return statement


def generate_xapi_statement_inter(*, user, course, time, verb, artefact, group=None,
                                  process=True):
    task_name = "Test_Wiki_Bla"
    course_full = "https://moodle.ikarion-projekt.de/course/view.php?id={}".format(course)
    statement = {
        "authority": {
            "objectType": "Agent",
            "name": "New Client",
            "mbox": "mailto:hello@learninglocker.net"
        },
        "stored": "2019-03-12T13:21:38.227Z",
        "context": {
            "extensions": {
                "http://collide.info/extensions/group": {
                    "311": {
                        "group_members": [
                            {
                                "name": "YAjW/wX68/Gmk+QtjpzCWg==",
                                "fullname": "cP4ZrroHA4OC7OLBPO1IChBPE9plkknnLOnqpKcD86g=",
                                "email": "P43D/ObyLlfj6bIYlyXXhvhBJiQDx4r8UWsWony3QincX/tdU/qtECWyvsksHioj",
                                "username": "+wRs4ylcVy2CaGbnAMs4NA=="
                            },
                            {
                                "name": "GA32Uf83DXlTfuu1FSeMFg==",
                                "fullname": "rJkxGM9yVOIpAjVoXJ1ZhA==",
                                "email": "1HGFKeWcPwguIY/Gbs23w9xf+11T+q0QJbK+ySweKiM=",
                                "username": "aROGBNUR1kyIIlRppuoF7w=="
                            },
                            {
                                "name": "1w21eIbpkSXstgIbXjb5MQ==",
                                "fullname": "lfy4EcVwvwQ5U5MODdRx/hBPE9plkknnLOnqpKcD86g=",
                                "email": "DD942q+B5EQJzH9XbE8GWApV/gzOdER6YUQhgms4zWw=",
                                "username": "kAGQl/YDZZJ/TagPxQmkaQ=="
                            },
                            {
                                "name": "h0sSOJhMJsrbKuSRR3qlsA==",
                                "fullname": "Nia47n6HXjJRb+KHo4yKWQ==",
                                "email": "v7a1dQ33BJ96n5Rl1gLsowta1hfiAs+An/K03OI8+Gc=",
                                "username": "WP/hHPNTh0zJeTwtDwQRUQ=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1228",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1229"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1551654300",
                            "task_start": "1551092400",
                            "task_name": "Woche 1 Mirroring",
                            "task_id": "71"
                        },
                        "timemodified": "1550828859",
                        "timecreated": "1550828859",
                        "description": "none",
                        "name": "W1Gruppe-1",
                        "id": "311"
                    },
                    group: {
                        "group_members": [
                            {
                                "name": "YAjW/wX68/Gmk+QtjpzCWg==",
                                "fullname": "cP4ZrroHA4OC7OLBPO1IChBPE9plkknnLOnqpKcD86g=",
                                "email": "P43D/ObyLlfj6bIYlyXXhvhBJiQDx4r8UWsWony3QincX/tdU/qtECWyvsksHioj",
                                "username": "+wRs4ylcVy2CaGbnAMs4NA=="
                            },
                            {
                                "name": "oxP3yJF/mny+oup/jprHJA==",
                                "fullname": "u4KufSmYeAF6O/EoY8OSlA==",
                                "email": "Uzw5Tt5eRMx503wEsCAy760fSrEyVN1nAKbVT1zoSjM=",
                                "username": "rxaXTX6920qtC2UwOhLhZw=="
                            },
                            {
                                "name": "h0sSOJhMJsrbKuSRR3qlsA==",
                                "fullname": "Nia47n6HXjJRb+KHo4yKWQ==",
                                "email": "v7a1dQ33BJ96n5Rl1gLsowta1hfiAs+An/K03OI8+Gc=",
                                "username": "WP/hHPNTh0zJeTwtDwQRUQ=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1202",
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1261"
                            ],
                            "task_type": "Test_Wiki_Le",
                            "task_end": "1552259100",
                            "task_start": "1551697200",
                            "task_name": task_name,
                            "task_id": "78"
                        },
                        "timemodified": "1551690322",
                        "timecreated": "1551690322",
                        "description": "none",
                        "name": "W2 Gruppe-1",
                        "id": group
                    }
                },
                "http://lrs.learninglocker.net/define/extensions/info": {
                    "https://moodle.org/": "3.2.3+ (Build: 20170509)"
                },
                "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log": {
                    "realuserid": None,
                    "eventname": "\\mod_wiki\\event\\page_updated",
                    "userid": "h0sSOJhMJsrbKuSRR3qlsA==",
                    "origin": "web",
                    "ip": "178.8.234.87",
                    "contextid": "2647",
                    "anonymous": "0",
                    "edulevel": "2",
                    "objecttable": "wiki_pages",
                    "other": "a:1:{s:10:\"newcontent\";s:14932:\"<h3><span xml:lang=\"de\" lang=\"de\">Hinweise zur gemeinsamen Arbeit im Wiki</span></h3>\n\n<p align=\"justify\">Bitte beachten Sie folgende Hinweise zur gemeinsamen Arbeit mit Wiki.<br>\nWikis sind asynchron, es kann also nur unter bestimmten Umständen gleichzeitig daran gearbeitet werden. Um zu vermeiden, dass eine parallele Bearbeitung der Wikis gestört wird, achten Sie bitte dringend darauf, dass Sie die einzelnen Wikis <u>nicht auf der obersten Ebene bearbeiten</u> (s. oben: Anzeige –Bearbeiten – Kommentare usw.), sondern in den einzelnen Kapiteln (siehe [Bearbeiten] rechts neben den Kapiteln).</p>\n\n<p align=\"justify\">Zur Information: Die Überschriften der Wikis (z.B. Frage 1 – Kognitive Entwicklung nach Piaget) wurden von uns als „Überschrift groß“ formatiert.\nBitte ändern Sie diese Überschrift nicht. Der Fließtext für die Fragen (z.B. Fragetext für die erste Frage: „…“) wurde als „Absatz“ formatiert.</p>\n\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p>\n\n<h3><span xml:lang=\"de\" lang=\"de\">Frage 1 &amp; 2 - Kognitive Entwicklung nach Piaget</span></h3>_________________________________________________________<p></p>\n\n<p align=\"justify\"><i>Welche der folgenden Aussagen <u>treffen zu</u> und welche <u>treffen nicht zu</u>?</i></p>\n\n<p><b><span xml:lang=\"de\" lang=\"de\">1.</span></b></p><p align=\"justify\"> Die nächste Aufgabe der Mathearbeit sieht wirklich schwierig aus. Gar nicht so, wie die anderen Aufgaben, die sie im Unterricht geübt haben! Lars probiert eine Weile an der Aufgabe herum. Kurz darauf merkt er, dass er diese Aufgabe doch mit der Lösung aus dem Unterricht lösen kann. Er fragt sich, wie er das nur übersehen könnte. Die Aufgabe kann Lars zügig lösen.</p>\n\n<p><span xml:lang=\"de\" lang=\"de\">Diese Situation zeigt das Fehlschlagen der Assimilation.</span></p>\n\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p>\n\n<p><b><span xml:lang=\"de\" lang=\"de\">2.</span></b></p>\n<p align=\"justify\"> Herr M. war bereits in vielen teuren Restaurants.\nZum ersten Mal besucht er nun ein McBurger. Wie gewohnt setzt er sich auf einen der freien Plätze und wartet darauf, dass die Bedienung die Speisekarte bringt. Er wartet vergeblich - es kommt keine Bedienung an den Tisch. Als Antwort auf einen verwirrten Blick und den Ruf der Bedienung kommt vom Tresen: \"Wir bedienen Sie nicht am Tisch. Kommen Sie her.\"</p>\n\n<p><span xml:lang=\"de\" lang=\"de\">Die Erfahrung führt zu einer Akkomodation.</span></p>\n\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p><p>Unter <b>Assimilation</b> versteht man, dass die Umwelt anhand schon vorhandener Denkmuster interpretiert und erfasst wird. Bekannt dazu ist das wau-wau Schemata; ein kleines Kind nennt einen Hund wau-wau. Nun sieht es eine Katze, die ebenso wie der Hund, Fell besitzt, einen Schwanz hat, auf vier Beinen läuft, und nennt jene Katze auch wau-wau.</p><p>Ein&nbsp;<b>Fehlschlagen der Assimilation</b>&nbsp;bedeutet, dass neu erfahrene Vorkommnisse in der Umwelt nicht den eigenen Denkstrukturen zugeordnet werden können. In dem Fallbeispiel scheitert Lars zwar im ersten Moment daran, jedoch benötigt er nur einige Zeit bis die Assimilation stattfindet, und ähnliche Matheaufgaben ins Gedächtnis gerufen werden.<br></p><p><b>Akkomodation</b> beschreibt nun den Prozess, dass das eigene Denkmuster der Umwelt angepasst wird. Das heißt, in diesem Fall z.B. lernt das Kind, dass die Katze zwar ähnliche Eigenschaften wie der Hund (wauwau) besitzt, jedoch ein anderen Tiergattung angehört. Sie macht nicht wauwau, sie miaut.</p><p>In dem Fallbeispiel findet eine Akkomodation statt, indem Herr M. herausfindet, dass die Bedienung in jenem Restaurant anders gehandhabt wird, als in ihm schon bekannten Restaurants.</p><p><span xml:lang=\"de\" lang=\"de\"><br></span></p><h3><span xml:lang=\"de\" lang=\"de\">Frage 3 - Kognitive Entwicklung nach Wygotski</span></h3>_________________________________________________________<p></p>\n\n<p><i><span xml:lang=\"de\" lang=\"de\">Trifft die Aussage zu</span></i><span xml:lang=\"de\" lang=\"de\">?</span></p>\n\n<p align=\"justify\">Mithilfe einer Lern-App schafft es Markus, sich Spanisch beizubringen und in einem Kurs die Sprachstufe A1/A2 zertifiziert zu bekommen. </p>\n\n<p align=\"justify\">Die Lern-App war demnach ein Werkzeug, welches Markus dabei unterstützt hat, in die Zone der proximalen Entwicklung zu kommen.</p>\n\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p>\n\n<p><span xml:lang=\"de\" lang=\"de\">&nbsp;</span></p><h3><span lang=\"de\" lang=\"de\" xml:lang=\"de\">Frage 4 - Wissensarten</span></h3>_________________________________________________________<p></p>\r\n\r\n<p align=\"justify\"><i>Bitte ordnen Sie jede der folgenden drei Szenen\r\njeweils einer Wissensart zu. Jede Wissensart wird genau einmal benötigt.\r\nBeachten Sie, dass nicht alle der aufgeführten Wissensarten benötigt werden.</i></p><i>\r\n\r\n</i><p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">1.</span></b></p><p align=\"justify\"> Ein fünfjähriges Mädchen bekommt von seiner Großmutter ein Fahrrad geschenkt. Als die Großmutter nach einiger Zeit zu Besuch kommt, fährt das Mädchen ihr im Garten auf dem Fahrrad entgegen und ruft: „Schau, ich kann schon Rad fahren.“</p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\r\n\r\n<p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">2.</span></b></p><p align=\"justify\"> Nina hat ihre Hausarbeit bereits zu lange aufgeschoben. Heute muss sie wirklich anfangen. Aber in der WG ist es einfach immer zu laut. Daher entscheidet sie sich dazu, zur Uni zu fahren und die Hausarbeit in der Bibliothek zu schreiben.</p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\r\n\r\n<p><b><span lang=\"de\" lang=\"de\" xml:lang=\"de\">3.</span></b></p><p align=\"justify\"> In der Nachhilfestunde soll Max eine Aufgabe lösen, die der Lehrer im Unterricht vorgestellt hat. Bevor Max jedoch die Aufgabe löst, soll er erklären, warum die Formel zur Lösung eingesetzt wird.</p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">&nbsp;</span></p>\r\n\r\n<p><b></b></p><p align=\"justify\"><b>Prozedurales Wissen - Selbstregulationswissen - Konzeptuelles Wissen - Situationales Wissen</b></p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">_________________________________________________________<br>\r\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p>\r\n\r\n<p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Prozedurales Wissen</b>, auch Handlungswissen genannt beschreibt, dass Handlungen und/oder auch Lösungsstrategien sich anhand schon erfahrener Strategien und vollendeten Handlungen orientieren. D.h. man führt eine Handlung nach schon bekanntem Prozedere aus ?</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Selbstregulationswissen</b> beschreibt den regulierten Vorgang seine eigenen Empfindungen, und Emotionen zu bändigen, bzw. der Situation anzupassen. Eventuell auch eigene Lernstrategien zu überdenken, und zu reflektieren. Im Fallbeispiel 2 kann man so eventuell von Selbstregulationswissen sprechen, da Nina sich dessen bewusst ist, wie sie ihre Aufmerksamkeit am besten auf die Fertigstellung ihrer Hausarbeit lenkt.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Konzeptuelles Wissen </b>beschreibt hierbei, dass Wissen anhand von Konzepten, eventuell Formeln, Kategorien, und Oberbegriffen gebündelt und angewandt wird. Im Fallbeispiel 3 kann man von konzeptuellen Wissen sprechen, da Max seine Matheaufgabe nach ihm schon bekannten (und auch allgemeinen) Lösungswegen (einem Konzept) löst.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><b>Situationales Wissen</b> beschreibt Wissen, das innerhalb einer sozialen Situation erworben, angewandt, und/oder gefestigt wird. Das kann durch soziale Interaktion und Kommunikation an sich passieren. Dabei kann ebenso die Motivation aus dem sozialen Umfeld, als auch Hilfestellung, Unterstützung und soziale Anerkennung dazu beitragen. Im ersten Fallbeispiel kann man somit von situationalem Wissen sprechen, da die Kleine Fahrrad fahren lernt, während ihre Großmutter ihr dabei über die Schultern schaut, und ihr Anerkennung dafür zeigt.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">1) Bei diesem Fall handelt es sich um das situationale Wissen. Das situationale Wissen beschreibt das Wissen über Anforderungen und Merkmale von Problemen in bestimmten Situationen. Anhand dieses Wissens kann anschließend die Aufmerksamkeit auf die Aspekte gelenkt werden, die relevant für die Problemlösung sind. Dabei wird oft auf Erfahrungen oder Erinnerungen zurückgegriffen. Wenn dem Individuum noch keine Lösung für die Situation bekannt ist, greift es oft auf ähnliche Situationen mittels seiner Erinnerung zurück, und nutzt die Problemlösung der damaligen Situation für die der jetzigen.</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">2) Bei diesem Fall handelt es sich um das Selbstregulationswissen. Beim Selbstregulationswissen ergreift der/die Lernende Selbststeuerungsmaßnahmen und überwacht somit selbstständig seinen Lernprozess. Da Nina in der vorliegenden Situation eigenständig die Entscheidung trifft zur Uni zu fahren und somit über ihren Lernprozess bestimmt, kann man hier von Selbstregulationswissen sprechen.&nbsp;</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\">3) Bei diesem Fall kann man vom konzeptuellem Wissen sprechen. Das konzeptuelle Wissen wird auch als \"semantisches Wissen\" bezeichnet und bezeichnet das Wissen über Fakten, Begriffe, Schemata und Prinzipien. Das konzeptuelle Wissen ermöglicht dem Individuum Beziehungen zwischen dem bereits vorhandenen und dem neuen Wissen herzustellen. In der vorliegenden Situation soll Max auf sein Wissen über ein bestimmtes Schemata (die Formel) zurückgreifen. Unteranderem stellt er mit der Erklärung, warum die Formel benötigt wird, eine Beziehung zwischen der Formel (vorhandenes Wissen) und der Lösung der Aufgabe (neues Wissen) her.&nbsp;</span></p><p><span lang=\"de\" lang=\"de\" xml:lang=\"de\"><br></span></p><h3><span xml:lang=\"de\" lang=\"de\">Frage 5 - Konstruktivismus &amp; Situiertes Lernen</span></h3>_________________________________________________________<p></p><p align=\"justify\"><i>Lesen Sie die folgende Kursbeschreibung und entscheiden Sie, welche der aufgeführten Gestaltungsmerkmalen verschiedener situierter Lernarrangements in diesem Kurs vorhanden sind.</i></p>\n\n<p align=\"justify\">SchülerInnen nehmen an einem Workshop teil, in dem das Konzept „Graphentheorien“ (Informatik) vermittelt werden soll. Dieser findet in einem außerschulischen Lernlabor statt.</p>\n\n<p align=\"justify\">Die Teilnehmenden des Workshops sollen die Organisatoren eines Jahrmarkts – einen Juristen, einen Schatzmeister und einen Magier – bei der Planung des Jahrmarkts unterstützen. Jeder der Organisatoren ist für einen bestimmten Bereich der Planung verantwortlich. Aufgabe für die Teilnehmenden ist es, die Organisation des Jahrmarkts als ExpertInnen zu unterstützen, indem sie deren spezifischen Probleme lösen. Diese Geschichte wird in einem animierten Film\npräsentiert.</p>\n\n<p align=\"justify\">Die Teilnehmenden werden auf drei Gruppen aufgeteilt, die jeweils einem Betreuer, der einen Organisator spielt, zugeteilt sind. Die Teilnehmenden sollen die Aufgabe jeweils in ihrer Gruppe lösen und sich dort gegenseitig bei der Arbeit unterstützen, laut denken, wie sie gerade vorgehen.</p>\n\n<p align=\"justify\">Eine Gruppe steht beispielsweise vor dem Problem, dass innerhalb der Geisterbahn alle Attraktionen mit Kabeln verbunden werden, wobei zur Einsparung von Geld möglichst wenig Kabel-Material verwendet werden sollen. Dieses Problem lässt sich mit <b>Algorithmen zur Suche des minimalen Spannbaums</b> lösen. Die Organisatoren geben jedoch<b> nur wenig Unterstützung</b> bei der Bearbeitung der Probleme, da etwa ein Jurist nicht mit Prinzipien der Informatik vertraut ist. Zur Unterstützung sind allerdings <i>in einem Kiosk verschiedene relevante und nicht relevante Zeitschriften ausgelegt</i>, die mögliche Lösungsansätze für die verschiedenen Probleme der Szenarien schülergerecht vorstellen. Zusätzlich dienen die Zeitschriften dazu, einen <b>Alltagsbezug der verwendeten informatischen Strategien vorzustellen</b>.</p>\n\n<p align=\"justify\">Haben die Teilnehmenden die Planung erfolgreich abgeschlossen, wird ihnen ein Abschlussfilm vorgespielt, der das erfolgreiche Stadtfest zeigt.</p>\n\n<p><b></b></p><p align=\"justify\"><b>Articulation – Scaffolding – Eingebettete Daten – Paar verwandter Aufgaben</b></p>\n\n<p><span xml:lang=\"de\" lang=\"de\">_________________________________________________________<br>\n*Bitte schreiben Sie ab hier Ihren Erläuterungstext</span></p><p>In der <b>konstruktivistischen Lerntheorie</b> geht es darum, dem Lernenden die Freiheit zu erschaffen, dass er sich sein eigenes Wissen konstruieren kann. Dem liegt die erkenntnistheoretische Auffassung zugrunde, dass Wissen nunmal subjektiv und individuell konstruiert wird.</p><p><br>Dazu gibt es diverse Modelle, anhand das Lernen und Lehren stattfindet, bzw. stattfinden sollte.</p><p>Zum einen gibt es den <b>Cognitive Apprenticeship </b>werden verschiedene Stufen beim Lernprozess dargestellt, und berücksichtigt. Zum einen gehört hierzu&nbsp;&nbsp;<b>Scaffolding, Coaching, und Articulation.</b>&nbsp;</p><p><b>Coaching</b> beschreibt, dass dem Lernenden z.B. vor dem Beginn der eigenen Projektarbeit Aufgaben vorgeführt werden, Modellvorlagen eines Protokolls, etc. zur Verfügung stehen. Dazu können auch verwandte Aufgaben zählen, nach deren Schemata die vorliegende Aufgabe gelöst werden kann.</p><p>Das Coaching, in diesem fall die verwandten Aufgaben sind indirekt in dem Lernprozess eingebettet. <b>Verwandte Aufgaben</b>, und somit Modelle von Lösungstrategien, die eventuell angewandt werden können, sind zugriffsbereit, werden jedoch nicht direkt vorgeführt. Also sind verwandte Aufgaben vorhanden, jedoch befinden sich die Schüler eher im Fading (Lehrpersonen verschwinden aus dem Lernprozess.)</p><p><b>Scaffolding </b>bedeutet, dass eine Lehrperson (oder ein Experte) im Hintergrund präsent ist, und als Ansprechperson bereit steht, um weitere Fragen zu beantworten.&nbsp;</p><p>Ein Scaffolding findet in dem Fallbeispiel nicht statt, da die Lehrpersonen keine Unterstützung leisten, sondern sich zurückhalten (Fading).</p><p><b>Articulation </b>beschreibt, dass der Lernende nach erfolgreicher Beendigung der Aufgabe seinen eigenen Lösungsweg reflektieren, und darstellen kann (bzw. ausformuliert).</p><p>Die Stufe der Articulation findet ebenfalls nicht in dem Fallbeispiel statt, da die Lernenden gar nicht an dem Punkt ankommen ihre Lösungen zusammenzutragen, und zu reflektieren.</p><p>Eingebettete Daten ?&nbsp;</p>\n\n\";}",
                    "target": "page",
                    "relateduserid": "h0sSOJhMJsrbKuSRR3qlsA==",
                    "contextlevel": "70",
                    "action": "updated",
                    "courseid": course,
                    "objectid": "274",
                    "id": "1711",
                    "timecreated": "1552222184",
                    "component": "mod_wiki",
                    "crud": "u",
                    "contextinstanceid": "1202"
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
                                    "cacherev": "1552313136",
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
                                    "cacherev": "1552319780",
                                    "showreports": "0",
                                    "groupmode": "1",
                                    "idnumber": "",
                                    "completionnotify": "0",
                                    "summary": "",
                                    "shortname": "MAP Vorbereitung (Bochum)",
                                    "maxbytes": "0",
                                    "theme": "",
                                    "enddate": "0",
                                    "groupmodeforce": "0",
                                    "newsitems": "5",
                                    "legacyfiles": "0",
                                    "lang": "de",
                                    "requested": "0",
                                    "url": course_full,
                                    "sortorder": "10010",
                                    "startdate": "1549839600",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1551692549",
                                    "format": "topics",
                                    "calendartype": "",
                                    "showgrades": "0",
                                    "marker": "8",
                                    "fullname": "MAP Vorbereitungskurs GM2",
                                    "type": "course",
                                    "id": course,
                                    "timecreated": "1526989731",
                                    "summaryformat": "1",
                                    "category": "1",
                                    "enablecompletion": "1",
                                    "defaultgroupingid": "0"
                                }
                            },
                            "description": {
                                "de": "A Moodle course"
                            },
                            "name": {
                                "de": "MAP Vorbereitungskurs GM2"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/course"
                        },
                        "id": course_full,
                        "objectType": "Activity"
                    },
                    {
                        "definition": {
                            "extensions": {
                                "http://lrs.learninglocker.net/define/extensions/moodle_module": {
                                    "forceformat": "0",
                                    "introformat": "1",
                                    "name": "Wiki - Woche 2",
                                    "intro": "<p>In diesem Wiki können Sie die Erläuterungstexte gemeinsam verfassen.<br>Bitte beachten Sie die Hinweise auf der erste Seite im Wiki.<br><br>Die <b>Einreichung </b>der gemeinsam erstellen Erläuterungstexte geschieht am Sonntag, <b>10.03.2019, 23:59 Uhr</b> automatisch. Danach wird das Wiki geschlossen und Sie können keine Änderungen mehr vornehmen.<br></p>",
                                    "url": "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1202",
                                    "editend": "0",
                                    "wikimode": "collaborative",
                                    "timemodified": "1550051204",
                                    "defaultformat": "html",
                                    "firstpagetitle": "Wiki zur Erstellung der Erläuterungstexte",
                                    "type": "wiki",
                                    "course": "9",
                                    "id": "60",
                                    "timecreated": "0",
                                    "editbegin": "0"
                                }
                            },
                            "description": {
                                "de": "<p>In diesem Wiki können Sie die Erläuterungstexte gemeinsam verfassen.<br>Bitte beachten Sie die Hinweise auf der erste Seite im Wiki.<br><br>Die <b>Einreichung </b>der gemeinsam erstellen Erläuterungstexte geschieht am Sonntag, <b>10.03.2019, 23:59 Uhr</b> automatisch. Danach wird das Wiki geschlossen und Sie können keine Änderungen mehr vornehmen.<br></p>"
                            },
                            "name": {
                                "de": "Wiki - Woche 2"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/wiki"
                        },
                        "id": "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1202",
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
                "name": user
            },
            "name": user,
            "objectType": "Agent"
        },
        "timestamp": 1551654300,
        "version": "1.0.0",
        "id": "c16d4842-2daa-48fb-b93f-b82430cac195",
        "verb": {
            "display": {
                "en": "viewed"
            },
            "id": "http://id.tincanapi.com/verb/viewed"
        },
        "object": {
            "definition": {
                "extensions": {
                    "http://lrs.learninglocker.net/define/extensions/moodle_block": {
                        "promptmessage": "Derzeit gibt es keine neuen Hinweise zur Forenaktivität eurer Gruppe.",
                        "prompttype": "default",
                        "contextinstanceid": "572",
                        "component": "block_grouplatency"
                    }
                },
                "description": {
                    "en": "Grouplatency prompt viewed"
                },
                "name": {
                    "en": "Grouplatency"
                },
                "type": "https://moodle.ikarion-projekt.de/define/type/moodle/block_grouplatency"
            },
            "id": "https://moodle.ikarion-projekt.de/course/view.php?id=2",
            "objectType": "Activity"
        }
    }

    if process:
        sp.process_statement(statement)
    # json_s = json.dumps(statement)
    # json_s.replace("forum", "blabla")
    # statement = json.loads(json_s)

    return statement


def generate_xapi_statement_inter_2(*, user, course, time, verb, artefact, group=None,
                                    process=True):
    task_name = "Test_Wiki_Bla"
    course_full = "https://moodle.ikarion-projekt.de/course/view.php?id={}".format(course)
    statement = {
        "authority": {
            "objectType": "Agent",
            "name": "New Client",
            "mbox": "mailto:hello@learninglocker.net"
        },
        "stored": "2019-01-19T21:39:08.040Z",
        "context": {
            "extensions": {
                "http://collide.info/extensions/group": {
                    "158": {
                        "group_members": [
                            {
                                "name": "/SYh8zWao54Hly6FA/eTgA==",
                                "fullname": "ETq6BCkNj1rCxwHjkT0fmhBPE9plkknnLOnqpKcD86g=",
                                "email": "motVyU7Anh5Cmjv+kKJWxJOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "EhSRnE8BeW4nvtHsp1xNbA=="
                            },
                            {
                                "name": "t/lZTuN8H58qZRrmIDuDUQ==",
                                "fullname": "Pk5pPWxgWDI7i1z4TV4QTw==",
                                "email": "d59Odj2FtAHY3fVi2QY+51ymKX7bEmpVVTT+Ldk2jRU=",
                                "username": "+XihLFceGG5dVMIZMq1jAA=="
                            },
                            {
                                "name": "8Ue2wJvcAxsrfcVNbYL0pA==",
                                "fullname": "+50DtA9Ifil86m+MjsQwLhBPE9plkknnLOnqpKcD86g=",
                                "email": "Y2aIO+VFMOA1adYz5KdjTJOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "sd1acpD4IbRsI1cHbAsi7g=="
                            },
                            {
                                "name": "cD/hMMcE+SOKDje6nNcUxw==",
                                "fullname": "BacSZULRJ/UK09Ok4cVUNA==",
                                "email": "m9ctUIyrKOtvPkFgEGb2Y20RQoohsdxyABWei6/Tni4=",
                                "username": "BK17xiRQ1shtdcmZ3B5ulQ=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=994",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=995"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1540767600",
                            "task_start": "1539597600",
                            "task_name": "Task1_IntModelle_Ko",
                            "task_id": "37"
                        },
                        "timemodified": "1539592607",
                        "timecreated": "1539592598",
                        "description": "none",
                        "name": "Gruppe Integrationsmodelle G5",
                        "id": "158"
                    },
                    "191": {
                        "group_members": [
                            {
                                "name": "vvwWX4aNx8IEA9/k7yt/hw==",
                                "fullname": "7XlnwDVMLLEaZvVwFEchQw==",
                                "email": "gtMrffWUEMhLCgxOcUGIiy66V94wTnvQeF7zcpnB1I0=",
                                "username": "nvniOoHCyR2lIxnWnDWOzQ=="
                            },
                            {
                                "name": "t/lZTuN8H58qZRrmIDuDUQ==",
                                "fullname": "Pk5pPWxgWDI7i1z4TV4QTw==",
                                "email": "d59Odj2FtAHY3fVi2QY+51ymKX7bEmpVVTT+Ldk2jRU=",
                                "username": "+XihLFceGG5dVMIZMq1jAA=="
                            },
                            {
                                "name": "8Ue2wJvcAxsrfcVNbYL0pA==",
                                "fullname": "+50DtA9Ifil86m+MjsQwLhBPE9plkknnLOnqpKcD86g=",
                                "email": "Y2aIO+VFMOA1adYz5KdjTJOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "sd1acpD4IbRsI1cHbAsi7g=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1031",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1032"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1541977200",
                            "task_start": "1540810800",
                            "task_name": "Task2_SozPraes_Ko",
                            "task_id": "47"
                        },
                        "timemodified": "1543222553",
                        "timecreated": "1540806725",
                        "description": "none",
                        "name": "Gruppe Soziale_Praesenz G5",
                        "id": "191"
                    },
                    "214": {
                        "group_members": [
                            {
                                "name": "/SYh8zWao54Hly6FA/eTgA==",
                                "fullname": "ETq6BCkNj1rCxwHjkT0fmhBPE9plkknnLOnqpKcD86g=",
                                "email": "motVyU7Anh5Cmjv+kKJWxJOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "EhSRnE8BeW4nvtHsp1xNbA=="
                            },
                            {
                                "name": "t/lZTuN8H58qZRrmIDuDUQ==",
                                "fullname": "Pk5pPWxgWDI7i1z4TV4QTw==",
                                "email": "d59Odj2FtAHY3fVi2QY+51ymKX7bEmpVVTT+Ldk2jRU=",
                                "username": "+XihLFceGG5dVMIZMq1jAA=="
                            },
                            {
                                "name": "2JU9E9oUbIh4dtQ/JpiujQ==",
                                "fullname": "tD0NrPrgcIX6oTeIeq3t3Q==",
                                "email": "EMhj25NyoJfOW7nJ/ARBK3rjW8RjNmVLqnLc70+IkRHVkTR2RsyDBwQIK8DRm3pc",
                                "username": "apyUyu0ZuGwqFLWH6JLMyA=="
                            },
                            {
                                "name": "8Ue2wJvcAxsrfcVNbYL0pA==",
                                "fullname": "+50DtA9Ifil86m+MjsQwLhBPE9plkknnLOnqpKcD86g=",
                                "email": "Y2aIO+VFMOA1adYz5KdjTJOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "sd1acpD4IbRsI1cHbAsi7g=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1045",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1046"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1543186800",
                            "task_start": "1542020400",
                            "task_name": "Task3_Brainstorming_Ko",
                            "task_id": "54"
                        },
                        "timemodified": "1542012510",
                        "timecreated": "1542012510",
                        "description": "none",
                        "name": "Gruppe Brainstorming G4",
                        "id": "214"
                    },
                    "242": {
                        "group_members": [
                            {
                                "name": "dkiFJIzVaf/TqPN+LQ7fLg==",
                                "fullname": "D8IfbkBPL25Z5F8Go8+y/VUGFXHaGOaEnIk+Fc/zWMI=",
                                "email": "nUDBKcpV4tEfBVUnq0Rth6v9jpd0EiijUMn1L775fm0=",
                                "username": "uJYjRankpq6p5eZGrO0Luw=="
                            },
                            {
                                "name": "fQ2Z3nMPn9K0nSA75zNs2Q==",
                                "fullname": "X43K59mVgEbEs7d7MbiCbQ==",
                                "email": "0W1VIu7Jly8+aTJZJ2qlyfnqp3Yfm54ZYbyfz1qIZ5c=",
                                "username": "y69ohF7TqT8hp7oOp328gw=="
                            },
                            {
                                "name": "8Ue2wJvcAxsrfcVNbYL0pA==",
                                "fullname": "+50DtA9Ifil86m+MjsQwLhBPE9plkknnLOnqpKcD86g=",
                                "email": "Y2aIO+VFMOA1adYz5KdjTJOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "sd1acpD4IbRsI1cHbAsi7g=="
                            },
                            {
                                "name": "Re3Mce6Yjm8KF4ZcEkD9Rg==",
                                "fullname": "3F8TPx44gWR+yUedKy6r0Q==",
                                "email": "IFiGdJMzpa210FDa1l8Poav9jpd0EiijUMn1L775fm0=",
                                "username": "9Fn+66a45+n2ihacGWgo0g=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1050",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1051"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1544396700",
                            "task_start": "1543230000",
                            "task_name": "Task4_Common_Ground_WA",
                            "task_id": "59"
                        },
                        "timemodified": "1543223768",
                        "timecreated": "1543223768",
                        "description": "none",
                        "name": "Gruppe Common_Ground G-6",
                        "id": "242"
                    },
                    "255": {
                        "group_members": [
                            {
                                "name": "8shCFjo+boJIroJYjEVG3w==",
                                "fullname": "dI/dmJzGBzx1S+Y2CtLCJRBPE9plkknnLOnqpKcD86g=",
                                "email": "TnixfLVVU9XVg9tMGSO8ZZOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "E652Rn4KB0UwR70bpYga5g=="
                            },
                            {
                                "name": "ouFVSEQq09GEg6Z/713Cdw==",
                                "fullname": "i3fNrt2xnWcWA95s/ZKugA==",
                                "email": "PTaQkEi45WFuQG65zOg69Pnqp3Yfm54ZYbyfz1qIZ5c=",
                                "username": "5rfrzlUoncZcmIlb5wrmBQ=="
                            },
                            {
                                "name": "Aes4XtX8DFbi7Kn00GWVug==",
                                "fullname": "Jkl7ecCobjJ2SzVyCdHz5/g3MBUKdpF4CFhL1J7YQfI=",
                                "email": "Sl8kPk1TEKz2pGPy67BcLmgMePYQ4ERvVCXcotYAyB4kSpAhzoNzjgx7JuM/Ka0e",
                                "username": "vPLlG0ZKNQPgyaquBnPF2Q=="
                            },
                            {
                                "name": "CN48GSRnSHlK/aUd3u5eHQ==",
                                "fullname": "y/HEWxSTB9kQYad1w3/wdQ==",
                                "email": "FLGj4PYFORA5AG/SkU4REPnqp3Yfm54ZYbyfz1qIZ5c=",
                                "username": "rVjS5oMX0p49fXnwHoPXDg=="
                            },
                            {
                                "name": "8Ue2wJvcAxsrfcVNbYL0pA==",
                                "fullname": "+50DtA9Ifil86m+MjsQwLhBPE9plkknnLOnqpKcD86g=",
                                "email": "Y2aIO+VFMOA1adYz5KdjTJOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "sd1acpD4IbRsI1cHbAsi7g=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1065",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1067"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1545606300",
                            "task_start": "1544439600",
                            "task_name": "Task5_Informationsaustausch_WA",
                            "task_id": "62"
                        },
                        "timemodified": "1544430844",
                        "timecreated": "1544430591",
                        "description": "none",
                        "name": "Gruppe Informationsaustausch G-2",
                        "id": "255"
                    },
                    "275": {
                        "group_members": [
                            {
                                "name": "sD63w9Czm87Aj4+hNvtf6w==",
                                "fullname": "h9tZd4kNVUEKSRW3WYJJvg==",
                                "email": "BOfkpMOWDmBQu/w53687wPnqp3Yfm54ZYbyfz1qIZ5c=",
                                "username": "p6cRMaLBhxn0zaHf0W36RA=="
                            },
                            {
                                "name": "o1v6f/6FhE1Y3sIa9mPzmg==",
                                "fullname": "4eJO2Vlz1TC6TyZu7Tn1a8+HhtqiFLWE0mXKGWJTcg4=",
                                "email": "QOpazbMsjmbNDIviB3TAvoDOchwrtjbOXVtM1lKsp4T+LIGzcr3LT2VKGZEQhh9E",
                                "username": "ZlyD6qrMY4CVuymfMa8vTQ=="
                            },
                            {
                                "name": "8Ue2wJvcAxsrfcVNbYL0pA==",
                                "fullname": "+50DtA9Ifil86m+MjsQwLhBPE9plkknnLOnqpKcD86g=",
                                "email": "Y2aIO+VFMOA1adYz5KdjTJOd38GOxy251sx0ttKkVuwQTxPaZZJJ5yzp6qSnA/Oo",
                                "username": "sd1acpD4IbRsI1cHbAsi7g=="
                            }
                        ],
                        "task": {
                            "task_resources": [
                                "https://moodle.ikarion-projekt.de/mod/forum/view.php?id=1074",
                                "https://moodle.ikarion-projekt.de/mod/wiki/view.php?id=1075"
                            ],
                            "task_type": "collaborative wiki writing",
                            "task_end": "1548025500",
                            "task_start": "1546858800",
                            "task_name": "Task6_Soz_Int_WA",
                            "task_id": "65"
                        },
                        "timemodified": "1546854117",
                        "timecreated": "1546853798",
                        "description": "none",
                        "name": "Gruppe Soz_Int G-4",
                        "id": "275"
                    }
                },
                "http://lrs.learninglocker.net/define/extensions/info": {
                    "https://moodle.org/": "3.2.3+ (Build: 20170509)"
                },
                "http://lrs.learninglocker.net/define/extensions/moodle_logstore_standard_log": {
                    "realuserid": None,
                    "eventname": "\\block_grouplatency\\event\\grouplatency_prompt_viewed",
                    "userid": "8Ue2wJvcAxsrfcVNbYL0pA==",
                    "origin": "web",
                    "ip": "87.123.197.34",
                    "contextid": 1705,
                    "anonymous": 0,
                    "edulevel": 0,
                    "objecttable": None,
                    "other": "a:2:{s:4:\"type\";s:4:\"note\";s:7:\"message\";s:228:\"<strong>Aufgrund der Datenlage gibt es den folgenden Hinweis für euch</strong>\r\n<br><br>\r\nWerft regelmäßig einen Blick ins Gruppenforum und gebt euch zeitnah Rückmeldungen, damit sich eure Gruppenmitglieder beachtet fühlen.\";}",
                    "target": "grouplatency_prompt",
                    "relateduserid": None,
                    "contextlevel": 80,
                    "action": "viewed",
                    "courseid": course,
                    "objectid": None,
                    "timecreated": 1547933946,
                    "component": "block_grouplatency",
                    "crud": "r",
                    "contextinstanceid": "605"
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
                                    "cacherev": "1552319780",
                                    "showreports": "0",
                                    "groupmode": "1",
                                    "idnumber": "",
                                    "completionnotify": "0",
                                    "summary": "",
                                    "shortname": "MAP Vorbereitung (Bochum)",
                                    "maxbytes": "0",
                                    "theme": "",
                                    "enddate": "0",
                                    "groupmodeforce": "0",
                                    "newsitems": "5",
                                    "legacyfiles": "0",
                                    "lang": "de",
                                    "requested": "0",
                                    "url": course_full,
                                    "sortorder": "10010",
                                    "startdate": "1549839600",
                                    "visible": "1",
                                    "visibleold": "1",
                                    "timemodified": "1551692549",
                                    "format": "topics",
                                    "calendartype": "",
                                    "showgrades": "0",
                                    "marker": "8",
                                    "fullname": "MAP Vorbereitungskurs GM2",
                                    "type": "course",
                                    "id": course,
                                    "timecreated": "1526989731",
                                    "summaryformat": "1",
                                    "category": "1",
                                    "enablecompletion": "1",
                                    "defaultgroupingid": "0"
                                }
                            },
                            "description": {
                                "de": "A Moodle course"
                            },
                            "name": {
                                "de": "MAP Vorbereitungskurs GM2"
                            },
                            "type": "http://lrs.learninglocker.net/define/type/moodle/course"
                        },
                        "id": course_full,
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
                "name": "8Ue2wJvcAxsrfcVNbYL0pA=="
            },
            "name": "+50DtA9Ifil86m+MjsQwLhBPE9plkknnLOnqpKcD86g=",
            "objectType": "Agent"
        },
        "timestamp": 1547933946,
        "version": "1.0.0",
        "id": "af50c9d6-a52a-4be9-bda1-5d60aeed8cb0",
        "verb": {
            "display": {
                "en": "viewed"
            },
            "id": "http://id.tincanapi.com/verb/viewed"
        },
        "object": {
            "definition": {
                "extensions": {
                    "http://lrs.learninglocker.net/define/extensions/moodle_block": {
                        "promptmessage": "<strong>Aufgrund der Datenlage gibt es den folgenden Hinweis für euch</strong>\r\n<br><br>\r\nWerft regelmäßig einen Blick ins Gruppenforum und gebt euch zeitnah Rückmeldungen, damit sich eure Gruppenmitglieder beachtet fühlen.",
                        "prompttype": "note",
                        "contextinstanceid": "605",
                        "component": "block_grouplatency"
                    }
                },
                "description": {
                    "en": "Grouplatency prompt viewed"
                },
                "name": {
                    "en": "Grouplatency"
                },
                "type": "https://moodle.ikarion-projekt.de/define/type/moodle/block_grouplatency"
            },
            "id": "https://moodle.ikarion-projekt.de/course/view.php?id=11",
            "objectType": "Activity"
        }
    }

    if process:
        sp.process_statement(statement)
    # json_s = json.dumps(statement)
    # json_s.replace("forum", "blabla")
    # statement = json.loads(json_s)

    return statement
