import os
import unittest
import mongomock
from test.model_db_access_layer import populate_database_test_data as pdt

from ikarion_data_management.data_access_layer.model_db_access_layer import group_model_dao as gm, user_model_dao as um
from ikarion_data_management.data_model_api.user_model_endpoints import encode_url_chars
import ikarion_data_management.ikarion_data_infrastructure as idi
import json

ITEM_NUMBER = 5

UM_PRE = "/user_model"
GM_PRE = "/groups"
COURSEID = encode_url_chars("http://localhost/ikarion_moodle/course/view.php?id=3")


class GroupModelDAOWikiTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        idi.app.testing = True
        concept_l = ["arbeit", "wiki", "kognitive Entwicklung"]
        task_prefix = "Test_Wiki"
        task_concepts = {
            "task_prefix": task_prefix,
            "concepts": concept_l,
        }
        with idi.app.app_context():
            print("lol")
            # gm.con.db.task_concepts.insert_one(task_concepts)
            # pdt.populate_xapi_model_wiki_mod(gm.con)

    def setUp(self):
        self.app = idi.app.test_client()
        self.app = idi.app.test_client()
        self.ctx = idi.app.app_context()
        self.ctx.__enter__()
        # mock_con = mongomock.MongoClient()
        # um.con = mock_con
        # gm.con = mock_con
        # pdt.populate_xapi_model(mock_con)
        self.courses = [encode_url_chars(item["courseid"]) for item in um.get_all_courses()]
        self.course = "https://moodle.ikarion-projekt.de/course/view.php?id=0"

    def test_calc_group_weighted_word_count(self):
        res = gm.get_group_weighted_wiki_word_count(self.course, "0", 1901225046)
        print(res)

    def tearDown(self):
        self.ctx.__exit__(None, None, None)

class GroupModelEndpointsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        idi.app.testing = True



    def setUp(self):
        # mock_con = mongomock.MongoClient()
        # um.con = mock_con
        # gm.con = mock_con
        # pdt.populate_xapi_model(mock_con)
        self.courses = [encode_url_chars(item["courseid"]) for item in um.get_all_courses()]
        self.course = "https://moodle.ikarion-projekt.de/course/view.php?id=0"

    def test_get_groups_for_course(self):
        response = self.app.get(GM_PRE + "/groups_for_course/{}".format(self.course))
        print(response.data)
        r_json = json.loads(response.data)
        print(r_json)

    def test_get_group_tasks(self):
        response = self.app.get(GM_PRE + "/group_tasks/" + self.course)
        print(self.course)
        print(response)
        print(response.data)
        response_str = response.data.decode("utf-8")
        print(response_str)
        r_json = json.loads(response_str)
        print(r_json)

    def tearDown(self):
        pass


class GroupModelSelfAssessmentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        idi.app.testing = True

    def setUp(self):
        self.app = idi.app.test_client()
        # mock_con = mongomock.MongoClient()
        # um.con = mock_con
        # gm.con = mock_con
        with idi.app.app_context():
            pdt.populate_xapi_model_self_assessment(gm.con)

    def test_get_self_assessment(self):
        course = encode_url_chars("https://moodle.ikarion-projekt.de/course/view.php?id={}".format(0))
        url_temp = GM_PRE + "/group_self_assessment/{}/{}/{}/"
        url = url_temp.format(course, 0, "66")
        response = self.app.get(url)
        print(COURSEID)
        print(response)
        print(response.data)
        response_str = response.data.decode("utf-8")
        print(response_str)
        r_json = json.loads(response_str)
        print(r_json)

    def tearDown(self):
        pass

class GroupModelWikiCountTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        idi.app.testing = True

    def setUp(self):
        self.app = idi.app.test_client()
        # mock_con = mongomock.MongoClient()
        # um.con = mock_con
        # gm.con = mock_con
        # with idi.app.app_context():
        #     pdt.populate_xapi_model_self_assessment(gm.con)

    def test_get_wiki_count(self):
        course = encode_url_chars("https://moodle.ikarion-projekt.de/course/view.php?id={}".format(0))
        url_temp = GM_PRE + "/weighted_wiki_wordcount/{}/{}/{}/"
        url = url_temp.format(course, 0, 78)
        response = self.app.get(url)
        print()
        print(response)
        print(response.data)
        response_str = response.data.decode("utf-8")
        print(response_str)
        r_json = json.loads(response_str)
        print(r_json)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
