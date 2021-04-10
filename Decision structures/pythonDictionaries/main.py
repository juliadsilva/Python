# Exercicio 01
# Copa do Mundo de Clubes da FIFA de 2015

fMudial = ('Barcelona', 'River Plate','Sanfrecce','Guangzhou Evergrande','America')
print('Tres primeiros:',fMudial[:3])
print('Dois ultimos:',fMudial[3:])
print('Ordem alfabetica:',sorted(fMudial))

for aux in range(0,len(fMudial)):
    if(fMudial[aux] == 'Barcelona'):
        print('Barcelona:',aux+1,'colocacao')

print('###########################################')

# Exercicio 2
lojaA = {'Iphone 12pro','Iphone 13', 'Redmi Noite 9'}
lojaB = {'Galaxy S21', 'Galaxy S20','Glaxy Note 21', 'Redmi Noite 9' }

print("Total:",lojaA | lojaB)
print('Ambas:',lojaA & lojaB)

print('###########################################')

# Exercicio 3
aluno = {'nome':'Mateus','media':70}

if aluno['media'] >= 60:
   aluno['situacao'] = 'AP'
else:
   aluno['situacao'] = 'RP'

for k,v in aluno.items():
    print(f'{k} é {v}')





