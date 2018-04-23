from flask_pymongo import PyMongo
from pymongo import MongoClient
# import ikarion_data_management.ikarion_data_infrastructure as idi

# mongo_uri = "mongodb://ikarion:ikariondb@cluster0-shard-00-00-n3pml.mongodb.net:27017,cluster0-shard-00-01-n3pml.mongodb.net:27017,cluster0-shard-00-02-n3pml.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"


modelDBConnection = PyMongo()
xapiDBConnection = PyMongo()

# modelDBConnection = MongoClient(mongo_uri)
# xapiDBConnection = MongoClient(mongo_uri)
