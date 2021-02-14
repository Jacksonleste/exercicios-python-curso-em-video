prim = int(input('insira o primeiro termo de sua pa:'))
raz = int(input('agora insira a razão:'))
for c in range(prim, prim +10 * raz, raz):
    print('{} '.format(c), end='-> ')
print('FIM')