"""
    TIPOS DE DADOS
"""

str()
int()
bool()
float()

""" variavel com valor definido
nomea = "karython Gomes"
idadea = 27
alturaa = 1.75
professaor = True
"""


# entrada de dados

nome = input("Digite o seu nome: ")
data = input("Digite sua data de nascimento: ")
peso = input("Digite seu peso: ")
altura = input("Digite sua altura: ")

print(f"Olá {nome} seja bem vindo ao sistema Python!\nAqui estão as suas informações: \n Data de nascimento: {data}\n Altura: {altura}\n  Peso: {peso}")

print(type(nome))

"""
desenvolva um sistema que receba do usuario
seu nome, data de nascimento, peso e altura
Formate a saida para aparecer na tela do usuario:
Olá {nome_informado}, seja bem vindo ao sistema Python!
Aqui estão as suas informações:
    Data Nascimento:
    Altura:
    Peso:
"""