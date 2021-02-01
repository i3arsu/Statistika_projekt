import folium
import pandas as pd


#Importamo datasetove
data1 = pd.read_csv (r'./owid-covid-data.csv')
df1 = pd.DataFrame(data1, columns = ['iso_code', 'continent', 'new_cases','population'])
data2 = pd.read_csv(r'./country_centroids_az8.csv')
df2 = pd.DataFrame(data2, columns = ['iso_a3', 'Longitude', 'Latitude'])
#Spajamo oba dataseta tako da saznamo koordinate drzava
result = pd.merge(left = df1, right = df2, left_on = 'iso_code', right_on = 'iso_a3')
result_fin = result.groupby(["iso_code",'continent',"Longitude", "Latitude"])["new_cases"].sum()
print(result_fin)


def plot_results(result_fin):
    # generate a new map
    folium_map = folium.Map(location=[49.372, 11.023],
                            zoom_start=5,
                            tiles="CartoDB dark_matter")
                                            
    # for each row in the data, add a cicle marker
    for country, case_sum in result_fin.iteritems():

        # generate the popup message that is shown on click.
        # popup_text = "{}<br> total departures: {}<br> total arrivals: {}<br> net departures: {}"
        # popup_text = popup_text.format(row["Start Station Name"],
        #                   row["Arrival Count"],
        #                   row["Departure Count"],
        #                   net_departures)

        popup = folium.Popup(folium.IFrame(country[0]+': '+str(case_sum), width=150, height=40), max_width=500)
        # radius of circles
        radius = case_sum/100_000
        
        # add marker to the map
        folium.CircleMarker(location=(country[3],
                                      country[2]),
                            radius=radius,
                            popup=popup,
                            fill=True).add_to(folium_map)
    return folium_map
f_map = plot_results(result_fin)

f_map.save("index.html")


#Napraviti da crta krugove
#Pocistiti malo dataset
