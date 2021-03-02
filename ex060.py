<<<<<<< HEAD
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
=======
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
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
print(mult)