print(F'''{'=-' * 15}
LOJÃO DO SEU JOÃO
{'=-' * 15}''')
tot = maismil = nombarato = cont = barato = 0
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    tot += preço
    cont += 1
    if preço >= 1000:
        maismil += 1
    if cont == 1 or preço < barato:
        nombarato = nome
        barato = preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]?')).strip().upper()
    print('═' * 23)
    if resp == 'N':
        print('FIM DAS COMPRAS!')
        print('═' * 23)
        break
print(f'Total a ser pago = R${tot:.2f}')
print(f'{maismil} produtos custam mais de R$1000,00')
print(f'{nombarato} é o produto mais barato e custou R${barato:.2f}')
