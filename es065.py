pross = 'S'
cont = soma = 0
while pross == 'S':
    n = int(input('insira um número:'))
    pross = str(input('quer digitar mais um número [S/N]?')).strip().upper()
    cont += 1
    soma += n
    media = soma / cont
print('a média dos {} números digitados é {}'.format(cont, media))