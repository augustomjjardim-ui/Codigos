# NOTE: boletim escolar

# importa uma libary
import os

os.system("cls")

nome = input("Digite o nome do aluno: ").title()
turma = input("Digite o nome da turma: ").upper()
nota = input("Digite a primeira nota do aluno: ").replace(",",".")
nota2 = input("Digite a segunda nota do aluno: ").replace(",",".")
nota3 = input("Digite a terceira nota do aluno: ").replace(",",".")
nota4 = input("Digite a quarta nota do aluno: ").replace(",",".")
nota5 = input("Digite a quinta nota do aluno; ").replace(",",".")
os.system("cls")
nota=float(nota)
nota2=float(nota2)
nota3=float(nota3)
nota4=float(nota4)
nota5=float(nota5)

media = (nota+nota2+nota3+nota4+nota5)/5

resultado = None

if media >= 7:
    resultado = "Aprovado"
elif media>=5:
    resultado = "Rcuperação"
else:
    resultado = "Reprovado"

print(30*"-","Boletim Escolar",30*"-","\n   Nome do Aluno: ",nome," | Turma: ",turma,
      "\n   Nota1:",nota,"\n   Nota2:",nota2,"\n   Nota3:",nota3,"\n   Nota4:",nota4,"\n   Nota5:",nota5,
      "\n",76*"=",f"\nMedia: {media:.2f} | Situação: {resultado}")