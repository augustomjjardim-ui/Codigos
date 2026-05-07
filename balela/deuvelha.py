# Jogo da Velha
import os
import time
# Tabuleiro
tabuleiro = [' ']*9
def mostrar_tabuleiro():

    print(f' {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print( '---+---+---')
    print(f' {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print( '---+---+---')
    print(f' {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')
# Fazendo uma jogada
def fazer_jogada(jogador):
    while True:
        pos = int(input(f'Onde deseja jogar, player {jogador}? '))-1
        if pos < 0 or pos > 8:
            print('Posição invalida!')
            continue
        elif tabuleiro[pos] != ' ':
            print('Posição ocupada')
            continue
        else:
            if jogador == '1':
                tabuleiro[pos] = 'X'
                break
            elif jogador == '2':
                tabuleiro[pos] = 'O'
                break
# Quem venceu?
def vencedor(jogador):
    if tabuleiro[0] == tabuleiro[1] == tabuleiro[2] != ' ':
        return True
    elif tabuleiro[3] == tabuleiro[4] == tabuleiro[5] != ' ':
        return True
    elif tabuleiro[6] == tabuleiro[7] == tabuleiro[8] != ' ':
        return True
    elif tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != ' ':
        return True
    elif tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != ' ':
        return True
    elif tabuleiro[0] == tabuleiro[3] == tabuleiro[6] != ' ':
        return True
    elif tabuleiro[1] == tabuleiro[4] == tabuleiro[7] != ' ':
        return True
    elif tabuleiro[2] == tabuleiro[5] == tabuleiro[8] != ' ':
        return True
    return False
# Empate
def empate():
    return ' ' not in tabuleiro
# Hora do jogo
while True:
    os.system('cls')
    mostrar_tabuleiro()
    fazer_jogada('1')
    if vencedor('1'):
        os.system('cls')
        print(f'O jogador 1 venceu!')
        mostrar_tabuleiro()
        break
    if empate():
        os.system('cls')
        print('\nEmpate!')
        mostrar_tabuleiro()
        break
    os.system('cls')
    mostrar_tabuleiro()
    fazer_jogada('2')
    if vencedor('2'):
        os.system('cls')
        print(f'O jogador 2 venceu!')
        mostrar_tabuleiro()
        break
    if empate():
        os.system('cls')
        print('\nEmpate!')
        mostrar_tabuleiro()
        break