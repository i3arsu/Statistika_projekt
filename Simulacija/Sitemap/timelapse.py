import folium
from folium.plugins import TimestampedGeoJson
import pandas as pd
from math import isnan
from datetime import datetime

data1 = pd.read_csv ('/home/i3arsu/Desktop/Statistika_projekt/Statistika_projekt/Simulacija/Sitemap/owid-covid-data.csv')
df1 = pd.DataFrame(data1, columns = ['iso_code', 'date', 'total_cases','population','continent'])

data2 = pd.read_csv('/home/i3arsu/Desktop/Statistika_projekt/Statistika_projekt/Simulacija/Sitemap/country_centroids_az8.csv')
df2 = pd.DataFrame(data2, columns = ['iso_a3', 'Longitude', 'Latitude','name'])
result = pd.merge(left = df1, right = df2, left_on = 'iso_code', right_on = 'iso_a3')

print(result)

def create_geojson_features(df):
    features = []
    
    feature = {
            'type': 'Feature',
            'geometry': {
                'type':'Point', 
                'coordinates':[0,0]
            },
            'properties': {
                'time': '2020-01-01',
                'style': {'color' : ''},
                'icon': 'circle',
                'iconstyle':{
                    'fillColor': '#000000',
                    'fillOpacity': 0.0,
                    'stroke': 'false',
                    'radius': 1
                }
            }
        } # to start from 1.1.2020.
    
    features.append(feature)
        
    s = 255/max((df['total_cases']/df['population'])) # biggest data value to color
    
    for _, row in df.iterrows():
        if isnan(row['total_cases']): #or row['continent'] != 'Europe':
            continue
        if datetime.fromisoformat(row['date']).timestamp()%604800 != 514800:
            continue

        gb = 255-int(((row['total_cases']/row['population']))*s) # map data to a color (shade of red)
        color = '#ff'+"{0:#0{1}x}".format(gb,4)[2:]*2
 
        feature = {
            'type': 'Feature',
            'geometry': {
                'type':'Point', 
                'coordinates':[row['Longitude'],row['Latitude']]
            },
            'properties': {
                'time': row['date'].__str__(),
                'style': {'color' : ''},
                'icon': 'circle',
                'popup': "Country:{name}<br>Population:{population}<br>Total Cases: {tcases}".format(name=row['name'], population = row['population'], tcases= row['total_cases']),
                'iconstyle':{
                    'fillColor': color,
                    'fillOpacity': 0.8,
                    'stroke': 'true',
                    'radius': 8
                }
            }
        }
        features.append(feature)
    return features

data_geojson = create_geojson_features(result)
folium_map = folium.Map(location=[49.372, 11.023],
                            zoom_start=5,
                            tiles="CartoDB dark_matter")

TimestampedGeoJson(data_geojson,
                  transition_time = 1000,
                   loop = False,
                   period = 'P7D').add_to(folium_map)
folium_map.save("timelapse.html")
