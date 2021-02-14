print('\033[31;1m{}VERIFICAR SE UM NÚMERO É IMPAR OU PAR{}'.format(6*'--=', 6*'=--'))
num = int(input('\033[30mInsira um número:'))
result = num%2
if result == 0:
    print('O número \033[34m{}\033[30m é um número par.'.format(num))
else:
    print('O número \033[34m{}\033[30m é um número impar.'.format(num))