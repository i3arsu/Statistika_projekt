import os 
import geopandas as gp
from geopandas import GeoSeries
import pandas as pd
import geoplot
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np
#double comparative
zaraz2=pd.read_csv(os.getcwd()+"\\owid-covid-data.csv")
plt.figure();
drzava1=input()
drzava2=input()
print("total_cases,new_cases,total_deaths,new_deaths,total_cases_per_million,total_deaths_per_million,")
tip=input()

#singleoutamo hrvatsku i podatke koje zelimo
zaraz2_1=zaraz2[(zaraz2['location']==drzava1) & zaraz2[tip] & zaraz2['date']]
zaraz2_2=zaraz2[(zaraz2['location']==drzava2) & zaraz2[tip] & zaraz2['date']]


#da pokazuje samo podatke koje zelimo bez croatia NaN
zaraz2 = pd.DataFrame(zaraz2,columns=[tip,'date'])


#pretvaramo date u datetime za svaki slučaj


#line plot
ax = plt.gca()

zaraz2_1.plot(x ='date', y=tip, kind = 'line', ax=ax)
zaraz2_2.plot(x= 'date', y=tip,color='red', kind='line', ax=ax)
