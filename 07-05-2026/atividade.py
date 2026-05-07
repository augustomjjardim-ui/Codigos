'''
Desenvolva um sistema de gerenciamento de Carros com realização CRUD
'''
import os
import time

carros = []
proximo_id = 1

os.system('cls')
while True:
    print('===== Sistema de Carros 🚗 =====')
    print('1 - Cadastrar carro')
    print('2 - Listar carro')
    print('0 - Sair carro')

    opcao = input('Escolha uma opção: ')

    # criar
    if opcao == '1':
        modelo = input('\nDigite o moddelo do carro: ').title()
        preco = float(input('Digite o preço do carro: ').replace(',','.'))
        marca = input('Digite a marca do carro: ').title()

        carro = {
            'id'     : proximo_id,
            'modelo' : modelo,
            'preco'  : preco,
            'marca'  : marca
        }
        carros.append(carro)
        proximo_id += 1
        with open('carro.txt', "a") as arquivo:
            for c in carros:
                arquivo.write(
                    f'ID: {c['id']} | Modelo: {c['modelo']} | '
                    f'Preço: {c['preco']} | Marca: {c['marca']}\n'
                )
        time.sleep(2)
        os.system('cls')

        print('✅Carro cadastrado com sucesso!')
    # read
    elif opcao == '2':
        print('\n Lista de carros: \n')
        with open('carro.txt', "r") as arquivo:
            for linha in arquivo:
                print(linha.strip())
                print('\n')
    # sair
    elif opcao == '0':
        total = 20
        barra = ""
        print('Saindo do sistema...')
        for i in range(1,total+1):
            barra += '🟩'
            porcentagem = int((i/total)*100)
            vazio ='🔳'*(total -i)
            print(f'\r[{barra}{vazio}] {porcentagem}%',end="")
            time.sleep(0.3)
        break

    else:
        print('Opção invalida!')