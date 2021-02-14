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
dataframe = pd.read_csv(os.getcwd()+"\\wrld_death2.csv",sep=None,engine='python')



#spajamo dva dataseta
dataframe=dataframe.rename(columns={'COUNTRY':'name'})
world = world.merge(dataframe,how='right',on='name')

#fig,ax = plt.subplots()
#divider = make_axes_locatable(ax)
#cax = divider.append_axes("right",size="30%" ,pad=0.8)
ax=world.plot(column='CASE-FATALITY',legend=True,figsize=(15, 10),cmap='OrRd',facecolor='lightgray',legend_kwds={'bbox_to_anchor': (1.3, 1)})
