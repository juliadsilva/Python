import pandas as pd

#Leitura de dados
dfRio = pd.read_csv("rio.csv", sep=",")
dfRio = dfRio[['height', 'sex', 'sport']]

dfFemale = dfRio[dfRio['sex'].str.contains('female')]
dfVolley = dfFemale[dfFemale['sport'].str.contains('volleyball')]
mean = dfVolley['height'].mean()
print("Media de altura volley feminino: %.2f" %mean)


