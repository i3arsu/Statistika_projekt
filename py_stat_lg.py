import os 
import geopandas as gp
from geopandas import GeoSeries
import pandas as pd
import geoplot
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

#učitamo basic mapu i države
cities = gp.read_file(gp.datasets.get_path('naturalearth_cities'))
world = gp.read_file(gp.datasets.get_path('naturalearth_lowres'))

#izbacimo države bez stanovnika
world = world[(world.pop_est>0) & (world.name!="Antarctica")]

#učitamo dataset koji sadržava podatke o korona virusu (updated 03.02.2021)
#source https://coronavirus.jhu.edu/data/mortality
dataframe = pd.read_csv(os.getcwd()+"\\Bolesti\\covid_death_data.csv",sep=None,engine='python')

#spajamo dva dataseta
dataframe=dataframe.rename(columns={'COUNTRY':'name'})
world = world.merge(dataframe,how='right',on='name')

#fig, ax = plt.subplots()
#divider = make_axes_locatable(ax)
#cax = divider.append_axes("bottom", size="20%", pad=0.8)
world.plot(column='CASE-FATALITY',legend=True,figsize=(15, 10),cmap='OrRd',facecolor='lightgray')




#2
#source https://ourworldindata.org/coronavirus-source-data
zaraz=pd.read_csv(os.getcwd()+"\\Bolesti\\covid_data.csv")
plt.figure();

#input države i tipa podataka
drzava=input()
print("total_cases,new_cases,total_deaths,new_deaths,total_cases_per_million,total_deaths_per_million,")
tip=input()

#singleoutamo hrvatsku i podatke koje zelimo
zaraz=zaraz[(zaraz["location"]==drzava) & zaraz[tip] & zaraz['date']]

#da pokazuje samo podatke koje zelimo bez croatia NaN
zaraz = pd.DataFrame(zaraz,columns=[tip,'date'])
print(zaraz)

#pretvaramo date u datetime za svaki slučaj
zaraz['date'] = pd.to_datetime(zaraz['date'])

#line plot
zaraz.plot(x ='date', y=tip, kind = 'line')
zaraz.set_index('date', inplace = True)
zaraz.resample('1M').count()[tip].plot(x ='date', y=tip, kind = 'line')


#3
#double comparative
zaraz2=pd.read_csv(os.getcwd()+"\\Bolesti\\covid_data.csv")
plt.figure();
drzava1=input()
drzava2=input()
print("total_cases,new_cases,total_deaths,new_deaths,total_cases_per_million,total_deaths_per_million,")
tip=input()


zaraz2_1=zaraz2[(zaraz2['location']==drzava1) & zaraz2[tip] & zaraz2['date']]
zaraz2_2=zaraz2[(zaraz2['location']==drzava2) & zaraz2[tip] & zaraz2['date']]



zaraz2 = pd.DataFrame(zaraz2,columns=[tip,'date'])



#line plot
ax = plt.gca()

zaraz2_1.plot(x ='date', y=tip, kind = 'line', ax=ax)
zaraz2_2.plot(x= 'date', y=tip,color='red', kind='line', ax=ax)


#4-komparacija između dvaju drzava na jednoj variabli
zaraz=pd.read_csv(os.getcwd()+"\\Bolesti\\covid_data.csv")

#input države i tipova podataka
drzava=input()
print("total_cases,new_cases,total_deaths,new_deaths,total_cases_per_million,total_deaths_per_million,")
tip1=input()
tip2=input()


zaraz=zaraz[(zaraz["location"]==drzava) & zaraz[tip1] & zaraz[tip2] & zaraz['date']]


ax = plt.gca()
#pretvaramo date u datetime za svaki slučaj
zaraz['date'] = pd.to_datetime(zaraz['date'])

#dupli line plot
zaraz.plot(x ='date', y=tip1, kind = 'line', ax=ax)
zaraz.plot(x= 'date', y=tip2,color='red', kind='line', ax=ax)
zaraz.set_index('date', inplace = True)


