import json


def filter_leaf_categories(data):
    leaf_categories = []
    stack = data["Table"]

    while stack:
        category = stack.pop(0)
        if "Child" in category:
            stack.extend(category["Child"])
        else:
            leaf_categories.append(category)

    return {"Table": leaf_categories}


with open("NON_filtered_categories.json", "r", encoding="utf-8") as file:
    json_data = json.load(file)

filtered_data = filter_leaf_categories(json_data)

with open("filtered_categories.json", "w", encoding="utf-8") as output_file:
    json.dump(filtered_data, output_file, ensure_ascii=False, indent=2)
