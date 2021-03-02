
num = int(input('\033[30;1minsira um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num//1000 % 10
print('analizando o número \033[31m{}\033[30m'.format(num))
print('''Unidade = \033[33m{}\033[30m
Dezena = \033[33m{}\033[30m
Centena = \033[33m{}\033[30m
Milhar = \033[33m{}\033[m'''.format(u, d, c, m))
