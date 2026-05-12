# função com parametro e retorno
#def funcao_segundo_grau(a,b,c):
#    return a +b +c

# chamando a funcao e armazenando
#x = funcao_segundo_grau(1,2,3)
#print(x)

'''def soma(a,b):
    resultado = a+b
    return resultado

num1 = int(input('Digite um numero qualquer'))
num2 = int(input('Digite um numero qualquer'))

resultado = soma(num1,num2)
print(resultado)'''


def mostrar_saudacao(nome):
    print(f'Olá {nome}, seja bem-vindo!')

mostrar_saudacao('Pão')

# função recursiva
def fatorial(n):
    #n!
    return 1 if n == 0 else n*fatorial(n-1)

import os

# funções lambda
somar = lambda x, y: x+y
limpar = lambda:os.system('cls' if os.name == 'nt' else 'clear')

# algoritimo principal
if __name__ == '__main__':
    try:
        x = int(input('Informe o valor de x: '))
        y = int(input('Informe o valor de y: '))
        result = somar(x,y)

        limpar()
        print(f'O resultado da soma é {result}.')
    except Exception as e:
        print(f'Não foi possivel somar {e}.')