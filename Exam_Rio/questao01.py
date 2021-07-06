import pandas as pd
import matplotlib.pyplot as plt

#Leitura de dados
dfRio = pd.read_csv("rio.csv", sep=",")

dfRio = dfRio[['sex']]
dfMale = dfRio[dfRio['sex'].str.contains('male')]
dfFemale = dfRio[dfRio['sex'].str.contains('female')]
plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.bar('Masculino', dfMale.size, color='#6495ED')
plt.bar('Feminino', dfFemale.size,  color='#6A5ACD')
plt.show()

