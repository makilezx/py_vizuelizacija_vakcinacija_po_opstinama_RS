import folium
import pandas as pd

map = folium.Map(location=[44.80401, 20.46513], zoom_start=10)
folium.TileLayer('cartodbpositron').add_to(map)

data = pd.DataFrame(
    {'lon': [20.516111, 20.532403, 20.425999, 20.693852, 18.560096, 20.502952, 20.475025, 20.464341, 20.355565, 20.262597, 20.203134, 20.263894, 20.385035, 20.262533, 20.451442, 20.452410, 20.380088],
     'lat': [44.811667, 44.776714, 44.395999, 44.436436, 54.441581, 44.671157, 44.799531, 44.818455, 44.853209, 44.791006, 44.662459, 44.379487, 44.683488, 44.442705, 44.782173, 44.603491, 44.809956],
     'name': ['Palilula', 'Zvezdara', 'Grocka', 'Mladenovac', 'Sopot', 'Vozdovac', 'Vracar', 'Stari Grad', 'Zemun', 'Surcin', 'Obrenovac', 'Lazarevac', 'Cukarica', 'Rakovica', 'Savski Venac', 'Barajevo', 'Novi Beograd'],
     'value': [54196, 58421, 22383, 12325, 5075, 59724, 26970, 22095, 56655, 12388, 16089, 12592, 60372, 38511, 16753, 7073, 86590]}, dtype=str)

for i, row in data.iterrows():
    folium.Circle(
        location = [row["lat"], row["lon"]],
        color="#69b3a2",
        fill=True,
        radius=float(data.iloc[i]['value'])/20,
        tooltip=folium.map.Tooltip(
        'Opstina ' + data.iloc[i]['name'] + ',' ' vakcinisano ' + data.iloc[i]['value'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"))
    ).add_to(map)
map