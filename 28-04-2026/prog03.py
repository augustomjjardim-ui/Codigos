
"""
    sisstema: calculadora
"""


while True:
    print(30*'-', 'Calculadora', 30 *'-')
    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite o segundo: '))
    print('1, Soma')
    print('2, Subtração')
    print('3, Multiplicação')
    print('4, Divisão')
    opcao =input('Digite a operação: ')

    match opcao:
        case '1':
            resultado = num1 +num2
            print(f"{num1} + {num2} = {resultado}")
            break
        
        case '2':
            resultado = num1 -num2
            print(f"{num1} - {num2} = {resultado}")
            break

        case '3':
            resultado = num1 *num2
            print(f"{num1} * {num2} = {resultado}")
            break

        case '4':
            if num1 != 0 and num2 !=0:
                resultado = num1 /num2
                print(f"{num1} + {num2} = {resultado}")
            break

        case _:
            print('Digite um numero valido')