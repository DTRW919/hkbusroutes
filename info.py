import json

aList = []

file = open("data/output.json")
fileData = file.read()
fileObject = json.loads(fileData)

for i in range(len(fileObject["features"])):
    if fileObject["features"][i]["properties"]["routeNameE"] not in aList:
        aList.append(fileObject["features"][i]["properties"]["routeNameE"])

aList.sort()
print(*aList, sep = "\n")
print(len(aList))
