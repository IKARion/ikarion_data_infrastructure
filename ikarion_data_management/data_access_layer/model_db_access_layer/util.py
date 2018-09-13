# Fields
RES_USED_LIST = 'resources_list'
RES_USED_FIELD = 'resource_accesses'
DISTINCT_RES_USED = 'distinct_resource_accesses'


#course_schema = "context.extensions.courseid"
group_schema = "context.groups.id"
task_schema = "relevant_group_task.task.task_id"
artefact_schema = "object.id"
artefact_type_schema = "object.definition.type"
#artefact_
user_schema = "actor.name"
time_stamp_schema = "timestamp"
action_schema = "verb.id"
verb_schema = "verb.id"
repository_schema = "context.extensions.repository"
object_content_schema = "object.definition.extensions.message"

def merge_query(*args):
    merged_query = {

    }
    for arg in args:
        merged_query.update(arg)

    return merged_query