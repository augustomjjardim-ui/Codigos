import os
import time
from cmath import sqrt

def ler_coeficiente(texto):
    """
    Converte:
        ""   -> 1
        "+"  -> 1
        "-"  -> -1
        "2"  -> 2
        "-3" -> -3
        "2.5" -> 2.5
    """
    if texto == '' or texto == '+':
        return 1.0
    elif texto == '-':
        return -1.0
    else:
        return float(texto)

def formatar_numero(x):
    if x.imag == 0:
        return x.real
    return x

while True:
    opcao = 's'

    operacao = input('Digite a expressão: ')
    expressao = operacao.lower().replace(' ','')

    if 'x^2' in expressao:
        segugrau_str, expressao = expressao.split('x^2')
        a = ler_coeficiente(segugrau_str)
        if "x" in expressao:
            primgrau_str, expressao = expressao.split('x')
            b = ler_coeficiente(primgrau_str)
        else:
            b = 0.0
        if expressao== '':
            c = 0.0
        else:
            c = float(expressao)

        delta = b**2 - 4*a*c
        raiz_delta = sqrt(delta)

        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)

        for i in range(5,0,-1):
            print(f'Calculando...{i}')
            os.system('cls')
            time.sleep(2)
        
        print(f'O zero da expressão {operacao} é X1 = {formatar_numero(x1)} e X2 = {formatar_numero(x2)}')
        opcao = input('\nDeseja fazer mais operações? ')

    elif 'x' in expressao:
        # Separa lado esquerdo e direito
        if '=' in expressao:
            esquerda, direita = expressao.split('=')
        else:
            # Se não houver "=", assume que a expressão é igual a zero
            # Ex.: 2x+3  ->  2x+3 = 0
            esquerda = expressao
            direita = '0'

        # ----------------------------------
        # Função que extrai coeficientes
        # de uma expressão do tipo ax+b
        # ----------------------------------
        def extrair_coeficientes(expr):
            if 'x' in expr:
                a_str, resto = expr.split('x', 1)
                a = ler_coeficiente(a_str)

                if resto == '':
                    b = 0.0
                else:
                    b = float(resto)
            else:
                a = 0.0
                b = float(expr)

            return a, b

        # Extrai coeficientes dos dois lados
        a_esq, b_esq = extrair_coeficientes(esquerda)
        a_dir, b_dir = extrair_coeficientes(direita)

        # Transformar:
        # a_esq*x + b_esq = a_dir*x + b_dir
        #
        # (a_esq - a_dir)x = b_dir - b_esq
        a_final = a_esq - a_dir
        b_final = b_dir - b_esq

        # Casos especiais
        if a_final == 0:
            if b_final == 0:
                print('A equação possui infinitas soluções.')
            else:
                print('A equação não possui solução.')
        else:
            x = b_final / a_final
            print(f'O resultado da expressão {operacao} é x = {x}')
            opcao = input('\nDeseja fazer mais operações? ')
    else:
        print('Operação invalida')
    
    if opcao.lower().startswith('n'):
        break