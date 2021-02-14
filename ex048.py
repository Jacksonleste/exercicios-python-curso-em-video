soma = 0
cont = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        soma = soma + c
        cont = cont + 1
print('a soma de todos os {} valores solicitados é {}'.format(cont, soma))
