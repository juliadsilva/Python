import numpy as np

# Carregando dados
space = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# Porcentagem de Missoes que deram certo
total = space[1:, 7].copy()
sucesso = total[np.char.find(total, 's') > 0]
qtdTotal = total.size
qtdSucesso = sucesso.size
media = (qtdSucesso/qtdTotal)*100
print('Media de sucessos %.2f' %media, '%')
print('--------------------------')

# Media de gastos de uma missão espacial
total = space[1:, 6].copy()
gastos = total[total > '0']
final = gastos.astype(float)
print('Media de gastos %.2f' %final.mean())
print('--------------------------')

# Missões - EUA
total = space[1:, 2].copy()
eua = total[np.char.find(total, 'USA') > 0]
qtdTotal = total.size
qtdEUA = eua.size
print('Missões EUA: ', qtdEUA)
print('--------------------------')

# Missão mais cara da empresa "SpaceX"
empresa = space[1:, 1].copy()
cost = space[1:, 6].copy()
spaceX = np.char.find(empresa,'SpaceX') >= 0
valorSpaceX = cost[spaceX == True]
final = valorSpaceX.astype(float)
print('A missao mais cara da SpaceX custou:', final.max())
print('--------------------------')

# Nome das empresas que ja realizaram missoes espaciais juntamente
# com suas respectivas quantidades de missoes
print('Empresa-Qunatidade')
empresa = space[1:, 1]
empresa, qnt = np.unique(empresa, return_counts=True)
for i in range(len(empresa)):
   print(empresa[i], ': ', qnt[i])
