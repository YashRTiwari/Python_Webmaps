import folium
map = folium.Map(location = [80,-100], zoom_start=6, tiles= "Mapbox Bright")

#adding markers
map.add_child(folium.Marker(location = [80,-100],
                            popup = "Marker popup",
                            icon = folium.Icon(color = "green")))

map.save("map1.html")
