<<<<<<< HEAD
num = (int(input('insira um número: ')), int(input('insira um número: ')),
       int(input('insira um número: ')), int(input('insira um número: ')))
print(f'O valor 9 apareceu {num.count(9)} vezes')
cont3 = num.count(3)
if cont3 > 0:
    print(f'O valor 3 foi visto primeiramente na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi encontrado')
print('Os números pares digitados são: ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
=======
num = (int(input('insira um número: ')), int(input('insira um número: ')),
       int(input('insira um número: ')), int(input('insira um número: ')))
print(f'O valor 9 apareceu {num.count(9)} vezes')
cont3 = num.count(3)
if cont3 > 0:
    print(f'O valor 3 foi visto primeiramente na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi encontrado')
print('Os números pares digitados são: ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
