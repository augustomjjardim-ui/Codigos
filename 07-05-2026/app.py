'''
    Manipulação de arquivos: percorrer os meus diretorios, encontrar o arquivo,
    pssar o comando de abertura do arquivo, passar comando de ação.

    arquivo = open("arquivo.txt","modo")

    modos de ação:
        - "r" : leitura do arquivo
        - "w" : escrita(sobrescreve)
        - "a" : adiciona conteudo
        - "x" : criar um arquivo
        - "b" : arquivos binarios
        - "t" : texto
'''
# Criando e escrevendo arquivo
arquivo = open('primeiro_arquivo.txt',"w")
arquivo.write('Olá mundo! Meu primeiro arquivo.')
arquivo.close()

# Lendo o arquivo
arquivo = open('primeiro_arquivo.txt',"r")
conteudo = arquivo.read()
print(conteudo)
arquivo.close()

# Aplicando boa pratica
with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# arquivo com multiplas escritas
with open('alunos.txt', "w") as arquivo:
    arquivo.write('Ana\n')
    arquivo.write('Bruna\n')
    arquivo.write('João\n')
    arquivo.write('Lucas\n')
    arquivo.write('Gomes\n')
    arquivo.write('Karython\n')

# Lendo linha a linha
with open('alunos.txt', "r") as arquivo:
    for linha in arquivo:
        print(linha)

# usando lista para escrever um arquivo
frutas = ['pera', 'abacaxi', 'melancia', 'manga', 'caju']

with open('frutas.txt', 'w') as arquivo:
    for f in frutas:
        arquivo.write(f + '\n')

# converrter arquivo em lista
with open('frutas.txt', "r") as arquivo:
    linhas = arquivo.readlines()

print(type(linhas))
print(linhas)

# Saida: ['pera\n', 'abacaxi\n', 'melancia\n', 'manga\n', 'caju\n']

#Limpar a quebra de linha

with open('frutas.txt', "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())


# exemplo para cadastro

while True:
    nome = input('Digite seu nome: ').title()

    with open("cadastro.txt", "a") as arquivo:
        arquivo.write(nome + "\n")
    
    sair =input("Deseja sair? s/n").lower()

    if sair == "s":
        break