

def generate_xapi_statement(*, user, course, time, verb, object, group):
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
                "type": 'http://lrs.learninglocker.net/define/type/moodle/course',
            },
            "id": object,
            "objectType": "Activity"
        }
    }

    return statement

def generate_xapi_statement_inter_2(*, user, course, time, verb, object, group=None,
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


    return statement