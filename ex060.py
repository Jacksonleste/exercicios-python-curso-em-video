num = int(input('Insira um número para ver seu fatorial: '))
mult = 1
print('{}! = '.format(num), end='')
while num != 0:
    mult = num * mult
    if num == 1:
        print('{} = '.format(num), end='')
    else:
        print('{} x '.format(num), end='')
    num -= 1
print(mult)