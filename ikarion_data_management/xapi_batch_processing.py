import pymongo

import ikarion_data_management.log_aggregator.statement_processing as sp
import ikarion_data_management.ikarion_data_infrastructure as idi
import requests


LRS_URL = "http://descartes.inf.uni-due.de:9001"
KEY = "b3f32910db630eacff743fcbb96e5111485e3d17"
SECRET = "c8783e809298c5e8d15630433a934ae026592d94"
XPERIENCE_API_VERSION = "1.0.3"

headers = {
    "X-Experience-API-Version": XPERIENCE_API_VERSION,
}


def batch_processing(dbname):
    client = pymongo.MongoClient(idi.MONGO_URI)
    more = True
    url = LRS_URL + "/data/xAPI/statements"
    count_statements = 0
    while more:
        print(url)
        get_request = requests.get(url, auth=(KEY, SECRET), headers=headers)
        request_json = get_request.json()
        statements = request_json["statements"]
        print("Processing Url: {}".format(url))
        print("Number of Statements:{}".format(len(statements)))
        proc_statements = []
        for statement in statements:
            try:
                sp.process_statement(statement)
                proc_statements.append(statement)
                # client[dbname].xapi_statements.insert_one(statement)
            except Exception as e:
                print(e)

        print("Number of Processed Statements:{}".format(len(proc_statements)))
        client[dbname].xapi_statements.insert_many(proc_statements)
        count_statements += len(proc_statements)

        more_url = request_json["more"]
        if more_url == "":
            more = False
        else:
            url = LRS_URL + more_url


if __name__ == "__main__":
    db_name = "db2"
    batch_processing(db_name)
