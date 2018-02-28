from .. import modelDBConnection as con
import json

# Retrieve
def getLatencies(course, group, context):

    # get action sequence for corresponding course, group and context
    data = list(con.db.group_sequence.find({'course_id': course, 'group_id': group, 'context_id': context}))
    data = data[0]
    action_sequence = data['action_sequence']
    elem_count = len(action_sequence)
    overall_latency = 0
    all_latencies = list() # list of latencies between all activities

    for i in range(len(action_sequence)):
        if i == 0:
            # do nothing for first activity
            first_activity = action_sequence[i]['start']
        else:
            # calculate time between current and previous activity
            current = action_sequence[i]
            previous = action_sequence[i-1]
            latency = int(current['start']) - int(previous['start'])
            all_latencies.append(latency)
            overall_latency = overall_latency + latency

    # calculate average latency
    average_latency = round(overall_latency / (elem_count-1))

    return average_latency, all_latencies
