import modulo as ma

def main():
    while True:
        print('Calculadora')
        print('1 soma')
        print('2. subtração')
        print('3. Multiplicar')
        print('4. Dividir')
        print('5. Limpar terminal')

        opcao = input('Digite a opção desejada: ')
        match opcao:
            case '1':
                print('-----SOMA-----')
                num1 = int(input('Digite um numero para somar: '))
                num2 = int(input('Digite outro numero para somar: '))
                result = ma.soma(num1,num2)
                print(f'Resultado: {result}')
                break
            case '2':
                print('-----SUBTRAÇÃO-----')
                num1 = int(input('Digite um numero para subtrair: '))
                num2 = int(input('Digite outro numero para subtrair: '))
                result = ma.sub(num1,num2)
                print(f'Resultado: {result}')
                break
            case '3':
                print('-----MULTIPLICAÇÃO-----')
                num1 = int(input('Digite um numero para multiplicar: '))
                num2 = int(input('Digite outro numero para multiplicar: '))
                result = ma.multi(num1,num2)
                print(f'Resultado: {result}')
                break
            case '4':
                print('-----DIVISÃO-----')
                num1 = int(input('Digite um numero para dividir: '))
                num2 = int(input('Digite outro numero para dividir: '))
                result = ma.divisao(num1,num2)
                print(f'Resultado: {result}')
                break
            case '5':
                ma.limppar_terminal
                break
            case _ :
                print('Opção invalida!')