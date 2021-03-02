continuar = 'S'
cont = soma = maior = menor = 0
while continuar == 'S':
    num = int(input('insira um número:'))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('quer digitar mais um número [S/N]?')).strip().upper()
print('=-' * 17)
print('Você digitou {} valores'.format(cont))
print('O maior valor digitado foi: {}'.format(maior))
print('O menor valor digitado foi: {}'.format(menor))
print('A média de todos os valores é {}'.format(soma / cont))
print('=-' * 17)
