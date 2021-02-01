import folium
import pandas as pd


#Importamo datasetove
data1 = pd.read_csv (r'/home/i3arsu/Desktop/Statistika_projekt/Statistika_projekt/Simulacija/Sitemap/owid-covid-data.csv')
df1 = pd.DataFrame(data1, columns = ['iso_code', 'continent', 'total_cases','population'])
data2 = pd.read_csv(r'/home/i3arsu/Desktop/Statistika_projekt/Statistika_projekt/Simulacija/Sitemap/country_centroids_az8.csv')
df2 = pd.DataFrame(data2, columns = ['brk_a3', 'Longitude', 'Latitude'])
#Spajamo oba dataseta tako da saznamo koordinate drzava
result = pd.merge(left = df1, right = df2, left_on = 'iso_code', right_on = 'brk_a3')
result_fin = result.groupby(["iso_code",'continent',"Longitude", "Latitude"])["total_cases"].count()
print(result_fin)

def get_data()


def plot_results(result_fin):
    # generate a new map
    folium_map = folium.Map(location=[49.372, 11.023],
                            zoom_start=5,
                            tiles="CartoDB dark_matter",
                            width='50%')

    # for each row in the data, add a cicle marker
    for index, row in result_fin.iterrows():
        s
        # generate the popup message that is shown on click.
        # popup_text = "{}<br> total departures: {}<br> total arrivals: {}<br> net departures: {}"
        # popup_text = popup_text.format(row["Start Station Name"],
        #                   row["Arrival Count"],
        #                   row["Departure Count"],
        #                   net_departures)
        
        # radius of circles
        radius = 10
        
        # add marker to the map
        folium.CircleMarker(location=(row["Latitude"],
                                      row["Longitude"]),
                            radius=radius,
                            color=color,
                            popup=popup_text,
                            fill=True).add_to(folium_map)
    return folium_map
plot_results(result_fin)
folium_map.save("index.html")


#Napraviti da crta krugove
#Pocistiti malo dataset