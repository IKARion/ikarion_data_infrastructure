import os
import ikarion_data_management.ikarion_data_infrastructure as ik
import unittest
import mongomock
import ikarion_data_management.data_access_layer as da


class LogReceiverTestCase(unittest.TestCase):
    def setUp(self):
        ik.app.testing = True
        self.app = ik.app.test_client()
        with ik.app.app_context():
            ik.init_db()

        mock_con = mongomock.MongoClient()
        da.modelDBConnection

    def tearDown(self):
        pass


test_statement = {
    "object": {
        "definition": {
            "name": {
                "en-US": "File"
            },
            "extensions": {
                "http://collide.info/xapi/gitAction": {
                    "type": "http://activitystrea.ms/schema/1.0/file",
                    "added_lines": "1",
                    "deleted_lines": "0",
                    "name": "gitExtension",
                    "fileURL": "IKARion_data_infrastructure.xml"
                }
            }
        },
        "id": "https://github.com/IKARion/ikarion_data_infrastructure/IKARion_data_infrastructure.xml",
        "objectType": "Activity"
    },
    "timestamp": "2018-01-19T08:35:25.000Z",
    "actor": {
        "mbox": "mailto:hecking@collide.info",
        "objectType": "Agent",
        "name": "hecking"
    },
    "verb": {
        "id": "http://activitystrea.ms/schema/1.0/add",
        "display": {
            "en-US": "added"
        }
    },
    "context": {
        "extensions": {
            "http://collide.info/xapi/commit_data": {
                "commit_hash": "d716320ae2c5c8bacb93dd08bf9a28c6b516b0e3",
                "repository": "https://github.com/IKARion/ikarion_data_infrastructure/",
                "commit_message": "Added IKARion_data_infrastructure.xml",
                "name": "Commit Data",
                "type": "http://collide.info/xapi/commit_data"
            }
        }
    },
    "id": "a821d55d-43f3-43f6-b90d-82dc815202c4",
    "stored": "2018-02-01T16:26:28.498Z",
    "authority": {
        "mbox": "mailto:hello@learninglocker.net",
        "name": "New Client",
        "objectType": "Agent"
    },
    "version": "1.0.0"
}

if __name__ == '__main__':
    unittest.main()