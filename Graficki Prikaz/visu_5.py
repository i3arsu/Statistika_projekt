zaraz2=pd.read_csv(os.getcwd()+"\\owid-covid-data.csv")
plt.figure();
zaraz3=pd.read_csv(os.getcwd()+"\\Pandemic_H1N1_2009.csv",sep=None,engine='python',error_bad_lines=False)
plt.figure();
print('What country')
drzava1=input()
print('Cases, Deaths')
tip=input()
if (tip=='Cases' or tip=='cases' or tip=='CASES'):
    tip1='total_cases'
    tip2='Cases'
    zaraz2_1=zaraz2[(zaraz2['location']==drzava1) & zaraz2[tip1] & zaraz2['date']]
    zaraz2_2=zaraz3[(zaraz3['Country']==drzava1) & zaraz3[tip2] & zaraz3['Update Time']]


if (tip=='Deaths' or tip=='DEATHS' or tip=='deaths') :
    tip1='total_deaths'
    tip2='Deaths'
    zaraz2_1=zaraz2[(zaraz2['location']==drzava1) & zaraz2[tip1] & zaraz2['date']]
    zaraz2_2=zaraz3[(zaraz3['Country']==drzava1) & zaraz3[tip2] & zaraz3['Update Time']]

zaraz2_1['date'] = pd.to_datetime(zaraz2_1['date'])

zaraz2 = pd.DataFrame(zaraz2,columns=[tip,'date'])

zaraz2_1.plot(x='date', y=tip1, kind = 'line')
zaraz2_2.plot(x='Update Time', y=tip2,color='red', kind='line')
