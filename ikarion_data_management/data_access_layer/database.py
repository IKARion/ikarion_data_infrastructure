import ikarion_data_management.ikarion_data_infrastructure as idi
from neo4j import GraphDatabase, Session


def execute_query(query, parameters):
    print(query)
    print(parameters)
    conf = idi.app.config
    driver = GraphDatabase.driver(conf["NEO4J_URI"], auth=(conf["NEO4J_USER"], conf["NEO4J_PW"]))

    with driver.session() as session:
        session: Session
        results = session.run(query, parameters)
        record_list = list(results.records())

    return record_list