import os 
import geopandas as gp
from geopandas import GeoSeries
import pandas as pd
import geoplot
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np


zaraz=pd.read_csv(os.getcwd()+"\\owid-covid-data.csv")

#input države i tipa podataka
drzava=input()
print("total_cases,new_cases,total_deaths,new_deaths,total_cases_per_million,total_deaths_per_million,")
tip1=input()
tip2=input()

#singleoutamo hrvatsku i podatke koje zelimo
zaraz=zaraz[(zaraz["location"]==drzava) & zaraz[tip1] & zaraz[tip2] & zaraz['date']]

ax = plt.gca()
#pretvaramo date u datetime za svaki slučaj
zaraz['date'] = pd.to_datetime(zaraz['date'])

#line plot
zaraz.plot(x ='date', y=tip1, kind = 'line', ax=ax)
zaraz.plot(x= 'date', y=tip2,color='red', kind='line', ax=ax)
zaraz.set_index('date', inplace = True)
