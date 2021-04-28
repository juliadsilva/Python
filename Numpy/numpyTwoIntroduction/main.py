import numpy as np

# Geracao de numeros aleatorios
# seed (semente)
# em algumas ferramentas, chamdo de setBase
print("NUMEROS ALEATORIOS")
print("Seed 5")
np.random.seed(5)

#rand
#entre 0 e 1
print("**********")
print("rand")
print(np.random.rand(10))
print(np.random.rand(3, 3))

#radnn - Dist. de Normal de Probabilidadae
# Fenomenos da Natureza funcionam por
# meio desta distribuicao
# gera numeros positivos e negativos
print("**********")
print("radnn")
print(np.random.randn(10))

#randint
print("**********")
print("randint")
print(np.random.randint(10, 20, 5))

# Elementos Unicos
print("\n")
print("NUMEROS UNICOS")
arr = np.array([1, 1, 5, 3, 7, 4, 8, 8])
print(np.unique(arr))
print(np.unique(arr, return_counts=True))

# Operacoes basicas sobre arrays
arr = np.array([1, 2, 3, 4])
arrdois = np.array([5, 6, 7, 8])
print(arr + arrdois)
print(arr - arrdois)

# Funcoes pre prontas do numpy
print(arr.mean())
print(arr.max())
print(arr.astype(str))

# Operacoes em arrays bidimensionais
mtz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
print(mtz.sum())
print(mtz.sum(axis=0))
print(mtz.sum(axis=1))

arr = mtz.sum(axis=1)
print(arr[0])
print(mtz.sum(axis=1)[0])