from time import sleep
from random import randint


def sorteia(lista):
    print('Sorteando 5 valores: ', end='')
    for n in range(0,5):
        num = randint(0, 10)
        numeros.append(num)
        sleep(0.4)
        print(num, end=' ')
def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma +=n


    print(f'\nSomando os valores pares de {lista}, temos {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)
