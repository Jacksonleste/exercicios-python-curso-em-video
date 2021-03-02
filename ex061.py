print('GERADOR DE PA')
print('=-' * 10)
termo1 = int(input('Insira o primeiro termo: '))
raz = int(input('insira a razão: '))
pa = termo1
cont = 0
while cont != 10:
    cont = cont + 1
    pa = pa + raz
    print(pa, end=' → ')
print('FIM')
