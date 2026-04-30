# NOTE: Boletim Escolar 2.0

import os

os.system("cls")

print("Boletim escolar")

lista_notas =[]
nome = input("Digite o nome do aluno: ").title()
curso = input("Digite o curso: ").upper()


while True:
    nota = input("Digite uma nota: ")
    nota = float(nota)
    lista_notas.append(nota)
    print(lista_notas)

    opcao = input("Deseja adicionar mais notas? (s - sim | n - não) ").lower()

    if opcao == "n":
        break

media = sum(lista_notas) / len(lista_notas)

print(media)