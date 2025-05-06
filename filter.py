import json

def removeTags(inputFile, outputFile, tags):
    with open(inputFile, "r") as f:
        data = json.load(f)

    # Recursive function to search for tags
    def remove_tags(data):
        if isinstance(data, dict):
            return {key: remove_tags(value) for key, value in data.items() if key not in tags}
        elif isinstance(data, list):
            return [remove_tags(item) for item in data]
        else:
            return data

    modified_data = remove_tags(data)

    with open(outputFile, "w") as f:
        json.dump(modified_data, f, indent=2)

# Actual usage; Put all unused tags in 'tags':
tags = ["hyperlinkC", "hyperlinkS", "locEndNameC", "hyperlinkE", "locStartNameS", "locEndNameS", "stopNameS", "stopNameC", "locStartNameC", "routeNameC", "routeNameS", "fullFare", "serviceMode", "journeyTime"]

inputFile = "base.json" # Base file
outputFile = "output.json" # Final file

removeTags(inputFile, outputFile, tags)
