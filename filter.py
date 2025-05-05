import json

def remove_tags_from_json(input_file, output_file, tags_to_remove):
    # Read the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Recursive function to remove tags from nested structures
    def remove_tags(data):
        if isinstance(data, dict):
            # Remove keys (tags) if they're in the list of tags to remove
            return {key: remove_tags(value) for key, value in data.items() if key not in tags_to_remove}
        elif isinstance(data, list):
            # Process list elements (recursive)
            return [remove_tags(item) for item in data]
        else:
            # Base case: just return the data
            return data

    # Remove the specified tags from the data
    modified_data = remove_tags(data)

    # Write the modified data back to a new file with proper indentation
    with open(output_file, 'w') as f:
        json.dump(modified_data, f, indent=2)


# Example usage:
tags_to_remove = ['hyperlinkC', 'hyperlinkS', 'locEndNameC', 'hyperlinkE', 'locStartNameS', 'locEndNameS', 'stopNameS', 'stopNameC', 'locStartNameC', 'routeNameC', 'routeNameS', 'fullFare', 'serviceMode', 'journeyTime']  # Specify the tags you want to remove
input_file = 'base_.json' # _ is there to stop me from doing this accidentally
output_file = 'output.json'
remove_tags_from_json(input_file, output_file, tags_to_remove)
