import folium
map = folium.Map(location = [80,-100], zoom_start=6, tiles= "Mapbox Bright")

#adding markers - 1
map.add_child(folium.Marker(location = [80,-100],
                            popup = "Marker popup",
                            icon = folium.Icon(color = "green")))

#adding markers - 2 Preferred
feature_grp = folium.FeatureGroup("My Maps")
feature_grp.add_child(folium.Marker(location = [5,-105],
                            popup = "Marker popup",
                            icon = folium.Icon(color = "red")))
map.add_child(feature_grp)

map.save("map1.html")
