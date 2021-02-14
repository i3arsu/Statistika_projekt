import folium
import pandas as pd
from os import getcwd

#Importamo datasetove
data1 = pd.read_csv (getcwd()+'/owid-covid-data.csv')
df1 = pd.DataFrame(data1, columns = ['iso_code', 'continent', 'new_cases','population'])
data2 = pd.read_csv(getcwd()+'/country_centroids_az8.csv')
df2 = pd.DataFrame(data2, columns = ['iso_a3', 'Longitude', 'Latitude'])
#Spajamo oba dataseta tako da saznamo koordinate drzava
result = pd.merge(left = df1, right = df2, left_on = 'iso_code', right_on = 'iso_a3')
result_fin = result.groupby(["iso_code"])
result_fin = result_fin["new_cases"].sum()/result_fin["population"].mean()*100
print(result_fin)

geo_json = getcwd()+'/countries.geojson'

f_map = folium.Map(location=[49.372, 11.023],
                            zoom_start=5,)

folium.Choropleth(
    geo_data=geo_json,
    data=result_fin,#pd.DataFrame(data = [result_fin.keys(),result_fin.values] ).T,
    #columns=[0,1],
    key_on="feature.properties.ISO_A3",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="Infection %",
).add_to(f_map)

f_map.save("Sitemap_covid19.html")

# TODO:
# Pocistiti dataset
