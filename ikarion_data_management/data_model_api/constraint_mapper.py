

KEY_MAPPING = {

}

def map_constraints(request):
    if request.is_json:
        constraints = request.get_json()
        mapped_constraints = []
        for key, value in constraints.items():
            mapped_constraints.append({KEY_MAPPING[key]: value})
        return mapped_constraints
    else:
        return []
