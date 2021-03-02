from random import randint
from time import sleep
print('''\033[31;1m{}\033[33m
o computador vai sortear um número de 0 a 10
\033[31m{}\033[m'''.format('=-' * 22, '=-' * 22))
sleep(0.5), print('processando...'), sleep(2)
cpu = randint(0, 10)
jog = 11
tenta = 0
while jog != cpu:
    mm = ''
    jog = int(input('tente adivinhar:'))
    if jog < cpu:
        mm = 'mais'
        print('{}... Tente novamente'.format(mm))
    elif jog > cpu:
        mm = 'menos'
        print('{}... Tente novamente'.format(mm))
    tenta += 1
if tenta == 1:
    print('Parabéns, você acertou de primeira')
else:
    print('você tentou {} vezes até acertar'.format(tenta))
