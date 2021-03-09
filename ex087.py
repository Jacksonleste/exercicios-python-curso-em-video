spar = 0
matriz = [[], [], []]
for c in range(0, 3):
    matriz[0].append(int(input(f'Digite um valor para {0}/{c}: ')))
for c in range(0, 3):
    matriz[1].append(int(input(f'Digite um valor para {1}/{c}: ')))
for c in range(0, 3):
    matriz[2].append(int(input(f'Digite um valor para {2}/{c}: ')))
print()
print('•═'  * 20)
for n in matriz:
    for c in n:
        if c % 2 == 0:
            spar += c
        print(f'[{c:^5}] ', end='')
    print()
soma3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print('•═'  * 20)
print(f'A soma de todos os valores pares é igual a: {spar}')
print(f'A soma dos números da terceira coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')