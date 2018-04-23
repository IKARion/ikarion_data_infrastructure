import ikarion_data_management.data_access_layer.model_db_access_layer.user_model_dao as umd

KEY_MAPPING = {
    "verb_id": umd.verb_schema,
    "user_id": umd.user_schema,
    "group_id": umd.group_schema,
    "timestamp": umd.time_stamp_schema,
}

def map_constraints(request):
    if request.is_json:
        constraints = request.get_json()
        mapped_constraints = []
        for key, value in constraints.items():
            if key in KEY_MAPPING:
                mapped_constraints.append({KEY_MAPPING[key]: value})
            else:
                mapped_constraints.append({key: value})
        return mapped_constraints
    else:
        return []
