from collections import OrderedDict

statement_insert_query = """
MERGE (moodle:Moodle{name: $moodle.url}) 
MERGE (course:Course{id: $course.id})[:PART_OF]->(moodle)
MERGE (user:User{id: $user.id})-[:HAS_ACCOUNT]->(moodle)
MERGE (user)-[:ENROLLED_IN]->(course)
MERGE (object:Object{id: $object.id)-[:PART_OF]->(course)
MERGE (action:ACTION{id: $action.id)-[:TAKEN_BY]->(user)
MERGE (action)-[:TAKEN_IN]->(course)
MERGE (action)-[:TAKEN_ON]->(object)
"""

task_query = "MERGE (task:Task{id: $task.id}-[:PART_OF]->(course)"

object_task_query_template = "MERGE (object:OBJECT{{id: ${}}})-[:RELEVANT_TO]->(task)"

content_query = "MERGE (content:Content)-[:ADDED_BY]->(action)"

group_course_query_template = """MERGE (group{}:Group{{id: ${}}})-[:PART_OF]->(course)\n
ON CREATE SET group = ${}
ON MATCH SET group = ${}
"""
# group_task_query_template = "MERGE (group:Group{{id: ${}}})-[:HAS_TASK]-(task)"
group_task_query_template = "MERGE (group{})-[:HAS_TASK]-(task)"

action_extra_template = "CREATE (action)-[:CONTAINS]->({}) SET {} = ${}"



key_mapping = OrderedDict([
    ("moodle", "name"),
    ("course", "id"),
    ("user", "id"),
    ("task", "id"),
    ("group", "id"),
    ("obect", "id"),
    ("action", "verbid"),
])