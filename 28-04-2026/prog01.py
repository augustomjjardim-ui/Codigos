'''
    sorteios
'''

import os
import random



lista_nomes=['Dragon','Daniel','Divon','Henk','Kamila','Kratos','Kalice',
             'Enki','Cristian','Mikan','Sistra','Rimuru','Subaru','Senku',
             'Kafka','Gong jo','Itadori','Frieren','Dawn','Augusto']



lista_sorteados=[]
sorteados = 0
while sorteados < 5:
    nome_sorteado = random.choice(lista_nomes)
    print(f'Sorteado: {nome_sorteado}')
    lista_sorteados.append(nome_sorteado)

    print(f'Lista atualizada {len(lista_nomes)}')

    lista_nomes.remove(nome_sorteado)

    print(f'Lista atualizada {len(lista_nomes)}')
    sorteados +=1

print('Fim do programa')