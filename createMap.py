import folium, json, os

map = folium.Map(
    prefer_canvas = True,
    tiles = "Cartodb Voyager",
    zoom_start = 12,
    min_zoom = 11,
    location = [22.345064, 114.190009]
    )

route1 = folium.FeatureGroup(name = "1", show = False).add_to(map)
route2 = folium.FeatureGroup(name = "2", show = False).add_to(map)
route3 = folium.FeatureGroup(name = "3", show = False).add_to(map)
route4 = folium.FeatureGroup(name = "4", show = False).add_to(map)
route5 = folium.FeatureGroup(name = "5", show = False).add_to(map)
route6 = folium.FeatureGroup(name = "6", show = False).add_to(map)
route7 = folium.FeatureGroup(name = "7", show = False).add_to(map)
route8 = folium.FeatureGroup(name = "8", show = False).add_to(map)
route9 = folium.FeatureGroup(name = "9", show = False).add_to(map)
routeX = folium.FeatureGroup(name = "Other", show = False).add_to(map)

folium.LayerControl().add_to(map)

file = open("data/output.json")
fileData = file.read()
fileObject = json.loads(fileData)

def plotLine(lat1, lon1, lat2, lon2, color, name, layer):
    folium.CircleMarker(
        location = [lat1, lon1],
        radius = 2,
        weight = 1,
        color = color
    ).add_to(layer)

    folium.PolyLine(
        locations = [[lat1, lon1], [lat2, lon2]],
        weight = 2,
        color = color,
        tooltip = name
    ).add_to(layer)

def setData(name, type):
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
    layers = [
        route1,
        route2,
        route3,
        route4,
        route5,
        route6,
        route7,
        route8,
        route9,
    ]

    strippedName = ''.join(char for char in name if char.isdigit())

    if not strippedName:
        if type == "color":
            return "black"
        elif type == "layer":
            return routeX
    else:
        if type == "color":
            return colors[int(strippedName[-1]) - 1]
        elif type == "layer":
            return layers[int(strippedName[0]) - 1]

for i in range(len(fileObject["features"]) - 1):
    lat1 = fileObject["features"][i]["geometry"]["coordinates"][1]
    lon1 = fileObject["features"][i]["geometry"]["coordinates"][0]
    lat2 = fileObject["features"][i + 1]["geometry"]["coordinates"][1]
    lon2 = fileObject["features"][i + 1]["geometry"]["coordinates"][0]

    if fileObject["features"][i]["properties"]["routeNameE"] == fileObject["features"][i + 1]["properties"]["routeNameE"]:
        if abs(lat2 - lat1) <= 0.05 and abs(lon2 - lon1) <= 0.05:
            if fileObject["features"][i + 1]["properties"]["stopSeq"] - fileObject["features"][i]["properties"]["stopSeq"] == 1:
                plotLine(
                    lat1, lon1,
                    lat2, lon2,
                    setData(fileObject["features"][i]["properties"]["routeNameE"], "color"),
                    fileObject["features"][i]["properties"]["routeNameE"],
                    setData(fileObject["features"][i]["properties"]["routeNameE"], "layer")
                )

subfolder = "output"
filename = "map.html"
full_path = os.path.join(subfolder, filename)
os.makedirs(subfolder, exist_ok = True)

map.save(full_path)
