# Jogo da Velha
import os
import time
# Tabuleiro
tabuleiro = ['0']*9
def mostrar_tabuleiro():
    for i in range(len(tabuleiro)):
        if i == '1':
            tabuleiro[i] = 'X'
        elif i == '2':
            tabuleiro[i] = 'O'
    print(f' {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}')
    print( '---+---+---')
    print(f' {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}')
    print( '---+---+---')
    print(f' {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}')
# Fazendo uma jogada
def fazer_jogada(jogador):
    while True:
        pos = input(f'Onde deseja jogar, player {jogador}? ')-1
        if pos < 0 or pos > 8:
            print('Posição invalida!')
            continue
        elif tabuleiro[pos] != '0':
            print('Posição ocupada')
            continue
        else:
            tabuleiro[pos] = jogador
            break
# Hora do jogo
while True:
    mostrar_tabuleiro()
    fazer_jogada('1')