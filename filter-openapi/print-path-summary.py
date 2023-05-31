import json

with open('admin-api.json') as f:
    openapi_dict = json.load(f)

with open('path-summary.txt', 'w') as f:
    paths = openapi_dict['paths']
    for path_name, path_obj in paths.items():
        f.write(f"Path: {path_name}\n")
        for method_name, method_obj in path_obj.items():
            if 'summary' in method_obj:
                f.write(f"  {method_name}: {method_obj['summary']}\n")
            else:
                f.write(f"  {method_name}: No summary provided\n")
        f.write('\n')

### Output format
#
# Path: /admin/routes
#   get: Get All Routes
#   post: Create Route
#
# Path: /admin/routes/{id}
#   put: Create Route by ID
#   get: Get Route by ID
#   patch: Update Route
#   delete: Delete Route by ID
