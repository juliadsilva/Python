# Importando NumPy
import numpy as np

#Questão 01
print("Questao 01")
np.random.seed(5)
arr = np.random.rand(10)
arr_m = arr*100
arr_f = arr_m.astype(int)
print(arr_f)
print("*****")

#Questão 02
print("Questao 02")
np.random.seed(10)
mtz = np.random.randint(1, 50, (4, 4))
print(mtz)
print("*****")

# Questão 03
print("Questao 03")
col_media = mtz.mean(axis=0)
lin_media = mtz.mean(axis=1)
print("Coluna:", col_media)
print("Linha:", lin_media)
print("Max Coluna:", col_media.max())
print("Max Linha:", lin_media.max())
print("*****")

# Questão 04
print("Questao 04")
unicos, cont = np.unique(mtz, return_counts=True)
print(np.asarray((unicos, cont)).T)

arr = mtz.reshape(16).tolist()
print("Elementos 02 vezes:")
dois = []
for i in unicos:
    c = arr.count(i)
    if(c == 2):
        dois.append(i);
print(dois)




