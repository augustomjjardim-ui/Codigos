import random
import os


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def criar_baralho():
    baralho = []
    naipes = ['^', 'v', '*', 'X']

    for valor in range(1, 14):
        for naipe in naipes:
            baralho.append((valor, naipe))

    random.shuffle(baralho)
    return baralho


def formatar_carta(carta):
    valor, naipe = carta

    nomes = {
        1: 'A',
        11: 'J',
        12: 'Q',
        13: 'K'
    }

    return f"{nomes.get(valor, str(valor))}{naipe}"


def mostrar_mao(mao):
    return [formatar_carta(c) for c in mao]


def extrair_trincas(mao, trincas_guardadas):
    contagem = {}

    for carta in mao:
        valor = carta[0]
        contagem.setdefault(valor, []).append(carta)

    for valor, cartas in contagem.items():
        while len(cartas) >= 3:
            trinca = cartas[:3]

            for carta in trinca:
                mao.remove(carta)

            trincas_guardadas.append(trinca)

            cartas = cartas[3:]


def mostrar_trincas(trincas):
    return [
        [formatar_carta(carta) for carta in trinca]
        for trinca in trincas
    ]


def mostrar_estado(mao1, mao2, trincas1, trincas2, pilha):
    print("=== ESTADO DO JOGO ===\n")

    print("Jogador 1:")
    print("Mão:", mostrar_mao(mao1))
    print("Trincas:", mostrar_trincas(trincas1))

    print()

    print("Jogador 2:")
    print("Mão:", mostrar_mao(mao2))
    print("Trincas:", mostrar_trincas(trincas2))

    print()

    if pilha:
        print("Carta da pilha:", formatar_carta(pilha[-1]))
    else:
        print("Pilha vazia")

    print()


# -------------------------
# INÍCIO DO JOGO
# -------------------------

baralho = criar_baralho()

mao1 = [baralho.pop() for _ in range(9)]
mao2 = [baralho.pop() for _ in range(9)]

trincas1 = []
trincas2 = []

pilha = [baralho.pop()]

extrair_trincas(mao1, trincas1)
extrair_trincas(mao2, trincas2)

turno = 1


# -------------------------
# LOOP PRINCIPAL
# -------------------------

while True:
    limpar()

    print(f"=== TURNO DO JOGADOR {turno} ===\n")

    mostrar_estado(mao1, mao2, trincas1, trincas2, pilha)

    mao = mao1 if turno == 1 else mao2
    trincas = trincas1 if turno == 1 else trincas2

    print("1 - Comprar do baralho")
    print("2 - Pegar da pilha")

    escolha = input("\nEscolha: ")

    if escolha == "1":
        if not baralho:
            print("\nBaralho vazio!")
            input("Pressione Enter...")
            break

        carta = baralho.pop()
        mao.append(carta)

    elif escolha == "2":
        if not pilha:
            print("\nPilha vazia!")
            input("Pressione Enter...")
            continue

        carta = pilha.pop()
        mao.append(carta)

    else:
        print("\nJogada inválida!")
        input("Pressione Enter...")
        continue

    # FORMAR TRINCAS AUTOMATICAMENTE
    extrair_trincas(mao, trincas)

    # DESCARTE OBRIGATÓRIO
    limpar()

    print(f"=== DESCARTE - JOGADOR {turno} ===\n")

    print("Sua mão:")
    for i, carta in enumerate(mao):
        print(f"{i+1} - {formatar_carta(carta)}")

    while True:
        try:
            indice = int(input("\nEscolha uma carta para descartar: ")) - 1

            if 0 <= indice < len(mao):
                descartada = mao.pop(indice)
                pilha.append(descartada)
                break
            else:
                print("Índice inválido.")

        except ValueError:
            print("Entrada inválida.")

    # VERIFICAR VITÓRIA
    if len(trincas1) >= 3 or len(trincas2) >= 3:
        break

    turno = 2 if turno == 1 else 1


# -------------------------
# FIM DE JOGO
# -------------------------

limpar()

print("=== FIM DE JOGO ===\n")

print("Jogador 1:")
print("Mão Final:", mostrar_mao(mao1))
print("Trincas:", mostrar_trincas(trincas1))
print("Total de Trincas:", len(trincas1))

print("\nJogador 2:")
print("Mão Final:", mostrar_mao(mao2))
print("Trincas:", mostrar_trincas(trincas2))
print("Total de Trincas:", len(trincas2))

print("\n=== RESULTADO ===")

if len(trincas1) > len(trincas2):
    print("🏆 Jogador 1 venceu!")
elif len(trincas2) > len(trincas1):
    print("🏆 Jogador 2 venceu!")
else:
    print("🤝 Empate!")