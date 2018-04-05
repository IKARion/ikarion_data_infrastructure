import os
import ikarion_data_management.ikarion_data_infrastructure as ik
import unittest
import mongomock
from test.model_db_access_layer import user_model_test_data as umd
from test.model_db_access_layer import populate_database_test_data as pdt

from ikarion_data_management.data_access_layer.model_db_access_layer import user_model_dao as um
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


class UserModelDAOTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        mock_con = mongomock.MongoClient()
        um.con = mock_con
        pdt.populate_xapi_model(mock_con)
    def setUp(self):
        pass

    def test_get_user_artefact_types(self):
        print("artefact types")
        artefact_types = um.get_user_artefact_types("1", "1")
        print(artefact_types)

    def test_get_user_model_for_course(self):
        print("user")
        user = um.get_user_model_for_course("1", "1")
        print(user)

    def test_get_user_active_days(self):
        print("active days")
        active_days = um.get_user_active_days("1", "1")
        print(active_days)
        self.assertEqual(len(active_days), 10)

    def test_get_user_times(self):
        times = um.get_all_user_times("0", "0")
        print(times)
        self.assertEqual(len(times), 10)

    def test_get_avg_latency(self):
        avg_lat = um.get_user_average_latency("0", "0")
        print(avg_lat)

    def test_get_avg_latency_with_constraints(self):
        constraints = [{
            "verb.id": "testverb1"
        }]
        avg_lat = um.get_user_average_latency("0", "0", *constraints)
        print(avg_lat)

    def tearDown(self):
        pass


class UserModelEndpointsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        idi.app.testing = True

    def setUp(self):
        self.app = idi.app.test_client()
        mock_con = mongomock.MongoClient()
        um.con = mock_con
        pdt.populate_xapi_model(mock_con)

    def test_get_user_model_for_course(self):
        print("user")
        response = self.app.get("/users/model/0/2")
        user_model = json.loads(response.data)
        print(user_model)

    def test_get_all_courses(self):
        print("courses")
        response = self.app.get("/users/courses")
        print(response.data)
        courses = json.loads(response.data)["courses"]
        print(courses)
        self.assertEqual(set(courses), {"0", "1"})

    def test_get_users(self):
        print("users")
        response = self.app.get("users/")
        print(response.data)

    def test_get_user_times(self):
        print("times:")
        response = self.app.get("users/times/0/0")
        print(response.data)

    def test_avg_latency(self):
        print("avg_latency")
        response = self.app.get("/users/avg_latency/0/0")
        print(response.data)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
