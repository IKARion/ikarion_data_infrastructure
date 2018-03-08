import os
import ikarion_data_management.ikarion_data_infrastructure as ik
import unittest
import mongomock
from test.model_db_access_layer import user_model_test_data as umd
from ikarion_data_management.data_access_layer.model_db_access_layer import user_model_dao as um

ITEM_NUMBER = 5

class UserModelDAOTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        mock_con = mongomock.MongoClient()
        um.con = mock_con
        for i in range(ITEM_NUMBER):
            test_user = umd.fill_user_model(i, i, list(range(i)), ITEM_NUMBER)
            mock_con.db.usermodels.insert_one(test_user)
    def setUp(self):
        pass

    def test_getAllCourses(self):
        courses = um.get_all_courses()
        expected_result = [str(i) for i in range(ITEM_NUMBER)]
        self.assertEqual(set(courses), set(expected_result))

    def test_getAllUsers(self):
        users = um.get_all_users()
        expected_result = [str(i) for i in range(ITEM_NUMBER)]
        self.assertEqual(set(users), set(expected_result))

    def test_getAllUsersForCourse(self):
        users = um.get_all_users_for_course("1")
        user = users[0]
        expected = {"uid": "1"}
        # To compare dict subset relation you can use items() and <=
        self.assertLessEqual(expected.items(), user.items())

    def test_getAllCoursesForUser(self):
        users = um.get_all_courses_for_user("1")
        user = users[0]
        expected = {"course": "1"}
        # To compare dict subset relation you can use items() and <=
        self.assertLessEqual(expected.items(), user.items())

    def test_getUserModel(self):
        user = um.getUserModel("1", "1")

        expected = {"uid": "1", "course": "1"}
        self.assertLessEqual(expected.items(), user.items())

    def test_getUserModelsForCourse(self):
        users = um.getUserModelsForCourse("1")
        user = users[0]

        expected = {"uid": "1", "course": "1"}
        self.assertLessEqual(expected.items(), user.items())

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
