import json

with open('admin-api.json') as f:
    openapi_dict = json.load(f)

def print_path_summ_desc():
    with open('path-summary-desc.txt', 'w') as f:
        paths = openapi_dict['paths']
        for path_name, path_obj in paths.items():
            f.write(f"Path: {path_name}\n")
            for method_name, method_obj in path_obj.items():
                f.write(f"  {method_name}:\n")
                if 'summary' in method_obj:
                    f.write(f"    Summary: {method_obj['summary']}\n")
                else:
                    f.write(f"    Summary: No summary provided\n")
                if 'description' in method_obj:
                    f.write(f"    Description: {method_obj['description']}\n")
                else:
                    f.write(f"    Description: No description provided\n")
            f.write('\n')

def main():
    print_path_summ_desc()

if __name__ == '__main__':
    main()
    
### Output format

# Path: /admin/routes
#   get:
#     Summary: xxx
#     Description: xxx
#   post:
#     Summary: xxx
#     Description: xxx
#
# Path: /admin/routes/{id}
#   ...
