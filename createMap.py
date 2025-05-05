import folium, json, os

map = folium.Map(
            prefer_canvas = True,
            tiles = "Cartodb Voyager",
            zoom_start = 12,
            min_zoom = 11,
            location = [22.345064, 114.190009]
                )

file = open("data/output.json")
fileData = file.read()
fileObject = json.loads(fileData)

def plotDot(lat, lon, color, name):
    folium.CircleMarker(
                    location = [lat, lon],
                    radius = 2,
                    weight = 1,
                    color = color,
                    tooltip = name
                       ).add_to(map)

def plotLine(lat1, lon1, lat2, lon2, color, name):
    folium.PolyLine(
                    locations = [[lat1, lon1], [lat2, lon2]],
                    weight = 2,
                    color = color,
                    tooltip = name
                       ).add_to(map)

def findColor(name):
    colors = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "purple",
        "pink",
        "darkred",
        "lightgreen",
        "darkblue"
             ]

    strippedName = ''.join(char for char in name if char.isdigit())

    if not strippedName:
        return "black"

    return colors[int(strippedName[0]) - 1]



for j in range(len(fileObject["features"]) - 1):
    lat1 = fileObject["features"][j]["geometry"]["coordinates"][1]
    lon1 = fileObject["features"][j]["geometry"]["coordinates"][0]
    lat2 = fileObject["features"][j + 1]["geometry"]["coordinates"][1]
    lon2 = fileObject["features"][j + 1]["geometry"]["coordinates"][0]

    if fileObject["features"][j]["properties"]["routeNameE"] == fileObject["features"][j + 1]["properties"]["routeNameE"]:
        if abs(lat2 - lat1) <= 0.05 and abs(lon2 - lon1) <= 0.05:
            if fileObject["features"][j + 1]["properties"]["stopSeq"] - fileObject["features"][j]["properties"]["stopSeq"] == 1:


                plotLine(lat1, lon1, lat2, lon2, findColor(fileObject["features"][j]["properties"]["routeNameE"]), fileObject["features"][j]["properties"]["routeNameE"])

subfolder = "output"
filename = "map.html"
full_path = os.path.join(subfolder, filename)

os.makedirs(subfolder, exist_ok = True)

map.save(full_path)
