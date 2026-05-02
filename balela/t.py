contador = 0
result = 0
num = int(input("Digite um número: "))
while contador <= 10:
    result=num*contador
    print(f"{num} X {contador} = {result}")
    contador+=1