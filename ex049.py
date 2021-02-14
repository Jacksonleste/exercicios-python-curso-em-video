from time import sleep
n = int(input('\033[30;1minsira um número para ver sua tabuada: '))
print('=-' * 7)
print(' TABUADA DE {}'.format(n))
print('=-' * 7)
for c in range(1, 11):
    sleep(0.4)
    print('\033[33;1m{} X {} = \033[34m{}\033[m'.format(n, c, n * c))
print('=-' * 7)
input()
