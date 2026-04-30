operacao=input("Olá, qual é a operação de hoje? ")
num1=float(input("Digite o primeiro: ").replace(",","."))
num2=float(input("Digite o segundo: ").replace(",","."))
if(operacao=="soma"):
    resultado=num1+num2
    print(f"A soma de {num1} e {num2} é {resultado}")
elif(operacao=="subtração"):
    resultado=num1-num2
    print(f"A subtração de {num1} e {num2} é {resultado}")
elif(operacao=="multiplicação"):
    resultado=num1*num2
    print(f"A multiplicação de {num1} e {num2} é {resultado}")
elif(operacao=="divisão"):
    resultado=num1/num2
    print(f"A divisão de {num1} e {num2} é {resultado}")
else:
    print("Essa operação não é conhecida pelo sistema")