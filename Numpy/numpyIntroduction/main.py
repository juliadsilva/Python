# Introducao ao NumPy
# Importando NumPy
import numpy as np

arr = np.array([1, 2, 3])
print(type(arr))

# Criando um NumPy Arrays 2D
# Neste caso, ele espera um lista de listas
mtz = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print(mtz)
print(mtz[1,1])

# Formas de se criar NumPy Arrays Automaticamente
# Funcoes pre-prontas para estruturas de ndarrays
# 1.zeros
arr = np.zeros(10)
# 2.ones
arr = np.ones(10)
mtz = np.ones([5,5], dtype=int)
# 3.arange
arr1 = np.arange(10) # de 0 ao valor inserido
arr2 = np.arange(10,20,1) # em um intervalo e passo definido
#4. linspace
arr = np.linspace(0,100,6)
print(arr)

# Ordenando elementos com NumPy Array
arr = np.array([2,1,5,3,7,4,6,8])
print(np.sort(arr))
print(np.flip(np.sort(arr)))

# Concatenando Arrays
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print('arr1+arr2',arr1+arr2)
print('arr1 concatenado com arr2', np.concatenate([arr1,arr2]))

# Extraindo infos importantes no NumPy
mtz = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
print('Size:', mtz.size)
print('Dimensoes:', mtz.ndim)
print('Shpa:', mtz.shape)

# Conceito de Reshape no NumPy
mtz = np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
])
arr = mtz.reshape(12)
mtz2 = arr.reshape(4,3)