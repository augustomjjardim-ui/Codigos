import os
import time
import math
#Atividade 1
while True:
    print(30*"=", "Atividade1", 30*"=")
    num1 = float(input("digite um numero: "))
    num2 = float(input("digite um numero: "))
    resultado = num2 / num1
    print(f'O resultado da divisão é: {resultado:.2f}')
    time.sleep(1)
    os.system('cls')
    break

#Atividade 2
while True:
    print(30*"=", "Atividade2", 30*"=")
    temp1 = float(input(f'Digite uma temperatura em Farenheit: '))
    temp2 = temp1 / 32
    print(f'A sua temperatura em Celsius é: {temp2} ')
    time.sleep(1)
    os.system('cls')
    break

#Atividade 3
while True:
    print(30*"=", "Atividade3", 30*"=")
    num25 = float(input(f'Digite  a quantidade de dinheiro em reais: R$ ')).replace(",", ".")
    num26 = num25/6
    print(f'Sabendo que um dolar em 2026 e aproximadamente 6 reais , a quantidade de dinheiro digitado e R$ {num25}')
    print (f'em dolar sera: ${num26}')
    time.sleep(1)
    os.system('cls')
    break
#Atividade 4
while True:
    print(30*"=", "Atividade4", 30*"=")
    num29 = float(input(f'Digite o primeiro numero '))
    num30 = float(input(f'Digite o segundo numero '))
    num31 = float(input(f'Digite o terceiro numero '))
    media = ((num29 + num30 + num31)/3)
    print(f'A media é: {media}')
    time.sleep(1)
    os.system('cls')
    break
#Atividade 5
while True:
    print(30*"=", "Atividade5", 30*"=")
    nome = input('Digite o seu nome').title()
    print(f'O nome {nome} é um dado do tipo: {type(nome)}')
    time.sleep(1)
    os.system('cls')
    break


#Atividade 6
while True:
    print(30*"=", "Atividade6", 30*"=")
    lista_num = []
    tmp = 0
    while tmp < 10:
        print (f'Digite 10 número, valores digitados até agora {tmp}')
        dig = float(input('Digite um número: '))
        lista_num.append(dig)
        tmp += 1
        time.sleep(1)
        os.system('cls')
    lista_doub = [x * 2 for x in lista_num]
    print(f'Lista inicial {lista_num}')
    print(f'Lista duplicada {lista_doub}')
    time.sleep(5)
    os.system('cls')    
    break

#Atividade 7
while True:
    print(30*"=", "Atividade7", 30*"=")
    num23 = float(input('Digite um número: '))
    num24 = float(input('Digite outro número: '))
    if num24 < num23:
        print(f'O segundo valot é o menor!')
    else:
        print(f'O segundo valor não é o menor')
    time.sleep(5)
    os.system('cls')    
    break
#Atividade 8
while True:
    print(30*"=", "Atividade8", 30*"=")
    nome1 = input('Digite o seu nome: ')
    snome1 = input('Digite o seu sobrenome: ')
    nome2 = input('Digite outro nome: ')
    snome2 = input('Digite outro sobrenome: ')
    print(f'Se trocarmos as suas informações de lugaro o resultado é: {nome1} {snome2} {nome2} {snome2}')
    time.sleep(5)
    os.system('cls')    
    break

#Atividade 9
while True:
    print(30*"=", "Atividade9", 30*"=")
    num5 = float(input("Digite um número: "))
    div = num5 / 2
    print(f'A metade do valor é: {div}')
    time.sleep(5)
    os.system('cls')    
    break

#Atividade 10
while True: 
    print(30*"=", "Atividade10", 30*"=")
    num6 = float(input('Digite a largura: '))
    num7 = float(input('Digite a altura: '))
    area = num6 * num7
    print(f'A sua área é {area}')
    time.sleep(5)
    os.system('cls')    
    break

#Atividade 11
while True: 
    print(30*"=", "Atividade11", 30*"=")
    num20 = int(input('Quer saber quem vem antes e depois de um numero? \n Digite ele: ').replace(",", "."))
    print(f'O antecessor é {num20-1} e o sucessor é {num20+1}')
    time.sleep(5)
    os.system('cls')    
    break
# Atividade 12
while True:
    print(30*"=", "Atividade12", 30*"=")
    num8 = float(input("Digite um número: "))
    dobro = num8 * 2
    triplo = num8 * 3
    rai = math.sqrt(num8)
    print(f'O dobro do valor digitado é {dobro}, o triplo do valor digitado é {triplo} e sua raiz é {rai}')
    time.sleep(5)
    os.system('cls')    
    break

# Atividade 13
while True:
    print(30*"=", "Atividade13", 30*"=")
    num21 = float(input('Digite um número: ').replace(",", "."))
    print(f'O dobro desse número é {num21*2}')
    time.sleep(5)
    os.system('cls')    
    break
#Atividade 14
while True:
    print(30*"=", "Atividade14", 30*"=")
    num9 = float(input("Digite um número: "))
    num10 = float(input("Digite um número: "))
    num11 = float(input("Digite um número: "))
    produto = num9 * num10 * num11
    print(f'O valor do produto é {produto}')
    time.sleep(5)
    os.system('cls')    
    break

#Atividade 15
while True:
    print(30*"=", "Atividade15", 30*"=")
    num27 = float(input('Digite o valor em dinheiro do produto: R$ ').replace(",", "."))
    num28 = num27 * 0.9
    print(f'O valor do produto normalmente seria R${num27}, mas com 10% de desconto, fica R${num28}')
#Atividade 16
while True:
    print(30*"=", "Atividade16", 30*"=")
    valor = float(input('Digite um capital inicial do seu investimento: ').replace(",", "."))
    taxj = float(input('Digite a taxa de jurois: ').replace(",", "."))
    tempo =  float(input('Por quanto tempo o dinheiro ficará investido? ').replace(",", "."))
    taxj = taxj/100
    juros = valor*taxj
    jsimples = juros * tempo
    print(f'O valor ganho pelos juros foi de R$: {jsimples}')
    time.sleep(5)
    os.system('cls')    
    break
#Atividade 17
while True:
    print(30*"=", "Atividade17", 30*"=")
    num12 = float(input("Digite um valor em metros: "))
    centimetros = num12 * 100
    mili = num12 * 1000
    km = num12 / 1000
    print(f'O valor digitado por você em cm é {centimetros}, em milimetros é {mili} e em km é {km}')
    time.sleep(5)
    os.system('cls')    
    break
#Atividade 18
while True:
    print(30*"=", "Atividade18", 30*"=")
    horas = float(input("Digite as horas: "))

    minutos = horas * 60
    print(minutos)
    time.sleep(5)
    os.system('cls')    
    break

#Atividade 19
while True:
    print(30*"=", "Atividade19", 30*"=")
    distancia = float(input('Digite a distancia percorrida: '))
    combustivel = float(input('Digite o combustivel gasto: '))

    consumo = distancia/combustivel
    print('O consumo medio foi: ', consumo)

#Atividade 20
while True:
    print(30*"=", "Atividade20", 30*"=")
    num22 = float(input('Digite um número: ').replace(",", "."))
    if num22 <0:
        print(f'O valor absoluto de {num22} é {num22*-1:.0f}')
    else:
        print(f'O valor absoluto de {num22} é {num:.0f}')