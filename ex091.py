from random import randint
from time import sleep
from operator import itemgetter
cont = 1
jogadas = dict()
jogadas['jogador1'] = randint(1,6)
jogadas['jogador2'] = randint(1,6)
jogadas['jogador3'] = randint(1,6)
jogadas['jogador4'] = randint(1,6)
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('•═' * 20)
cont = 1
for k, v in ranking:
    print(f'{cont}º Lugar: {k} - {v}')
    cont += 1
    sleep(1)
