print('''{}
SEQUÊNCIA DE FIBONACCI
{}'''.format(12 * '=-', 12 * '=-'))
num = int(input('insira um número:'))
cont = 2
n1 = 0
n2 = 1
print('{} → {} → '.format(n1, n2), end='')
while cont != num:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print('{} → '.format(n3), end='')
    cont = cont + 1
print('FIM')
