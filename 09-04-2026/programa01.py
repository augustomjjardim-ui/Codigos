"""
    Calculos e manipulação de variaveis
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")

# tratamento de exeção
try:
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
except ValueError as e:
    print(e)

idade = int(idade)

imc = peso/ (altura ** 2)

print("Olá, ",nome," seu imc é: ",imc)