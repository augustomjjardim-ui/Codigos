import random


# =========================
# MODIFICADORES
# =========================
def aplicar_kh(rolagens, valor):
    return sorted(rolagens, reverse=True)[:valor]


def aplicar_kl(rolagens, valor):
    return sorted(rolagens)[:valor]


def aplicar_dl(rolagens, valor):
    return sorted(rolagens)[valor:]


def aplicar_dh(rolagens, valor):
    return sorted(rolagens)[:-valor]


MODIFICADORES = {
    'kh': aplicar_kh,
    'kl': aplicar_kl,
    'dl': aplicar_dl,
    'dh': aplicar_dh
}


# =========================
# TOKENIZER REAL
# =========================
def tokenizar_expressao(expressao):
    tokens = []
    atual = ''

    operadores = set('+-*/()')

    for char in expressao:
        if char in operadores:
            if atual:
                tokens.append(atual)
                atual = ''

            tokens.append(char)

        else:
            atual += char

    if atual:
        tokens.append(atual)

    return tokens


# =========================
# SHUNTING YARD
# =========================
def para_rpn(tokens):
    precedencia = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    saida = []
    operadores = []

    for token in tokens:
        if token not in precedencia and token not in '()':
            saida.append(token)

        elif token in precedencia:
            while (
                operadores
                and operadores[-1] != '('
                and precedencia[operadores[-1]] >= precedencia[token]
            ):
                saida.append(operadores.pop())

            operadores.append(token)

        elif token == '(':
            operadores.append(token)

        elif token == ')':
            while operadores and operadores[-1] != '(':
                saida.append(operadores.pop())

            operadores.pop()

    while operadores:
        saida.append(operadores.pop())

    return saida


# =========================
# PROCESSAR TERMO DE DADO
# =========================
def processar_termo(termo):
    modificador = None
    valor_mod = None

    for mod in MODIFICADORES:
        if mod in termo:
            termo, valor_str = termo.split(mod)
            modificador = mod
            valor_mod = int(valor_str)
            break

    if 'd' in termo:
        qtd_str, faces_str = termo.split('d')

        quantidade = int(qtd_str) if qtd_str else 1
        faces = int(faces_str)

        rolagens = [
            random.randint(1, faces)
            for _ in range(quantidade)
        ]

        usadas = rolagens.copy()

        if modificador:
            usadas = MODIFICADORES[modificador](usadas, valor_mod)

        return {
            'tipo': 'dado',
            'rolagens': rolagens,
            'usadas': usadas,
            'total': sum(usadas)
        }

    return {
        'tipo': 'fixo',
        'valor': int(termo),
        'total': int(termo)
    }


# =========================
# AVALIAR RPN
# =========================
def avaliar_rpn(rpn):
    pilha = []

    for token in rpn:
        if token not in '+-*/':
            resultado = processar_termo(token)

            if resultado['tipo'] == 'dado':
                texto = f'{resultado["rolagens"]}'

                if resultado['rolagens'] != resultado['usadas']:
                    texto += f' -> usados {resultado["usadas"]}'

            else:
                texto = str(resultado['valor'])

            pilha.append({
                'total': resultado['total'],
                'texto': texto
            })

        else:
            b = pilha.pop()
            a = pilha.pop()

            if token == '+':
                total = a['total'] + b['total']
            elif token == '-':
                total = a['total'] - b['total']
            elif token == '*':
                total = a['total'] * b['total']
            elif token == '/':
                total = a['total'] / b['total']

            texto = f'({a["texto"]} {token} {b["texto"]})'

            pilha.append({
                'total': total,
                'texto': texto
            })

    return pilha[0]


# =========================
# FUNÇÃO PRINCIPAL
# =========================
def rolar(expressao):
    repeticoes = 1

    if '#' in expressao:
        rep_str, expressao = expressao.split('#')
        repeticoes = int(rep_str)

    tokens = tokenizar_expressao(expressao)
    rpn = para_rpn(tokens)

    for r in range(repeticoes):
        print(f'\n=== Rolagem {r+1} ===')

        resultado = avaliar_rpn(rpn)

        print(resultado['texto'])
        print(f'TOTAL GERAL: {resultado["total"]}')


# =========================
# EXECUÇÃO
# =========================
rolar(input('Digite a rolagem: '))