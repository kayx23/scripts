import json

def filter_json(data):
    """
    filter out items with name containing apifox.
    """
    if isinstance(data, dict):
        # If data is a dictionary
        filtered_data = {}
        for key, value in data.items():
            if 'apifox' not in key:
                filtered_data[key] = filter_json(value)
        return filtered_data
    elif isinstance(data, list):
        # If data is a list
        filtered_data = []
        for element in data:
            filtered_data.append(filter_json(element))
        return filtered_data
    else:
        return data
        
with open('open-api.json', 'r') as f:
    data = json.load(f)

filtered_data = filter_json(data)

with open('filtered_open-api.json', 'w') as f:
    json.dump(filtered_data, f, indent=2)

print('Filtered JSON saved to filtered_open-api.json')
