# Arredondamento
num = 5.4
print(f'{round(num)}')
# DOBRO
lista=[67,94,3,95,4678]
dobro=[v*2 for v in lista]
print(dobro)
#Comparação
num1 =input("")
num2 = input('')
# Operador termario
resultado = f"{num1} é maior." if num1 > num2 else f'{num2} é maior.'
# Maipulação de lista
nome1 = input('digite o primeiro nome completo: ')
nome2 = input('digite o segundo nome completo: ')

# Separando os dois
parte1 = nome1.split()
parte2 = nome2.split()

#separando os nomes dentro das variaveis
primeiro_nome = parte1[0]
sobrenome1 = parte2[-1]

segundo_nome = parte2[0]
sobrenome2 = parte1[-1]

novo_nome1 = primeiro_nome + " " + sobrenome1
novo_nome2 = segundo_nome + " " + sobrenome2

print(novo_nome1)
print(novo_nome2)