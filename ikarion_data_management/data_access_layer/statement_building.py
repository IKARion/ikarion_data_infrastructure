from itertools import permutations
from .query_util import *


# turn property dict into valid cypher properties
def cypherize_properties(prop):
    kv_template = "{}:{}"
    kv_list = []
    for key, value in prop.items():
        kv_list.append(kv_template.format(key, "\"" + value + "\""))

    return "{" + ",".join(kv_list) + "}"


def match_node_query(node: str, node_type, properties: dict = None):
    if properties is None:
        template = "({}:{})"
        node_query = template.format(node, node_type)
    else:
        template = "({}:{}{})"
        node_query = template.format(node, node_type, properties)
    return node_query


def match_relation_query(node_a, node_b, relation_type=None):
    if relation_type is None:
        relation_type = ""
    else:
        relation_type = ":" + relation_type
    template = "({})-[{}]-({})"

    relation_query = template.format(node_a, relation_type, node_b)
    return relation_query


def build_relation_query(nodes, relation_model):
    match_relation_list = []
    for node_a, node_b in permutations(nodes, 2):
        if (node_a, node_b) in relation_model:
            r_q = match_relation_query(node_a, node_b)
            match_relation_list.append(r_q)
    return match_relation_list


def build_query(constraints, targets, relation_model):
    constraint_dict = {}
    for key, value in constraints.items():
        c_type, c_property = key.split("_")
        if c_type not in constraint_dict:
            constraint_dict[c_type] = {}
        constraint_dict[c_type][c_property] = value

    target_node_set = set()
    for t_val in targets:
        if "_" in t_val:
            t_type, t_property = t_val.split("_")
            target_node_set.add(t_type)
        else:
            target_node_set.add(t_val)
    target_node_list = list(target_node_set)

    node_list_c = [(node, node.capitalize(), properties) for node, properties in constraint_dict.items()]
    nodes_only_c = [item[0] for item in node_list_c]

    # only add nodes from target list if not already part of constraint node list
    # avoids duplication
    node_list_t = [(node, node.capitalize(), None)
                   for node in target_node_list
                   if node not in nodes_only_c]

    node_list = node_list_c + node_list_t
    nodes_only = [item[0] for item in node_list]

    match_node_list = [match_node_query(node, node_type, properties)
                       for node, node_type, properties
                       in node_list]

    match_relation_list = build_relation_query(nodes_only, relation_model)

    query_template = "MATCH \n{} \nRETURN {}"

    match_string = ",\n".join(match_node_list + match_relation_list)
    return_string = ",".join(targets)
    query = query_template.format(match_string, return_string)

    return query


def build_query_parameterized(constraints, targets, relation_model):
    constraint_set = set()
    for key, value in constraints.items():
        c_type, c_property = key.split("_")
        constraint_set.add(c_type)

    target_node_set = set()
    for t_val in targets:
        if "_" in t_val:
            t_type, t_property = t_val.split("_")
            target_node_set.add(t_type)
        else:
            target_node_set.add(t_val)
    target_node_set

    node_list = list(constraint_set.union(target_node_set))

    match_node_list = [match_node_query(node, node.capitalize())
                       for node
                       in node_list]

    match_relation_list = build_relation_query(node_list, relation_model)

    where_list = ["{} = {}".format(key, "$`" + key + "`") for key in constraints.keys()]
    where_string = " AND\n".join(where_list)

    query_template = "MATCH \n{} \nWHERE\n{} \nRETURN {}"

    match_string = " ,\n".join(match_node_list + match_relation_list)
    return_string = " ,".join(targets)
    query = query_template.format(match_string, where_string, return_string)
    return query


# def build_action_insert_statement(properties, relation_model, key_mapping:OrderedDict):
#     node_merge_list = []
#     for k, v in key_mapping:
#         prop = properties[k]
#         node_merge_statement = "MERGE ({}:{} {})\n".format(k, k.capitalize(), "$" + k)
#         node_merge_list.append(node_merge_statement)
#
#     relation_merge_list = []
#     relation_merge_template = "MERGE ({})-[]-({})"
#     nodes = list(properties.keys())
#     for node_a, node_b in permutations(nodes, 2):
#         if (node_a, node_b) in relation_model:
#             relation_merge_statement = relation_merge_template.format(node_a, node_b)
#             relation_merge_list.append(relation_merge_statement)
#
#     merge_list = node_merge_list + relation_merge_list
#     merge_statement = "\n".join(merge_list)
#     return merge_statement

def build_action_insert_statement(properties,
                                  group_tasks,
                                  action_extras,
                                  relevant_task,
                                  key_mapping: OrderedDict):
    """
    Builds a cypher statement to insert all relevant information of a moodle action
    into the database.
    :param properties:  dictionary of entities and their properties.
    Containing moodle, course, user, action, and possible content.
    :type properties: dict
    :param group_tasks: Since there are multiple groups with related tasks.
    Contains tuples of groups and tasks
    these need to be handled extra.
    :type group_tasks: list
    :param action_extras: Extra Nodes attached to action like content or selfassessment data.
    :type action_extras:
    :param key_mapping: dict that gives back the identifying key property of each entity.
    Ex.: "course" -> "id", "moodle" -> "url.
    This and the relation to other entities uniquely identifies a node
    :type key_mapping: dict
    :return: Returns a statement that adds all relevant entities and their connections
    to the database. Those include moodle, course, user, action, object, group, task, content
    :rtype: str
    """
    parameters = {}
    # add the properties which contain all the key/value pairs
    # for the base insert statement
    parameters.update(properties)

    # Add key parameters for base insert statement
    for k, v in properties.items():
        print(k)
        print(v)
        # Get the field that is the identifying key for the entity. Ex. id for course
        key = key_mapping[k]
        # parameter name for insertion into cypher statement. Ex. "course.id"
        p_name = k + "_" + key
        print(k)
        print(v)
        p_value = v[key]
        parameters[p_name] = p_value

    # Connections from the groups to their course and tasks need to be established
    group_course_queries = []
    task_course_queries = []
    group_task_queries = []
    group_member_queries = []
    task_resource_queries = []

    group_key = key_mapping["group"]
    task_key = key_mapping["task"]

    # tuple format = ({"id": group_id}, task, group_members)

    for i, (group, task, task_resources, group_members) in enumerate(group_tasks):
        # create unique identifiers for statement parameters for each group
        group_name = str(i)
        group_properties_name = "group_properties_" + str(i)
        group_key_prop_name = "group_id_" + str(i)
        group_key_value = group[group_key]

        # Create group to course sub statement
        group_course_query = group_course_query_template.format(
            group_name,
            group_key_prop_name,
            group_name,
            group_properties_name,
            group_name,
            group_properties_name,
        )
        group_course_queries.append(group_course_query)
        parameters[group_key_prop_name] = group_key_value
        parameters[group_properties_name] = group

        # Create group to task sub statement
        task_name = str(i)
        task_key_prop_name = "task_id_" + str(i)
        task_properties_name = "task_properties_" + str(i)
        task_key_value = task[task_key]
        task_course_query = task_course_query_template.format(
            task_name,
            task_key_prop_name,
            task_name,
            task_properties_name,
            task_name,
            task_properties_name,
        )
        parameters[task_key_prop_name] = task_key_value
        parameters[task_properties_name] = task
        task_course_queries.append(task_course_query)

        group_task_query = group_task_query_template.format(group_name, task_name)
        group_task_queries.append(group_task_query)

        # add connection between task and artefacts

        for io, object_id in enumerate(task_resources):
            o_p_name = ("object{}_".format(io)) + task_name
            task_resource_q = task_resource_template.format(task_name, o_p_name)
            parameters[o_p_name] = object_id
            task_resource_queries.append(task_resource_q)

        # Need to check if group member is user
        # then change variable name for member
        # otherwise main user in statement gets duplicated
        user_id = parameters["user"]["id"]
        for im, member in enumerate(group_members):
            if member == user_id:
                member_name = "user"
                g_m_q = group_member_mainuser_template.format(member_name, group_name)
                member_course_q = group_member_course_template.format(member_name)
                member_moodle_q = group_member_moodle_template.format(member_name)
                group_member_queries.append(g_m_q)
                group_member_queries.append(member_course_q)
                group_member_queries.append(member_moodle_q)
            else:
                member_name = str(im) + "_" + str(group_name)
                member_key_prop_name = "member_name_" + member_name
                g_m_q = group_member_template.format(member_name, member_key_prop_name, group_name)
                parameters[member_key_prop_name] = member
                member_course_q = group_member_course_template.format(member_name)
                member_moodle_q = group_member_moodle_template.format(member_name)
                group_member_queries.append(g_m_q)
                group_member_queries.append(member_course_q)
                group_member_queries.append(member_moodle_q)

    # Add extra nodes connected to action
    # Used to model special things about an action like wiki content or selfassesment
    action_extra_statements = []
    for e_k, e_v in action_extras.items():
        extra_statements, extra_parameters = create_action_extra_statements(e_k, e_v)
        parameters.update(extra_parameters)
        action_extra_statements.extend(extra_statements)

    if relevant_task:
        task_id = relevant_task["task_id"]
        r_statement = [relevant_task_template.format(task_id)]
    else:
        r_statement = []

    query_statement_list = [
        [base_statement_insert_query],
        group_course_queries,
        task_course_queries,
        group_task_queries,
        group_member_queries,
        action_extra_statements,
        r_statement
    ]

    flat_list = [item for sub_l in query_statement_list for item in sub_l]
    query_string = "\n".join(flat_list)

    return query_statement_list, query_string, parameters


def create_action_extra_statements(e_key, e_values):
    statements = []
    parameters = {}
    if e_key == "content":
        content_vals = e_values["content_vals"]
        content_parameter_name = "content"
        c_p_l = [content_parameter_name] * 6
        content_statement = action_extra_template.format(content_parameter_name,
                                                         "Content",
                                                         *c_p_l)
        statements.append(content_statement)
        parameters[content_parameter_name] = content_vals

        concept_list = e_values["concepts"]

        for ic, concept in enumerate(concept_list):
            concept_parameter_name = "co_" + str(ic)
            concept_statement = content_concept_template.format(ic, concept_parameter_name)
            statements.append(concept_statement)
            parameters[concept_parameter_name] = concept
    elif e_key == "self_assessment":
        self_assessment_parameter_name = e_key
        s_a_l = [self_assessment_parameter_name] * 6
        self_assessment_statement = action_extra_template.format(self_assessment_parameter_name,
                                                                 "Self_Assessment",
                                                                 *s_a_l)
        parameters[self_assessment_parameter_name] = {}
        statements.append(self_assessment_statement)
        items = e_values
        for ii, item in enumerate(items):
            item_parameter_name = "item_" + str(ii)
            item_statement = self_assessment_items_template.format(str(ii),
                                                                   str(ii),
                                                                   item_parameter_name)
            statements.append(item_statement)
            parameters[item_parameter_name] = item

    return statements, parameters
