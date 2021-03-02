from random import choice
from time import sleep

jog = int(input('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA
Qual sua jogada? '''))
if jog == 1 or jog == 2 or jog == 3:
    if jog == 1:
        jog = 'Pedra'
    elif jog == 2:
        jog = 'Papel'
    elif jog == 3:
        jog = 'Tesoura'
    cpu = choice(['Pedra', 'Papel', 'Tesoura'])
    sleep(1), print('JO', end=''),
    sleep(1), print('KEN')
    sleep(1), print('PO!!!')
    sleep(0.3), print(12 * '=-')
    print('Computador jogou {}'.format(cpu))
    print('Jogador jogou {}'.format(jog))
    print(12 * '=-')
    if jog == 'Tesoura' and cpu == 'Papel' or jog == 'Papel' and cpu == 'Pedra' or jog == 'Pedra' and cpu == 'Tesoura':
        print('JOGADOR VENCE')
    elif jog == cpu:
        print('EMPATE')
    else:
        print('COMPUTADOR VENCE')
else:
    print('JOGADA INVÁLIDA, TENTE NOVAMENTE.')
