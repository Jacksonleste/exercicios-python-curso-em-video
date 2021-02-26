lista = list()
pares = list()
impares = list()
while True:
    lista.append(int(input('\033[1mInsira um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
for v in lista:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('═•' * 30)
print(f'Você digitou os números: {lista}')
print(f'Os números pares são: {pares}')
print(f'E os ímpares são: {impares}')
