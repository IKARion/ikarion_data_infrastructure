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


def populate_xapi_model(client):
    for course in range(2):
        for user in range(5):
            base_time = 1517443200.0 + course*user*60
            for i in range(10):
                time = base_time + i*3600*24
                statement = umd.generate_xapi_statement(user, course, time, "testverb")
                client.db.xapi_statements.insert(statement)


def clear_user_model():
    with pymongo.MongoClient(database_url) as client:
        client.db.usermodels.delete_many({})

