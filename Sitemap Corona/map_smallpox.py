import folium
import pandas as pd
import numpy as np
from os import getcwd

#Importamo datasetove
data1 = pd.read_csv ('/home/i3arsu/Desktop/Statistika_projekt/Statistika_projekt/Sitemap Corona/number-of-reported-smallpox-cases.csv')
df1 = pd.DataFrame(data1, columns = ['Entity', 'Code', 'Cases'])
data2 = pd.read_csv('/home/i3arsu/Desktop/Statistika_projekt/Statistika_projekt/Sitemap Corona/country_centroids_az8.csv')
df2 = pd.DataFrame(data2, columns = ['name', 'Longitude', 'Latitude'])
#Spajamo oba dataseta tako da saznamo koordinate drzava
result = pd.merge(left = df1, right = df2, left_on = 'Entity', right_on = 'name')
result_fin = result.groupby(["Entity","Longitude", "Latitude"])#["new_cases_per_million"].sum()
result_fin = result_fin["Cases"].sum()
print(result_fin)

def plot_results(result_fin):
    folium_map = folium.Map(location=[49.372, 11.023],
                            zoom_start=5,
                            tiles="CartoDB dark_matter")
    
    s = 255/np.average(result_fin) # biggest data value to color
                                            

    for country, case_sum in result_fin.iteritems():
        if country[0] == 'HKG':
            continue # no data
        
        gb = 255-int((case_sum)*s) # map data to a color (shade of red)
        
        if gb < 0:
            gb = 0
            
        color = '#ff'+"{0:#0{1}x}".format(gb,4)[2:]*2

        popup = folium.Popup(folium.IFrame(country[0]+': '+str(case_sum), width=130, height=70), max_width=500)
        
        radius = 7
        
        folium.CircleMarker(location=(country[2],
                                      country[1]),
                            radius=radius,
                            popup=popup,
                            color=color,
                            fill=True).add_to(folium_map)
    return folium_map

f_map = plot_results(result_fin)
f_map.save("Sitemap_smallpox.html")

