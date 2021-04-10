# Colecoes em Python

# 1. Tuplas (Tuple)
# Guarda seus valores dentro de ()
# Colecao IMUTAVEL

print('**** COLECAO ****')
nomes = ('Goku', 'Vegeta', 'Trunks', 'Goran')
print(nomes)
print(nomes[2:])
print(nomes[:2])
print(nomes[1:3])
print(nomes[1])
print(nomes[-1])
print(len(nomes))

# Erro - tuplas não podem ser alteradas
# nomes[0] = 'Bulma'

print('******')

for aux in range(0,len(nomes)):
    print(nomes[aux])

# Alguns metodos padroes do Python
print(sorted(nomes))
print(max(nomes))

print('******')

x = (2,6,8)
y = (5,6,9,1)
z = x + y
print(z)

print('###########################################')

# 2. Listas
# Guardam seus elementos entre[]
# Colecao MUTAVEL

print('**** LISTAS ****')
nomesL = ['Goku','Vegeta','Trunks','Gohan']
print(nomesL)
nomesL[3] = 'Goten'
print(nomesL)
nomesL.append('Bulma')
print(nomesL)
nomesL.remove('Vegeta')
print(nomesL)

if 'Vegeta' in nomesL:
    print("Vixi treta na area!")
else:
    print('Podemos ficar mais suaves :)')

print('###########################################')

# 3. Conjunto (SETS)
# Guarda seus elementos dentro de {}
# NAO GUARDA ELEMENTOS REPETIDOS
# Nao guarda o indice dos elementos

print('**** CONJUNTOS ****')
nomesC = {'Goku','Vegeta','Trunks','Gohan','Trunks','Goku'}
print(nomesC)

print('###########################################')

# 4. Dicionarios (DictionariesDictionaries)
# Indices customizados
# Tambem guarda seus elementos entre {}
# Utiliza do conceito de chave:valor para seus valores
# {'chave':'valor')

print('**** DICIONARIOS ****')
dados = {'nome':'Goku','idade':43}
print(dados['nome'])
dados['sexo'] = 'M'
print(dados)
del dados['sexo']
print(dados)

print('******')

print(dados.keys())
print(dados.values())
print(dados.items())

print('******')

for k,v in dados.items():
    print(f'{k} é {v}')

print('******')

dados1 = {'nome':'Goku','idade':43}
dados2 = {'nome':'Gohan','idade':23}
dados3 = {'nome':'Pan','idade':5}
dbz = [dados1,dados2,dados3]

print(dbz[0]['nome'])











