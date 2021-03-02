<<<<<<< HEAD
num = list()
for c in range(0, 5):
    num.append(int(input(f'Insira um número para a posição {c}: ')))
maior = max(num)
menor = min(num)
print('══' * 28 )
print(f'Você digitou os valores: {num}')
print(f'o maior numéro digitado foi {maior}, e está nas posições ', end='')
for cont, n in enumerate(num):
    if n == maior:
        print(cont, end='...')
print(f'\no menor número digitado foi {menor}, e está nas posições ', end='')
for cont, n in enumerate(num):
    if n == menor:
        print(cont, end='... ')
=======
num = list()
for c in range(0, 5):
    num.append(int(input(f'Insira um número para a posição {c}: ')))
maior = max(num)
menor = min(num)
print('══' * 28 )
print(f'Você digitou os valores: {num}')
print(f'o maior numéro digitado foi {maior}, e está nas posições ', end='')
for cont, n in enumerate(num):
    if n == maior:
        print(cont, end='...')
print(f'\no menor número digitado foi {menor}, e está nas posições ', end='')
for cont, n in enumerate(num):
    if n == menor:
        print(cont, end='... ')
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
