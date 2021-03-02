cont = 0
num = int(input('insira um número:'))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m {} \033[m'.format(c), end=' ')
        cont = cont + 1
    else:
        print('\033[34m {} \033[m'.format(c), end=' ')
print(end='''
''')
print('o número \033[32m{}\033[m é divisivel \033[32m{}\033[m vezes,'.format(num, cont), end=' ')
if cont > 2:
    print('portanto não é um número primo'.format(num))
else:
    print('portanto é um número primo'.format(num))
