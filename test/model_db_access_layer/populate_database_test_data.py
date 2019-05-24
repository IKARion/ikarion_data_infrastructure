import test.model_db_access_layer.user_model_test_data as umd
import pymongo

database_url = "mongodb://ikarion:ikariondb@cluster0-shard-00-00-n3pml.mongodb.net:27017,cluster0-shard-00-01-n3pml.mongodb.net:27017,cluster0-shard-00-02-n3pml.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"


# def populate_user_model():
#
#     with pymongo.MongoClient(database_url) as client:
#
#         for course in range(2):
#             for user in range(10):
#                 base_time = 1517443200.0 + course*user*60
#                 user_model = umd.fill_user_model(user, course, 5, 5,
#                                                  num_actions=5,
#                                                  base_time=base_time,
#                                                  randomized=True)
#                 client.db.usermodels.insert_one(user_model)

def populate_database():
    print("populating")
    with pymongo.MongoClient(database_url) as client:
        populate_xapi_model(client)


def populate_xapi_model(client):
    statement_list = generate_xapi_model()
    for statement in statement_list:
        client.db.xapi_statements.insert_one(statement)


def populate_xapi_model_self_assessment(client):
    statement_list = generate_xapi_model_self_assessment()
    for statement in statement_list:
        client.db.xapi_statements.insert_one(statement)


def populate_xapi_model_wiki_mod(client):
    statement_list = generate_xapi_model_wiki_concepts()
    for statement in statement_list:
        client.db.xapi_statements.insert_one(statement)


def populate_xapi_model_intervention(client):
    statement_list = generate_xapi_model_interventions()
    for statement in statement_list:
        client.db.xapi_statements.insert_one(statement)


def generate_xapi_model_interventions(process=True):
    name_list = [
        "nlrrOSj7CO4Pk21IIcDnog==",
        "tLbffKo5+/MJtqFFCnIWEg==",
        "wdqshw4nFEYjiBA+UokJ5w==",
    ]
    verb = "http://id.tincanapi.com/verb/replied"
    artefact = "http://localhost:5555/moodle32/moodle/mod/forum/discuss.php?d=1#12"
    statement_list = []
    for course in range(1):
        for group in range(2):
            for user_i, user_str in enumerate(name_list):
                course_offset = course * 3600 * 24 * 7
                user_offest = user_i * 3600 * 3
                group_latency_factor = 1 + 0.1 * group
                base_time = 1550478910.0 + course_offset * course
                for i in range(10):
                    time = base_time + (i * 3600 * 2 * group_latency_factor) + course_offset + user_offest
                    course_str = str(course)
                    group_str = str(group)
                    statement = umd.generate_xapi_statement_inter(user=user_str,
                                                                  course=course_str,
                                                                  group=group_str,
                                                                  time=time,
                                                                  verb=verb,
                                                                  artefact=artefact,
                                                                  process=process)
                    statement_list.append(statement)
    return statement_list


def generate_xapi_model_self_assessment(process=True):
    name_list = [
        "nlrrOSj7CO4Pk21IIcDnog==",
        "tLbffKo5+/MJtqFFCnIWEg==",
        "wdqshw4nFEYjiBA+UokJ5w==",
    ]
    verb = "http://id.tincanapi.com/verb/replied"
    artefact = "http://localhost:5555/moodle32/moodle/mod/forum/discuss.php?d=1#12"
    statement_list = []
    for course in range(1):
        for group in range(2):
            for user_i, user_str in enumerate(name_list):
                course_offset = course * 3600 * 24 * 7
                user_offest = user_i * 3600 * 3
                group_latency_factor = 1 + 0.1 * group
                base_time = 1550478910.0 + course_offset * course
                for i in range(10):
                    time = base_time + (i * 3600 * 2 * group_latency_factor) + course_offset + user_offest
                    course_str = str(course)
                    group_str = str(group)
                    statement = umd.generate_xapi_self_assessment_statement(user=user_str,
                                                                            course=course_str,
                                                                            group=group_str,
                                                                            time=time,
                                                                            verb=verb,
                                                                            artefact=artefact,
                                                                            process=process)
                    statement_list.append(statement)
    return statement_list


def generate_xapi_model(process=True):
    verb = "http://id.tincanapi.com/verb/replied"
    artefact = "http://localhost:5555/moodle32/moodle/mod/forum/discuss.php?d=1#12"
    statement_list = []
    for course in range(2):
        for group in range(4):
            for user in range(3):
                course_offset = course * 3600 * 24 * 7
                user_offest = user * 3600 * 3
                group_latency_factor = 1 + 0.1 * group
                base_time = 1536147000.0 + course_offset * course
                for i in range(10):
                    time = base_time + (i * 3600 * 2 * group_latency_factor) + course_offset + user_offest
                    course_str = str(course)
                    group_str = str(group)
                    user_str = str(user)
                    statement = umd.generate_xapi_statement2(user=user_str,
                                                             course=course_str,
                                                             group=group_str,
                                                             time=time,
                                                             verb=verb,
                                                             artefact=artefact,
                                                             process=process)
                    statement_list.append(statement)
    return statement_list


def generate_xapi_model_self_assessment(process=True):
    name_list = [
        "nlrrOSj7CO4Pk21IIcDnog==",
        "tLbffKo5+/MJtqFFCnIWEg==",
        "wdqshw4nFEYjiBA+UokJ5w==",
    ]
    verb = "http://id.tincanapi.com/verb/replied"
    artefact = "http://localhost:5555/moodle32/moodle/mod/forum/discuss.php?d=1#12"
    statement_list = []
    for course in range(1):
        for group in range(2):
            for user_i, user_str in enumerate(name_list):
                course_offset = course * 3600 * 24 * 7
                user_offest = user_i * 3600 * 3
                group_latency_factor = 1 + 0.1 * group
                base_time = 1550478910.0 + course_offset * course
                for i in range(10):
                    time = base_time + (i * 3600 * 2 * group_latency_factor) + course_offset + user_offest
                    course_str = str(course)
                    group_str = str(group)
                    statement = umd.generate_xapi_self_assessment_statement(user=user_str,
                                                                            course=course_str,
                                                                            group=group_str,
                                                                            time=time,
                                                                            verb=verb,
                                                                            artefact=artefact,
                                                                            process=process)
                    statement_list.append(statement)
    return statement_list


def generate_xapi_model_wiki_concepts(process=True):
    name_list = [
        "YAjW/wX68/Gmk+QtjpzCWg==",
        "oxP3yJF/mny+oup/jprHJA==",
        "h0sSOJhMJsrbKuSRR3qlsA==",
    ]
    verb = "http://id.tincanapi.com/verb/replied"
    artefact = "http://localhost:5555/moodle32/moodle/mod/forum/discuss.php?d=1#12"
    statement_list = []
    for course in range(1):
        for group in range(1):
            for user_i, user_str in enumerate(name_list):
                course_offset = course * 3600 * 24 * 7
                user_offest = user_i * 3600 * 3
                group_latency_factor = 1 + 0.1 * group
                base_time = 1550478910.0 + course_offset * course
                for i in range(1):
                    time = base_time + (i * 3600 * 2 * group_latency_factor) + course_offset + user_offest
                    course_str = str(course)
                    group_str = str(group)
                    statement = umd.generate_xapi_statement_wiki_mod(user=user_str,
                                                                     course=course_str,
                                                                     group=group_str,
                                                                     time=time,
                                                                     verb=verb,
                                                                     artefact=artefact,
                                                                     process=process,
                                                                     user_i=user_i,
                                                                     statement_i=i)
                    statement_list.append(statement)
    return statement_list


def clear_xap_statements():
    with pymongo.MongoClient(database_url) as client:
        client.db.xapi_statements.delete_many({})

# clear_xap_statements()
# populate_database()
