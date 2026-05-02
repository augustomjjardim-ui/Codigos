# Jogo da Velha
"""
acaba = str(None)
# Tabuleiro
linha1 = [0,0,0]
linha2 = [0,0,0]
linha3 = [0,0,0]
# Hora do jogo
while True:
    print('Para jogar escolham um número de 1 a 9')
    # Tabuleiro
    print(linha1)
    print(linha2)
    print(linha3)
    # Jogador 1 ou X
    jog1 = input('Onde vai jogar, Player 1? ')
    # Jogada sendo efetuada
    match jog1:
        case '1':
            if linha1[0] == 0:
                linha1[0] = 1
            else:
                print('Já está ocupado!')
        case '2':
            if linha1[1] == 0:
                linha1[1] = 1
            else:
                print('Já está ocupado!')
        case '3':
            if linha1[2] == 0:
                linha1[2] = 1
            else:
                print('Já está ocupado!')
        case '4':
            if linha2[0] == 0:
                linha2[0] = 1
            else:
                print('Já está ocupado!')
        case '5':
            if linha2[1] == 0:
                linha2[1] = 1
            else:
                print('Já está ocupado!')
        case '6':
            if linha2[2] == 0:
                linha2[2] = 1
            else:
                print('Já está ocupado!')
        case '7':
            if linha3[0] == 0:
                linha3[0] = 1
            else:
                print('Já está ocupado!')
        case '8':
            if linha3[1] == 0:
                linha3[1] = 1
            else:
                print('Já está ocupado!')
        case '9':
            if linha3[2] == 0:
                linha3[2] = 1
            else:
                print('Já está ocupado!')
    # Jogador 2
    jog2 = input('Onde vai, Player 2? ')
    # Jogada sendo efetuada
    match jog2:
        case '1':
            if linha1[0] == 0:
                linha1[0] = 2
            else:
                print('Já está ocupado!')
        case '2':
            if linha1[1] == 0:
                linha1[1] = 2
            else:
                print('Já está ocupado!')
        case '3':
            if linha1[2] == 0:
                linha1[2] = 2
            else:
                print('Já está ocupado!')
        case '4':
            if linha2[0] == 0:
                linha2[0] = 2
            else:
                print('Já está ocupado!')
        case '5':
            if linha2[1] == 0:
                linha2[1] = 2
            else:
                print('Já está ocupado!')
        case '6':
            if linha2[2] == 0:
                linha2[2] = 2
            else:
                print('Já está ocupado!')
        case '7':
            if linha3[0] == 0:
                linha3[0] = 2
            else:
                print('Já está ocupado!')
        case '8':
            if linha3[1] == 0:
                linha3[1] = 2
            else:
                print('Já está ocupado!')
        case '9':
            if linha3[2] == 0:
                linha3[2] = 2
            else:
                print('Já está ocupado!')
    # Verificando o vencedor
    if linha1[0,1,2] != 0:
        print('O jogo acabou!!!')
        print(linha1)
        print(linha2)
        print(linha3)
        break
    elif linha2[0,1,2] != 0:
        print('O jogo acabou!!!')
        print(linha1)
        print(linha2)
        print(linha3)
        break
    elif linha3[0,1,2] != 0:
        print('O jogo acabou!!!')
        print(linha1)
        print(linha2)
        print(linha3)
        break
    elif linha1[0] == linha2[0] and linha1[0] == linha3[0] and linha2[0] == linha3[0]:
        print('O jogo acabou!!!')
        print(linha1)
        print(linha2)
        print(linha3)
        break
"""