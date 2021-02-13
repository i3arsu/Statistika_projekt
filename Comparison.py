import matplotlib.pyplot as plt
import pandas as pd
from os import getcwd
from datetime import datetime

fig, ax = plt.subplots(figsize=(10,8))
ax.set_facecolor("#333333")
fig.set_facecolor("#333333")

data = pd.read_csv (getcwd()+'/Bolesti/covid_data.csv')
covid = pd.DataFrame(data, columns = ['iso_code','date','new_cases','new_cases_smoothed', 'total_cases', 'population'])
sim = pd.read_csv (getcwd()+'/Simulacija/simulation.csv')

covid_HR = covid.loc[covid['iso_code'] == 'HRV']
covid_AND = covid.loc[covid['iso_code'] == 'AND'] # najveci postotak
covid_WW = covid.groupby('date')
covid_WW = covid_WW['total_cases'].sum()/covid_WW['population'].sum()[:-1]

start_time = datetime.fromisoformat(min(covid['date'])).timestamp()
start_HR = int((datetime.fromisoformat(min(covid_HR['date'])).timestamp()-start_time)/(60*60*24))
start_AND = int((datetime.fromisoformat(min(covid_AND['date'])).timestamp()-start_time)/(60*60*24))
start_WW = 0

ax.plot(range(start_HR,len(covid_HR)+start_HR),covid_HR['total_cases']/covid_HR['population'],label='HRV')
ax.plot(range(start_AND,len(covid_AND)+start_AND),covid_AND['total_cases']/covid_AND['population'],label='AND')
ax.plot(range(start_WW,len(covid_WW)+start_WW),covid_WW,label='SVJ')
timestep = int(len(covid_WW)/len(sim))
ax.plot(range(0,len(sim)*timestep,timestep),sim['total_cases']/sim['population'],label='SIM')

ax.legend(loc='upper left')

plt.show()
