import folium
import json

map = folium.Map(
            prefer_canvas = True,
            tiles = "Cartodb Voyager",
            zoom_start = 12,
            min_zoom = 12,
            max_zoom = 20,
            location = [22.345064, 114.190009]
                )

file = open("data/output.json")
fileData = file.read()
fileObject = json.loads(fileData)

def plotDot(lat, lon, color, name):
    folium.CircleMarker(
                    location = [lat, lon],
                    radius = 5,
                    weight = 2,
                    color = color,
                    tooltip = name
                       ).add_to(map)

for i in range(len(fileObject["features"])):
    lat = fileObject["features"][i]["geometry"]["coordinates"][1]
    lon = fileObject["features"][i]["geometry"]["coordinates"][0]
    color = ""

    routeName = fileObject["features"][i]["properties"]["routeNameE"]

    if routeName[0:3] == "E36":
        plotDot(lat, lon, "red", fileObject["features"][i]["properties"]["routeNameE"])
    if routeName[0:3] == "272":
        plotDot(lat, lon, "orange", fileObject["features"][i]["properties"]["routeNameE"])
    if routeName[0:3] == "907":
        plotDot(lat, lon, "blue", fileObject["features"][i]["properties"]["routeNameE"])
    if routeName[0:3] == "798":
        plotDot(lat, lon, "pink", fileObject["features"][i]["properties"]["routeNameE"])
    if routeName[0:2] == "40":
        plotDot(lat, lon, "green", fileObject["features"][i]["properties"]["routeNameE"])
    if routeName[0:2] == "51" and len(routeName) == 2:
        plotDot(lat, lon, "yellow", fileObject["features"][i]["properties"]["routeNameE"])
    if routeName[0:2] == "81":
        plotDot(lat, lon, "purple", fileObject["features"][i]["properties"]["routeNameE"])

map.save("map.html")
