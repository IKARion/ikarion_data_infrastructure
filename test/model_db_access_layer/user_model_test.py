import os
import unittest
import mongomock
from test.model_db_access_layer import user_model_test_data as umd
from test.model_db_access_layer import populate_database_test_data as pdt

from ikarion_data_management.data_access_layer.model_db_access_layer import user_model_dao as um
from ikarion_data_management.data_access_layer.model_db_access_layer import group_model_dao as gm
from ikarion_data_management.data_model_api.user_model_endpoints import encode_url_chars
import ikarion_data_management.ikarion_data_infrastructure as idi
import json

ITEM_NUMBER = 5

# class UserModelDAOTestCase(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls):
#         mock_con = mongomock.MongoClient()
#         um.con = mock_con
#         for i in range(ITEM_NUMBER):
#             test_user = umd.fill_user_model(i, i, list(range(i)), ITEM_NUMBER)
#             mock_con.db.usermodels.insert_one(test_user)
#     def setUp(self):
#         pass
#
#     def test_getAllCourses(self):
#         courses = um.get_all_courses()
#         expected_result = [str(i) for i in range(ITEM_NUMBER)]
#         self.assertEqual(set(courses), set(expected_result))
#
#     def test_getAllUsers(self):
#         users = um.get_all_users()
#         expected_result = [str(i) for i in range(ITEM_NUMBER)]
#         self.assertEqual(set(users), set(expected_result))
#
#     def test_getAllUsersForCourse(self):
#         users = um.get_all_users_for_course("1")
#         user = users[0]
#         expected = {"uid": "1"}
#         # To compare dict subset relation you can use items() and <=
#         self.assertLessEqual(expected.items(), user.items())
#
#     def test_getAllCoursesForUser(self):
#         users = um.get_all_courses_for_user("1")
#         user = users[0]
#         expected = {"course": "1"}
#         # To compare dict subset relation you can use items() and <=
#         self.assertLessEqual(expected.items(), user.items())
#
#     def test_getUserModel(self):
#         user = um.getUserModel("1", "1")
#
#         expected = {"uid": "1", "course": "1"}
#         self.assertLessEqual(expected.items(), user.items())
#
#     def test_getUserModelsForCourse(self):
#         users = um.getUserModelsForCourse("1")
#         user = users[0]
#
#         expected = {"uid": "1", "course": "1"}
#         self.assertLessEqual(expected.items(), user.items())
#
#     def tearDown(self):
#         pass

# Usermodel Url prefix
UM_PRE = "/user_model"
GM_PRE = "/groups"
# COURSEID = encode_url_chars("http://localhost/ikarion_moodle/course/view.php?id=3")
COURSEID_TEMPLATE = encode_url_chars("https://moodle.ikarion-projekt.de/course/view.php?id=")+"{}"


class UserModelDAOTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mock_con = mongomock.MongoClient()
        um.con = mock_con
        gm.con = mock_con
        pdt.populate_xapi_model(gm.con)
        cls.mock_db = True
        # with idi.app.app_context():
        #     pdt.populate_xapi_model(gm.con)
        # cls.con = mock_con
        # cls.mock_db = False

    def setUp(self):
        # mock_db = True
        self.ctx = idi.app.app_context()
        self.ctx.__enter__()
        courses = um.get_all_courses()
        self.courses = [item["courseid"] for item in um.get_all_courses()]
        self.course = self.courses[0]


    def test_get_all_courses(self):
        courses = um.get_all_courses()
        print(courses)

    def test_get_user_artefact_types(self):
        print("artefact types")
        artefact_types = um.get_user_artefact_types("1", self.course)
        print(artefact_types)

    def test_get_user_model_for_course(self):
        print("user")
        user = um.get_user_model_for_course("1", self.course)
        print(user)

    def test_get_user_active_days(self):
        print("active days")
        active_days = um.get_user_active_days("1", self.course)
        print(active_days)
        self.assertGreater(len(active_days), 0)

    def test_get_user_times(self):
        times = um.get_all_user_times("0", self.course)
        print(times)
        self.assertEqual(len(times), 36)

    def test_get_users_for_group(self):
        users = gm.get_all_users_for_group(self.course, "0")
        print(users)

    def test_get_groups_for_course(self):
        groups = gm.get_all_groups_for_course(self.course)
        print(groups)
        self.assertEqual(len(groups), 4)

    def test_get_avg_latency(self):
        avg_lat = um.get_user_average_latency("0", self.course)
        print(avg_lat)

    # def test_get_avg_latency_with_constraints(self):
    #     constraints = [{
    #         "verb.id": "http://id.tincanapi.com/verb/replied"
    #     }]
    #     courses = um.get_all_courses()
    #     avg_lat_course_0 = um.get_user_average_latency("0", self.course, *constraints)
    #     avg_lat_course_1 = um.get_user_average_latency("0", courses[1], *constraints)
    #     print(avg_lat_course_0)
    #     print(avg_lat_course_1)

    def test_get_group_activities(self):
        if not self.mock_db:
            group_activities = gm.get_group_activities(self.course, "0")
            print(group_activities)


    # def test_get_xapi_statements(self):
    #     statements = list(UserModelDAOTestCase.con.db.xapi_statements.find({}))
    #     print(len(statements))

    def tearDown(self):
        self.ctx.__exit__(None, None, None)


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
        self.courses = [encode_url_chars(item["courseid"]) for item in um.get_all_courses()]
        self.course = self.courses[0]

    def test_get_user_model_for_course(self):
        print("user")
        response = self.app.get(UM_PRE + "/model/{}/2".format(self.course))
        user_model = json.loads(response.data)
        print(user_model)

    def test_get_user_models_for_course(self):
        print("usermodels")
        response = self.app.get(UM_PRE + "/models/{}".format(self.course))
        user_models = json.loads(response.data)
        print(user_models)

    def test_get_all_courses(self):
        # Does not work with mongomock
        print("courses")
        response = self.app.get(UM_PRE + "/courses")
        print(response.data)
        courses = json.loads(response.data)["data"]
        print(courses)

    def test_get_users(self):
        print("users")
        response = self.app.get(UM_PRE + "/")
        print(response.data)

    def test_get_users_for_course(self):
        print("users for course")
        response = self.app.get(UM_PRE + "/{}".format(self.course))
        r_json = json.loads(response.data)
        print(response.data)
        print(r_json)

    def test_get_user_times(self):
        print("times:")
        response = self.app.get(UM_PRE + "/times/0/{}".format(self.course))
        print(response.data)


    def test_avg_latency_user(self):
        print("avg_latency")
        response = self.app.get(UM_PRE + "/avg_latency/0/{}".format(self.course))
        print(response.data)


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
