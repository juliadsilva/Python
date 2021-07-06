import pandas as pd

#Leitura de dados
dfRio = pd.read_csv("rio.csv", sep=",")
dfRio = dfRio[['name', 'nationality', 'sport', 'gold']]
maxGold = dfRio['gold'].max()
print(dfRio[dfRio['gold'] == maxGold])
