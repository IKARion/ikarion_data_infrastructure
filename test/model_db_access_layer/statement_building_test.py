import unittest
from ikarion_data_management.data_access_layer.model_db_access_layer import statement_building as sb
from ikarion_data_management.data_access_layer.model_db_access_layer import query_util as qu


class BuildActionInsertStatementTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_insert(self):
        properties = {
            "course": {
                "id": 4
            },
            "object": {
                "id": 6
            },
            "user": {
                "id": "wargarbl"
            }
        }

        group_tasks = [
            ({"id": 3}, {"id": 5}),
            ({"id": 4}, {"id": 5}),
        ]

        action_extras = {
            "content": {"text": "abcdefg"}
        }

        s_list, param_dict = sb.build_action_insert_statement(properties,
                                                  group_tasks, action_extras,
                                                  qu.key_mapping)

        s_flat = [item for l in s_list for item in l]
        print("\n".join(s_flat))

    def test_tummy(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
