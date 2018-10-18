import unittest
import mongomock
import json
import subprocess
import shlex
import time
from selenium import webdriver
import threading

import ikarion_data_management.data_access_layer.management_access_layer.management_dao as md
import ikarion_data_management.ikarion_data_infrastructure as idi
from ikarion_data_management.data_access_layer.model_db_access_layer import user_model_dao as um
import test.job_scheduler.xapi_statements as xs


LOG_PRE = "/logs"




def scheduledRscriptMock(uri):
    print("RScript Job was called - uri: {}".format(uri))

md.scheduledRscript = scheduledRscriptMock

idi.app.use_reloader = False

def run_flask_app():
    # idi.app.testing = True
    idi.app.run(host="0.0.0.0", use_reloader=False)

run_flask_app()