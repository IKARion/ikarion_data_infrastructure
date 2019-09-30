from collections import OrderedDict

base_statement_insert_query = """
MERGE (moodle:Moodle{url: $moodle_url})
ON CREATE SET moodle = $moodle
ON MATCH SET moodle = $moodle 
MERGE (course:Course{id: $course_id})-[:PART_OF]->(moodle)
ON CREATE SET course = $course
ON MATCH SET course = $course
MERGE (user:User{id: $user_id})-[:HAS_ACCOUNT]->(moodle)
ON CREATE SET user = $user
ON MATCH SET user = $user
MERGE (user)-[:ENROLLED_IN]->(course)
MERGE (object:Object{id: $object_id})-[:PART_OF]->(course)
ON CREATE SET object = $object
ON MATCH SET object = $object
MERGE (action:Action{id: $action_id})-[:TAKEN_BY]->(user)
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

task_course_query_template = """MERGE (course)-[:IN]-(task{}:Task{{id: ${}}})
ON CREATE SET task{} = ${}
ON MATCH SET task{} = ${}
"""

# group_task_query_template = "MERGE (group:Group{{id: ${}}})-[:HAS_TASK]-(task)"
group_task_query_template = "MERGE (group{})-[:HAS_TASK]-(task{})"

# template for group members
group_member_template = "MERGE (member{}:User{{id: ${}}})-[:PART_OF]-(group{})"
group_member_mainuser_template = "MERGE ({})-[:PART_OF]-(group{})"

group_member_moodle_template = "MERGE (member{})-[:HAS_ACCOUNT]->(moodle)"
group_member_course_template = "MERGE (member{})-[:ENROLLED_IN]->(course)"

task_resource_template = "MERGE (task{})<-[:RESOURCE]-(object:Object{{id: ${}}})"



relevant_task_template = "MERGE (action)<-[:RELEVANT_TO]-(task{{id: ${}}})"

# action extra queries

action_extra_template = """
MERGE (action)-[:CONTAINS]->({}:{})
ON CREATE SET {} = ${}
ON MATCH SET {} = ${}
"""

#   content keywords

content_concept_template = """
MERGE (content:Content)-[:HAS_CONCEPT]->(co{}:Concept)
SET co{} = ${}
"""

#   Self Assessment

self_assessment_items_template = """
MERGE (self_assessment:Self_Assessment)-[:HAS_ITEM]->(item{}:Item)
set item{} = ${}
"""


key_mapping = OrderedDict([
    ("moodle", "url"),
    ("course", "id"),
    ("user", "id"),
    ("task", "id"),
    ("group", "id"),
    ("object", "id"),
    ("action", "id"),
])

entitiy_relations = {("moodle", "course"),
                     ("course", "group"),
                     ("course", "user"),
                     ("course", "object"),
                     ("course", "action"),
                     ("group", "user"),
                     ("group", "task"),
                     ("user", "action"),
                     ("object", "action"),
                     ("object", "task"),
                     ("action", "task")}
