import pandas as pd
import numpy as np

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})
print("Serie Ano 1:")
print(seriesAno1)
print("Serie Ano 2:")
print(seriesAno2)
print("*******************************")

print("Somatorio ano 1:", sum(seriesAno1))
print("Somatorio ano 2:", sum(seriesAno2))
print("*******************************")

print("Crescimento/Declinio")
print(seriesAno1.sub(seriesAno2, fill_value = 0));
print("*******************************")

print("Crescimento")
taxa = seriesAno1.sub(seriesAno2, fill_value = 0);
print(taxa[taxa > 0])
print("*******************************")

seriesAno3 = seriesAno2 + taxa
print("Serie Ano 3:")
print(seriesAno3)
seriesAno4 = seriesAno3 + taxa
print("Serie Ano 4:")
print(seriesAno4)

print("Mais popular:");
print(seriesAno4.nlargest(n=1, keep='first'))