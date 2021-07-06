import pandas as pd
import matplotlib.pyplot as plt

#Questão 01
dfSpace = pd.read_csv("space.csv", sep=";")
dfSpace = dfSpace[['Location', 'Company Name']]

dfEUA = dfSpace[dfSpace['Location'].str.contains('USA')]
companyEUA = dfEUA['Company Name']
companyEUA = pd.unique(companyEUA);

dfChina = dfSpace[dfSpace['Location'].str.contains('China')]
companyChina = dfChina['Company Name']
companyChina = pd.unique(companyChina)

plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.xlabel('Paises')
plt.ylabel('Qtd Empresas Espaciais')
plt.bar('EUA', companyEUA.size,  color='#6A5ACD')
plt.bar('CHINA', companyChina.size, color='#6495ED')

#Questão 02
dfPaises = pd.read_csv("paises.csv", sep=";", converters={'Country': str.strip, 'Region': str.strip})
dfPaises = dfPaises[['Country', 'Region', 'Birthrate', 'Deathrate']]
dfPaises = dfPaises[dfPaises['Region'].str.contains('NORTHERN AMERICA')]

plt.subplot(2, 1, 2)
plt.xlabel('Cidades')
plt.ylabel('Taxas')
plt.plot(dfPaises['Country'], dfPaises['Birthrate'], color='#00BFFF')
plt.plot(dfPaises['Country'], dfPaises['Deathrate'], color='blue')
plt.legend(('Birthrate', 'Deathrate'))
plt.show()





















