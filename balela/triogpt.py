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


def mostrar_trincas(trincas):
    return [
        [formatar_carta(carta) for carta in trinca]
        for trinca in trincas
    ]


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


def mostrar_estado_privado(mao, trincas, mao_oponente, trincas_oponente, pilha):
    print("=== SEU ESTADO ===\n")

    print("Sua mão:")
    print(mostrar_mao(mao))

    print("\nSuas trincas:")
    print(mostrar_trincas(trincas))

    print("\n=== OPONENTE ===")
    print("Cartas na mão:", len(mao_oponente))
    print("Trincas formadas:", len(trincas_oponente))

    print("\n=== PILHA ===")
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

    input(f"Jogador {turno}, pressione Enter quando estiver pronto para ver sua mão...")
    limpar()

    if turno == 1:
        mao = mao1
        trincas = trincas1
        mao_oponente = mao2
        trincas_oponente = trincas2
    else:
        mao = mao2
        trincas = trincas2
        mao_oponente = mao1
        trincas_oponente = trincas1

    print(f"=== TURNO DO JOGADOR {turno} ===\n")

    mostrar_estado_privado(
        mao,
        trincas,
        mao_oponente,
        trincas_oponente,
        pilha
    )

    print("1 - Comprar do baralho")
    print("2 - Pegar da pilha")

    escolha = input("\nEscolha: ")

    if escolha == "1":
        if not baralho:
            print("\nBaralho vazio!")
            input("Pressione Enter...")
            break

        mao.append(baralho.pop())

    elif escolha == "2":
        if not pilha:
            print("\nPilha vazia!")
            input("Pressione Enter...")
            continue

        mao.append(pilha.pop())

    else:
        print("\nJogada inválida!")
        input("Pressione Enter...")
        continue

    # Formar trincas automaticamente
    extrair_trincas(mao, trincas)

    # Descarte obrigatório
    limpar()
    print(f"=== DESCARTE - JOGADOR {turno} ===\n")

    print("Sua mão:")
    for i, carta in enumerate(mao):
        print(f"{i + 1} - {formatar_carta(carta)}")

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

    # Verificar vitória
    if len(trincas1) >= 3 or len(trincas2) >= 3:
        break

    limpar()
    input("Passe o computador para o próximo jogador e pressione Enter...")

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