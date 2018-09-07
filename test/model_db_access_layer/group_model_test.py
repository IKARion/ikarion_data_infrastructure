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

class GroupModelDAOTestCase(unittest.TestCase):
    pass


class UserModelEndpointsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        idi.app.testing = True

    def setUp(self):
        self.app = idi.app.test_client()
        mock_con = mongomock.MongoClient()
        um.con = mock_con
        gm.con = mock_con
        pdt.populate_xapi_model(mock_con)

    def test_get_group_tasks(self):
        response = self.app.get(GM_PRE+"/group_tasks/"+COURSEID)
        print(response)
        r_json = json.loads(response.data)
        print(r_json)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
