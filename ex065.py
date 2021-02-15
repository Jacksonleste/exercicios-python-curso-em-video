cont = soma = total = 0
continuar = ''
while continuar != 'N':
    num = int(input('insira um número: '))
    cont += 1
    total += num
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('quer continuar [S/N]?')).strip().upper()
print('maior: {}'.format(maior))
print('menor: {}'.format(menor))
print('média: {:.2f}'.format(total/cont))
