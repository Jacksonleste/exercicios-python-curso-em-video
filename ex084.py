cont = pesadas = leves = 0
nomleve = list()
nompes = list()
dados = list()
pessoas = list()
while True:
    dados.append(str(input('Insira seu nome: ')))
    dados.append(float(input('Insira seu peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]? ')).strip().upper()
    if resp == 'N':
        break
for p in pessoas:
    cont += 1
    if cont == 1:
        leves = pesadas = p[1]
    else:
        if p[1] > pesadas:
            pesadas = p[1]
        if p[1] < leves:
            leves = p[1]
print('═•' * 30 )
print(f'Foram cadastradas {cont} pessoas.')
print(f'O maior peso foi de {pesadas:.1f}KG. peso de: ', end='')
for c in pessoas:
    if c[1] == pesadas:
        print(f'[{c[0]}]', end=' ')
print(f'\nO menor peso foi de {leves:.1f}KG. peso de: ', end=' ')
for c in pessoas:
    if c[1] == leves:
        print(f'[{c[0]}]', end=' ')