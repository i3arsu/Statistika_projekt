import matplotlib.pyplot as plt
import pandas as pd
from os import getcwd

fig, ax = plt.subplots(figsize=(10,8))
ax.set_facecolor("#333333")
fig.set_facecolor("#333333")

data = pd.read_csv (getcwd()+'/Sitemap/owid-covid-data.csv')
covid = pd.DataFrame(data, columns = ['iso_code','new_cases','new_cases_smoothed', 'total_cases', 'population'])
sim = pd.read_csv (getcwd()+'/simulation.csv')

covid = covid.loc[covid['iso_code'] == 'HRV']

ax.plot(range(len(covid)),covid['total_cases'],label='HRV')
ax.plot(range(0,len(sim)*7,7),sim['sick']*1000,label='SIM x 1000')

ax.legend(loc='upper left')

plt.show()
