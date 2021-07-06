import pandas as pd

#Leitura de dados
dfRio = pd.read_csv("rio.csv", sep=",")
dfRio = dfRio[['weight', 'sport']]
dfPeso = dfRio[dfRio['weight'] > 150]
sport = pd.unique(dfPeso['sport'])
print(sport)


