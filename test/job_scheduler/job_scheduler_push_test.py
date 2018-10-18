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
dashboard_path = "~/PycharmProjects/ikarion_analytics_dashboard/dashboard"
dashboard_command = shlex.split('R -e "shiny::runApp(\'{}\', port=5341)"'.format(dashboard_path))

class JobSchedulerPushTest(unittest.TestCase):

    job_was_called = 0
    @classmethod
    def setUpClass(cls):
        def scheduledRscriptMock(uri):
            cls.job_was_called = cls.job_was_called + 1
            print("RScript Job was called - uri: {}".format(uri))
        md.scheduledRscript = scheduledRscriptMock

        idi.app.use_reloader = False
        def run_flask_app():
            # idi.app.testing = True
            idi.app.run(host="0.0.0.0", use_reloader=False)

        cls.flask_thread = threading.Thread(target=run_flask_app)
        cls.flask_thread.start()
        print("Setup Flask Thread")
        time.sleep(4)

    @classmethod
    def tearDownClass(cls):
        pass



    def setUp(self):
        self.app = idi.app.test_client()
        JobSchedulerPushTest.job_was_called = 0
        self.dashboard_process = subprocess.Popen(dashboard_command,
                                                  stdout=subprocess.PIPE,
                                                  shell=True)
        time.sleep(8)
        start_dashboard_and_jobs()
        time.sleep(5)


    def tearDown(self):
        self.dashboard_process.kill()
        print("Terminated Dashboard")


    def test_non_triggering_statement(self):
        self.app.get(LOG_PRE + "/log_forwarding",
                     data=json.dumps(xs.non_trigger_statment),
                     content_type='application/json')

        self.assertEqual(JobSchedulerPushTest.job_was_called, 0)


    def test_triggering_statement(self):
        self.app.get(LOG_PRE + "/log_forwarding",
                     data=json.dumps(xs.triggering_statement),
                     content_type='application/json')
        self.assertEqual(JobSchedulerPushTest.job_was_called, 1)



def start_dashboard_and_jobs():
    # Selenium needs gecko drivers on path of pc
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:5341")
    time.sleep(4)
    # multiple elements with this class
    # course_select = driver.find_element_by_class_name("selectize-dropdown-content")
    # select_children = course_select.find_elements_by_class_name("div")
    # course_select.click()
    # select_children[0].click()

    # group_model_link = driver.find_element_by_partial_link_text("Group Models")
    # group_model_link.click()
    # options = driver.find_elements_by_class_name("option")
    # for option in options:
    #     print(option.text)
    #     if option.text == "minute":
    #         parent = option.find_element_by_xpath("..")
    #         parentparent = parent.find_element_by_xpath("..")
    #         parent.click()
    #         parentparent.click()
    #         option.click()
    #         print("selected send every minute")
    #
    # send_button = driver.find_element_by_id("GM_to_XPS")
    # send_button.click()

    # driver.close()



