# Exercícos Propostos
# Julia Daniele Moreira da Silva

# Exercío 01
nome = input('Qual o seu nome? ')
print("Letras maiúsculas:", nome.upper())
print("Letras minúsculas:", nome.lower())
print("Total com espaços:", len(nome))
print("Troca por Inatel:", nome.replace('da Silva', 'Inatel'),"\n")

# Exercío 02
tabuada = int(input("Tabuada do numero: "))
print("Qual o intervalor: ")
x1 = int(input("De: "))
x2 = int(input("Até: "))
# Inclusive o x1
for count in range(x1 - 1, x2):
    print(tabuada, 'x', count + 1, '=', tabuada * (count + 1))
print("\n")

# Exercío 03
print("Entre com seu sexo: ")
sexo = str(input("F - Feminino / M - Masculino: "))
while sexo != 'F' and sexo != 'M':
    sexo = str(input("F - Feminino / M - Masculino: "))

print("Sexo:", sexo)
