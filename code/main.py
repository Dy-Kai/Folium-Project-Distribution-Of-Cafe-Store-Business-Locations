import folium
import pandas as pd
from folium.plugins import *
from folium import *

# Deklarasi variabel map
mapObj = folium.Map(location=[0.5139625, 101.3711349], zoom_start=10)

# Deklarasi cluster
CafeCluster = MarkerCluster(name="Cafe").add_to(mapObj)
kampusCluster = MarkerCluster(name="Kampus").add_to(mapObj)

# Memasukkan data lokasi melalui script langsung
folium.Marker(location=[0.498805940159409, 101.41560805425205], popup="Universitas Muhammadiyah Riau", name="Universitas Muhammadiyah Riau", icon=folium.Icon(color="green", icon_color="yellow")).add_to(kampusCluster)

# Membaca file excel
dataDf = pd.read_excel('\spatial_data.xlsx')

# Memasukkan data dari file excel
for i in range(len(dataDf)):
    latVal = dataDf.iloc[i]["Latitude"]
    lonVal = dataDf.iloc[i]["Longitude"]
    nameVal = dataDf.iloc[i]["Nama Tempat"]
    # print(latVal, lonVal, NameVal)

    folium.Marker(location=[latVal, lonVal], popup=nameVal, name=nameVal, icon=folium.Icon(color="red", icon_color="white")).add_to(CafeCluster)

# Search bar
locationSearch = Search(layer=CafeCluster, search_label="name", placeholder='Cari Lokasi', collapsed=False, search_zoom=20).add_to(mapObj)

LayerControl().add_to(mapObj)

# Output map
mapObj.save("Map.html")