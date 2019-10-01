from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.jobstores.memory import MemoryJobStore


# put in your own data and copy this file to config.py

class Config(object):
    DEBUG = False
    TESTING = False
    MONGO_URI = "base mongo uri"
    LRS_URL = "Url to learning locker"
    KEY = "key for learning locker"
    SECRET = "secret for learning locker"
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
    RSCRIPT = "Rscript"

class ProductionConfig(Config):
    MONGO_URI = "Your production mongo uri"
    SCHEDULER_JOBSTORES = {
        'default': MongoDBJobStore(),
    }

class DevelopmentConfig(Config):
    DEBUG = True
    SCHEDULER_JOBSTORES = {
        'default': MemoryJobStore(),
    }
    MONGO_URI = "your test mongo db"


class TestingConfig(Config):
    TESTING = True