import folium
map = folium.Map(location = [80,-100], zoom_start=6, tiles= "Mapbox Bright")

import pandas
vol = pandas.read_csv("Volcanoes.txt")


#adding markers - 1
# map.add_child(folium.Marker(location = [80,-100],
#                             popup = "Marker popup",
#                             icon = folium.Icon(color = "green")))

#adding markers - 2 Preferred
feature_grp = folium.FeatureGroup("Volcanoes")

def colorElev(elev):
    if elev < 1000:
        return 'red'
    elif 1000 <= elev <2000 :
        return 'green'
    else:
        return 'blue'

# feature_grp.add_child(folium.Marker(location = [lat,long],
#                         popup = str(elev),
#                         icon = folium.Icon(color = colorElev(int(elev)))))



for lat,long,elev in zip(list(vol["LAT"]), list(vol["LON"]), list(vol["ELEV"])):
    feature_grp.add_child(folium.CircleMarker(location = [lat,long],
                          radius = 3,
                          popup = str(elev)+" m",
                          fill_color = colorElev(int(elev)),
                          color = 'grey',
                          fill_opacity = 0.7))

feature_grp_2 = folium.FeatureGroup("Population")
feature_grp_2.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                      style_function = lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000
                      else "yellow" if x["properties"]["POP2005"] >= 10000000 else "red"}))


map.add_child(feature_grp)
map.add_child(feature_grp_2)

#always at the end to let festure group get showed
map.add_child(folium.LayerControl())

map.save("map1.html")
