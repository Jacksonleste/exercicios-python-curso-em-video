<<<<<<< HEAD
from random import choice
from time import sleep
print('\033[36;1m{}JOGO DA ADIVINHAÇÃO{}\033[30m'.format(6*'>', 6*'<'))
sorteio = choice([0, 1, 2, 3, 4, 5])
print('o computador vai sortear um número de 0 a 5.'), sleep(2)
print('\033[33mSorteando...'), sleep(3)
resposta = int(input('\033[30mTente adivinhar que número o Computador sorteou:'))
print('\033[33mprocessando...\033[m'), sleep(3)
if sorteio == resposta:
    print('\033[32;1mParabéns, você acertou!!\033[m')
else:
=======
from random import choice
from time import sleep
print('\033[36;1m{}JOGO DA ADIVINHAÇÃO{}\033[30m'.format(6*'>', 6*'<'))
sorteio = choice([0, 1, 2, 3, 4, 5])
print('o computador vai sortear um número de 0 a 5.'), sleep(2)
print('\033[33mSorteando...'), sleep(3)
resposta = int(input('\033[30mTente adivinhar que número o Computador sorteou:'))
print('\033[33mprocessando...\033[m'), sleep(3)
if sorteio == resposta:
    print('\033[32;1mParabéns, você acertou!!\033[m')
else:
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
    print('\033[31;1mNão foi dessa vez, o número sorteado foi {}\033[m'.format(sorteio))