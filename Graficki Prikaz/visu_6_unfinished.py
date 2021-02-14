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
dataframe = pd.read_csv(os.getcwd()+"\\swine_flu_732.csv",sep=',',engine='python',error_bad_lines=False)
#dataframe =dataframe[dataframe["Country"] & dataframe['Deaths'] & dataframe['Cases'] & (dataframe['Update Time']=='7/3/2009 9:00')]


print(world)
print(dataframe)
#spajamo dva dataseta

world = world.merge(dataframe,how='outer',on='name')

#fig,ax = plt.subplots()
#divider = make_axes_locatable(ax)
#cax = divider.append_axes("right",size="30%" ,pad=0.8)

world.plot(column='Deaths',legend=True,figsize=(15, 10),cmap='OrRd',facecolor='lightgray')
