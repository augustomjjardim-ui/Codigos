# Jogo da velha pelo ChatGPT
tabuleiro = [0] * 9

import os


def mostrar_tabuleiro():
    print()

    for i in range(0, 9, 3):
        linha = []

        for j in range(3):
            valor = tabuleiro[i+j]

            if valor == 0:
                linha.append(str(i+j+1))
            elif valor == 1:
                linha.append('X')
            else:
                linha.append('O')

        print(f' {linha[0]} | {linha[1]} | {linha[2]} ')

        if i < 6:
            print('-----------')


def fazer_jogada(jogador):
    while True:
        pos = int(input(f'Onde vai jogar, Player {jogador}? ')) - 1

        if pos < 0 or pos > 8:
            print('Posição inválida!')
            continue

        if tabuleiro[pos] != 0:
            print('Já está ocupado!')
            continue

        tabuleiro[pos] = jogador
        break


def verificar_vitoria():
    combinacoes = [
        [0,1,2], [3,4,5], [6,7,8],  # linhas
        [0,3,6], [1,4,7], [2,5,8],  # colunas
        [0,4,8], [2,4,6]            # diagonais
    ]

    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] != 0:
            return tabuleiro[a]

    return 0
def verificar_empate():
    return 0 not in tabuleiro

while True:
    print('\nTabuleiro:')
    mostrar_tabuleiro()

    fazer_jogada(1)

    vencedor = verificar_vitoria()
    if vencedor:
        print(f'\nPlayer {vencedor} venceu!')
        mostrar_tabuleiro()
        break

    if verificar_empate():
        print('\nEmpate!')
        mostrar_tabuleiro()
        break

    fazer_jogada(2)

    os.system('cls')

    vencedor = verificar_vitoria()
    if vencedor:
        print(f'\nPlayer {vencedor} venceu!')
        mostrar_tabuleiro()
        break

    if verificar_empate():
        print('\nEmpate!')
        mostrar_tabuleiro()
        break