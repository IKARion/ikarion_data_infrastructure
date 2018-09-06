import unittest
import mongomock
import json

from ikarion_data_management import ikarion_data_infrastructure as idi
from ikarion_data_management.log_aggregator import log_receiver_endpoints as lre
from test.model_db_access_layer import populate_database_test_data as pdtd
from test.model_db_access_layer import user_model_test_data as umd


LOG_PRE = "/logs"

class LogReceiverTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        idi.app.testing = True

    def setUp(self):
        self.app = idi.app.test_client()
        mock_con = mongomock.MongoClient()
        lre.con = mock_con
        self.con = mock_con

    def test_process_log(self):
        lre.con = self.con
        statement_list = pdtd.generate_xapi_model(process=False)
        # statement = umd.generate_xapi_statement(user="test",
        #                                         course="test",
        #                                         time="2018-04-26T12:12:13.000Z",
        #                                         verb="test",
        #                                         artefact="test",
        #                                         group="3",
        #                                         process=False)
        for statement in statement_list:
            self.app.get(LOG_PRE+"/log_forwarding",
                         data=json.dumps(statement),
                         content_type='application/json')
        # self.app.get(LOG_PRE+"/log_forwarding",
        #              data=json.dumps(statement),
        #              content_type='application/json')

        db_statement_list = list(lre.con.db.xapi_statements.find({}))
        print(db_statement_list)
        print(len(db_statement_list))
        print(db_statement_list[0])
        groups = list(lre.con.db.groups.find({}))
        print(groups)

        tasks = list(lre.con.db.grouptasks.find({}))
        print(tasks)





