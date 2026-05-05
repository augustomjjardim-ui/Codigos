"""
[] -> lista -> valores str, int, float e boolean | len = conta qunato tem
    +> 0,1,2...
{} -> Dicionario -> parece objeto e .json. pode ser sobreescrito
    +> objeto: {"chave" : "valor", "a" : 5}
podem se misturar
() -> Tupla -> constante
"""

lista = ['gomes','fulano', 'cicrano', 'beltrano', 'maria', 'pedro']

print(lista)

# imprimindo valor especifico
print(lista[0])

# imprimindo ultimo valor
print(lista[-1])

# imprimir intervalo
print(lista[2:4])

#ordenar essa lista
#lista.sort()

# adicionando na lista
lista.append("karython")

# inserindo em posição especifica
lista.insert(2, 'joao')

# inserindo varios valores
lista.extend(['ana', 'beatriz', 'david', 'roberto'])

numeros = []

# adicionado de forma dinamica
for i in range(10):
    numeros.append(i * 2)
#print(numeros)


# removendo de forma dinamica
print(f'lista antes de remover')

# pop - remove pelo indice, sem o indice ele remove o ultimo
lista.pop(0)

# removendo pelo valor, (remove o primeiro que achar)
lista.remove('cicrano')


lista_numeros = [n for n in range(11)]
# removendo intervalo de valores
del lista_numeros[2:4]

print(f'Lista depois de remover {lista}')

listanomes = ['gomes','fulano', 'cicrano', 'beltrano', 'maria', 'pedro']
# alterando valor da lista
listanomes[1] = 'lucas'

print(listanomes)

numeros = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(numeros)):
    if numeros[i] > 5:
        numeros[i] = numeros[i] * 2
print(numeros)

numeros2 = [10,20,30,40,50]

# list compreheision
numeros2 = [n * 2 if n>20 else n for n in numeros2]