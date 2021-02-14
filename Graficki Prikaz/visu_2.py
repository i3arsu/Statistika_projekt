import os 
import geopandas as gp
from geopandas import GeoSeries
import pandas as pd
import geoplot
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
#source https://ourworldindata.org/coronavirus-source-data
zaraz=pd.read_csv(os.getcwd()+"\\owid-covid-data.csv")
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
