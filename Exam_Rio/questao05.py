import pandas as pd
import matplotlib.pyplot as plt

#Leitura de dados
dfRio = pd.read_csv("rio.csv", sep=",")
dfRio = dfRio[['nationality', 'id']]
dfRio = dfRio.groupby('nationality').count()

dfPaises = dfRio.nlargest(3, 'id')
print(dfPaises)

plt.pie(x=dfPaises['id'].values, labels=dfPaises.index.values, autopct='%1.1f%%', colors=['#6495ED', '#6A5ACD', '#00BFFF'])
plt.legend()
plt.show()