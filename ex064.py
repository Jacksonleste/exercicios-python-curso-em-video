n = cont = soma = 0
while n != 999:
    n = int(input('insira um número [ 999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print('a soma de todos os {} números digitados é {}'.format(cont, soma))