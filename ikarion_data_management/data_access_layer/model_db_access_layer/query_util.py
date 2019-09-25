from collections import OrderedDict

base_statement_insert_query = """
MERGE (moodle:Moodle{name: $moodle.url})
ON CREATE SET moodle = $moodle
ON MATCH SET moodle = $moodle 
MERGE (course:Course{id: $course.id})[:PART_OF]->(moodle)
ON CREATE SET course = $course
ON MATCH SET course = $course
MERGE (user:User{id: $user.id})-[:HAS_ACCOUNT]->(moodle)
ON CREATE SET user = $user
ON MATCH SET user = $user
MERGE (user)-[:ENROLLED_IN]->(course)
MERGE (object:Object{id: $object.id)-[:PART_OF]->(course)
ON CREATE SET object = $object
ON MATCH SET object = $object
MERGE (action:ACTION{id: $action.id)-[:TAKEN_BY]->(user)
ON CREATE SET action = $action
ON MATCH SET action = $action
MERGE (action)-[:TAKEN_IN]->(course)
MERGE (action)-[:TAKEN_ON]->(object)
"""

task_query = "MERGE (task:Task{id: $task.id}-[:PART_OF]->(course)"

object_task_query_template = "MERGE (object:OBJECT{{id: ${}}})-[:RELEVANT_TO]->(task)"

content_query = "MERGE (content:Content)-[:ADDED_BY]->(action)"

group_course_query_template = """MERGE (group{}:Group{{id: ${}}})-[:PART_OF]->(course)\n
ON CREATE SET group{} = ${}
ON MATCH SET group{} = ${}
"""

task_course_query_template = """MERGE (course)-[:IN]-(task{}:TASK{{id: ${}}})
ON CREATE SET task{} = ${}
ON MATCH SET task{} = ${}
"""

# group_task_query_template = "MERGE (group:Group{{id: ${}}})-[:HAS_TASK]-(task)"
group_task_query_template = "MERGE (group{})-[:HAS_TASK]-(task{})"


# template for group members
group_member_template = "MERGE (member{}:User{{name: ${}}})-[:PART_OF]-(group{})"


action_extra_template = "CREATE (action)-[:CONTAINS]->({}:{}) SET {} = ${}"



key_mapping = OrderedDict([
    ("moodle", "url"),
    ("course", "id"),
    ("user", "name"),
    ("task", "id"),
    ("group", "id"),
    ("object", "id"),
    ("action", "verbid"),
])