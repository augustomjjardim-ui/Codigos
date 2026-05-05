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
    print('3 - Atualizar carro')
    print('4 - Deletar carro')
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

        print('✅Carro cadastrado com sucesso!')
    # read
    elif opcao == '2':
        if not carros:
            print('Não há nenhum carro cadastrado')
        else:
            print('\n Lista de carros: ')
            for carro in carros:
                print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preco']} | Marca: {carro['marca']}\n')
        
    # update
    elif opcao == '3':
        os.system('cls')
        print('\n Lista de carros: ')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preco']} | Marca: {carro['marca']}')
        id_busca = int(input('Digite o id do carro para Atualizar: '))

        encontrado = False

        for carro in carros:
            if carro['id'] == id_busca:
                novo_modelo =input('Digite o novo modelo: ').title()
                novo_preco = float(input('Digite o novo Preço: ').replace(',','.'))
                nova_marca = input('Digite a nova marca: ').title()

                carro['modelo'] = novo_modelo
                carro['preco'] = novo_preco
                carro['marca'] = nova_marca

                print('Carro atualizado com sucesso!')
                encontrado = True
                break
        if not encontrado:
            print('Carro não encontrado')
    # deleta
    elif opcao == '4':
        os.system('cls')
        print('\n Lista de carros: ')
        for carro in carros:
            print(f'ID: {carro['id']} | Modelo: {carro['modelo']} | Preço: {carro['preco']} | Marca: {carro['marca']}')
        id_busca = int(input('Digite o id do carro para deletar: '))

        encontrado = False

        for carro in carros:
            if carro['id'] == id_busca:
                carros.remove(carro)
                print('Carro deletado com sucesso!')
                encontrado = True
                break
        if not encontrado:
            print(' Carro não encontrado!')
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