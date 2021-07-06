import pandas as pd

# Leitura dos Dados
dfPaises = pd.read_csv("paises.csv", sep=";")
dfPaises = (dfPaises.fillna(method='ffill'))
print(dfPaises)
print("_________________________________________")

# Questao 01
print('Paises da Oceania')
dfPaises2 = pd.read_csv("paises.csv", sep=";", converters={'Country': str.strip, 'Region': str.strip})
dfPaises2 = dfPaises2[['Country', 'Region']]
dfPaises2 = dfPaises2.set_index('Region')
oceania = (dfPaises2.loc[['OCEANIA'], ['Country']])
print(oceania)
print('Quantidade: ', len(oceania))
print("_________________________________________")

# Questão 02
print('Maior população')
dfPaises3 = pd.read_csv("paises.csv", sep=";", converters={'Country': str.strip, 'Region': str.strip})
dfPaises3 = dfPaises3[['Country', 'Region', 'Population']]
max = dfPaises3['Population'].max()
print(dfPaises3[dfPaises3['Population'] == max])
print("_________________________________________")

# Questão 03
print('Media de alfabetização por região')
dfPaises4 = pd.read_csv("paises.csv", sep=";", converters={'Region': str.strip})
dfPaises4 = dfPaises4[['Region', 'Literacy (%)']]
lit = dfPaises4.groupby('Region')
print(lit.mean())
print("_________________________________________")

# Questão 04
print('Paises sem costa marítima')
dfPaises5 = pd.read_csv("paises.csv", sep=";")
dfPaises5 = dfPaises5[['Country', 'Coastline (coast/area ratio)']]
dfPaises5[dfPaises5['Coastline (coast/area ratio)'] == 0].to_csv('noCost.csv', sep=";", header=False)
print(dfPaises5[dfPaises5['Coastline (coast/area ratio)'] == 0])
print("_________________________________________")

# Questão 05
def Deathrate(x):
    if x < 9:
        return 'Balanced'
    else:
        return 'Urgent'

dfPaiseshh = pd.read_csv("paises.csv", sep=";")
dfPaiseshh = (dfPaiseshh.fillna(method='ffill'))
hh = dfPaiseshh['Deathrate'].apply(Deathrate)
dfPaiseshh['Humanitari Help'] = hh
dfPaiseshh.to_csv('humanitariHelp.csv', sep=";", header=False)
print(dfPaiseshh)









