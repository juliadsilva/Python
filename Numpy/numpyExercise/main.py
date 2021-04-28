# Remodelamento (Reshape) de Arrays
# Exercícios Propostos

# Importando NumPy
import numpy as np

print('Questao 1')
arr1 = np.linspace(0,1,12)
print(arr1)

print('Questao 2')
arr2 = np.arange(0,51,2)
arr3 = np.arange(100,50,-2)
arr4 = np.concatenate([arr2,arr3])
print(np.sort(arr4))

print('Questao 3')
print(np.flip(np.sort(arr4)))

print('Questao 4')
mtz1 = np.ones([3,4], dtype=int)
arr5 = mtz1.reshape(12)
print(mtz1)
print(arr5)

print('Questao 5')
mtz2 = np.ones([1,3], dtype=int)
[lin,col] = mtz2.shape
mult = lin*col

if(mult % 2 == 0):
    print('Vetor com numeros pares de elementos')
else:
    print('Vetor com numeros impares de elementos')


