print('Questão 01')
filmes = []
anos = {}

print('Para sair digite S')

nome = input('Entre com o nome do filme:')
while nome != 'S':
    ano = input('Entre com o ano do filme:')
    filme = {'nome': nome, 'ano': ano}
    filmes.append(filme)
    nome = input('Entre com o nome do filme:')
print(filmes)

anos = {filmes[0]['ano']}
for i in range(1, len(filmes)):
    anos |= {filmes[i]['ano']}

maisRecente = 0
for i in range(len(filmes)):
    if int(filmes[i]['ano']) > maisRecente:
        maisRecente = int(filmes[i]['ano'])

for i in range(len(filmes)):
    if int(filmes[i]['ano']) == maisRecente:
        ano_recente = (filmes[i])

print('Quantidade de filme cadastrados:', len(filmes))
print("Diferentes anos cadastrados:", anos)
print("Filme mais recente:", ano_recente)

print('--------------------------')

print('Questão 02')
import numpy as np
marcas1 = np.array(['apple', 'motorola', 'nokia', 'sony'])
marcas2 = np.array(['xiaomi', 'lg', 'huawei', 'google'])

marcas = np.concatenate((marcas1, marcas2))
marcas = np.char.upper(marcas)
marcas = np.sort(marcas)
marcas = marcas.reshape(4, 2)

indx = np.char.find(marcas, 'A')
print(indx)
indx = indx > -1
indx = indx.sum(axis=1)

print(marcas)
print('Linha que contem A nos dois elementos: ')
k = 0
for i in indx:
    if i == 2:
         print(k)
    k += 1

print('--------------------------')

print('Questão 03')
colors = [{"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1],"hex": "#000"}}, {"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1],"hex": "#0F0"}}, {"color": "yellow", "type": "primary","code": {"rgba": [255,255,0,0.7],"hex": "#FF0"}}, {"color": "blue", "type": "primary","code": {"rgba": [0,0,255,1],"hex": "#00F"}} ]

print('A) Cores: ')
for i in range(4):
    if (colors[i]['type'] == 'primary'):
        print(colors[i]['color'])

print('B) Azul: ')
blue = []
for i in colors:
    if (i['code']['rgba'][2] == 255):
        blue.append(i)

for nome in blue:
    print(nome['code']['hex'])

print('C) Opacidade 0.1: ')
j = 0
opacidadeMin = []
for i in colors:
    if i['code']['rgba'][3] == 0.1:
       print(j)
       j += 1

print('D) Hexadecimal dois zeros: ')
hex = []
for i in colors:
    if (i['code']['hex'].__contains__('00')):
        hex.append(i)

for nome in hex:
    print("Cor:", nome['color'], "Tipo:", nome['type'])

print('E) Hexadecimal com f: ')
hex = []
for i in colors:
    if (i['code']['hex'].__contains__('F')):
        hex.append(i)

for nome in hex:
    print("Cor:", nome['color'], "Tipo:", nome['type'])











