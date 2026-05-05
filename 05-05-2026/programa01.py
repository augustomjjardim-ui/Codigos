'''
1. Crie um programa que o usuario passa digitar quantos numeros quiser e ao terminar imprima a lista em ordem crescente
2. Crie um programa que o ususario possa digitar a quantidade desejada de notas de um determinado aluno(min 0 max 10) 
e mostre se ele esta aprovado >=7, recuperação>=5, reprovado
'''
import os
import time
lista = []

while True:
    num = float(input('Qual numero quer digitar? '))
    lista.append(num)
    acabou = input('Deseja colocar mais numeros? (s - sim | n - não) ').lower()
    if acabou == 'n':
        break
lista.sort()
os.system('cls')
for i in range(5,0,-1):
    time.sleep(1)
    os.system('cls')
    print(f'Contagem regressiva...{i}')
print(f'essa é sua lista {lista}')
time.sleep(5)
os.system('cls')

print(30*'=','Boletim Escolar',30*'=')
lista_notas = []
nome = input('Digite o nome do aluno: ').title()
curso = input('Digite o curso do aluno: ').upper()
while True:
    num1 = float(input('Digite a nota do aluno '))
    if num1 < 0 or num1 > 10:
        print('Número invalido!')
        continue
    else:
        lista_notas.append(num1)
        acabou = input('Tem mais notas? (s - sim | n - não) ').lower()
        if acabou == 'n':
            break
os.system('cls')
media = sum(lista_notas)/len(lista_notas)
for i in range(5,0,-1):
    time.sleep(1)
    os.system('cls')
    print(f'Aguarde...{i}')
os.system('cls')
if media >= 7:
    print(f'{23*'='}APROVADO{23*'='}\n\n{23*' '}Aluno: {nome}\n{23*' '}Media: {media}')
elif media >= 5:
    print(f'{23*'='}RECUPERAÇÃO{23*'='}\n\n{23*' '}Aluno: {nome}\n{23*' '}Media: {media}')
else:
    print(f'{23*'='}REPROVADO{23*'='}\n\n{23*' '}Aluno: {nome}\n{23*' '}Media: {media}')