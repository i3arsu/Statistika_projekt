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

def plot_results(result_fin):
    folium_map = folium.Map(location=[49.372, 11.023],
                            zoom_start=5,
                            tiles="CartoDB dark_matter")
                                            

    for country, case_sum in result_fin.iteritems():
        if country[0] == 'HKG':
            continue # no data

        popup = folium.Popup(folium.IFrame(country[0]+': '+str(round(case_sum*100,2))+ ' %', width=130, height=34), max_width=500)
        
        radius = case_sum*250
        
        folium.CircleMarker(location=(country[3],
                                      country[2]),
                            radius=radius,
                            popup=popup,
                            fill=True).add_to(folium_map)
    return folium_map

#f_map = plot_results(result_fin)


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

f_map.save("index.html")

# TODO:
# Pocistiti dataset
