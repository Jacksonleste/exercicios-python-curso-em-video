from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os  valores sorteados foram: ', end='')
for c in num:
    print(c, end=' ')
print(f'\nO maior número sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')
