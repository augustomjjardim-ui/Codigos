# for 

# laço de for, ele é finito: quando eu sei o número de repetições
frutas = ["melancia","abacaxi",'melão', 'pera']
fruta = "melancia"

#for f in frutas:
#    print(f)

#for range(inicio,fim,salto)

#for i in range(1,20,2):
#    print(i)
'''
num = float(input("Digite um número para saber sua tabuada: ").replace(",","."))

for i in range(11):
    print(f"{i} X {num} = {i*num}")'''



lista_nomes=['Dragon','Daniel','Divon','Henk','Kamila','Kratos','Kalice',
             'Enki','Cristian','Mikan','Sistra','Rimuru','Subaru','Senku',
             'Kafka','Gong jo','Itadori','Frieren','Dawn']

for i,nome in enumerate(lista_nomes):
    print(f'{i+1}º {nome}')


nome_buscar = input("Digite um nome: ").title()

if nome_buscar in lista_nomes:
    print('Usuario enccontrado!')