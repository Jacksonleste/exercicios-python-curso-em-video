from random import randint
from time import sleep
cont = 0
numeros = list()
lista = list()
print('•═' * 20)
print('SORTEANDO JOGOS DA MEGA-SENA')
print('•═' * 20)
jog = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, jog): 
    for n in range(0,6):
        sorteio = randint(0 , 60)
        while True:
            if sorteio not in numeros:
                numeros.append(sorteio)
                break
            else:
                sorteio = randint(0, 60)
    lista.append(numeros[:])
    numeros.clear()
print('•═' * 20)
for l in lista:
    cont += 1
    print(f'Jogo {cont}: {sorted(l)}')
    sleep(1)
print('•═' * 20)
print('>' * 15, 'BOA SORTE', '<' * 15)
print('•═' * 20)