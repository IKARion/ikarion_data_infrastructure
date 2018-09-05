from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.memory import MemoryJobStore
class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = "mongodb://ikarion:ikariondb@cluster0-shard-00-00-n3pml.mongodb.net:27017,cluster0-shard-00-01-n3pml.mongodb.net:27017,cluster0-shard-00-02-n3pml.mongodb.net:27017/db2?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"
    LRS_URL = "http://descartes.inf.uni-due.de:9001"
    KEY = "b3f32910db630eacff743fcbb96e5111485e3d17"
    SECRET = "c8783e809298c5e8d15630433a934ae026592d94"
    XPERIENCE_API_VERSION = "1.0.3"
    SCHEDULER_JOBSTORES = {
        'default': MongoDBJobStore(),
    }
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    SCHEDULER_EXECUTORS_PROCESSPOOL = {
        'type': 'processpool',
        'max_workers': '5'
    }
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    SCHEDULER = {
        'timezone': 'UTC'
    }
    RSCRIPT = "Rscript.exe"

class ProductionConfig(Config):
    MONGO_URI = "mongodb://ikarion:ikariondb@cluster0-shard-00-00-n3pml.mongodb.net:27017,cluster0-shard-00-01-n3pml.mongodb.net:27017,cluster0-shard-00-02-n3pml.mongodb.net:27017/db2?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"
    SCHEDULER_JOBSTORES = {
        'default': MongoDBJobStore(),
    }

class DevelopmentConfig(Config):
    DEBUG = True
    SCHEDULER_JOBSTORES = {
        'default': MemoryJobStore(),
    }
    MONGO_URI = "mongodb://ikarion:ikariondb@cluster0-shard-00-00-n3pml.mongodb.net:27017,cluster0-shard-00-01-n3pml.mongodb.net:27017,cluster0-shard-00-02-n3pml.mongodb.net:27017/db2?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin"

class TestingConfig(Config):
    TESTING = True