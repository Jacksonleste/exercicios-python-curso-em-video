frase = str(input('insira uma frase:'))
separar = frase.replace('', ' ').split()
junt = ''.join(separar)
inv = (junt[::-1])
print('o inverso de {} é {}'.format(junt, inv))
if junt == inv:
    print('a frase digitada é um palíndromo'.format(frase))
else:
    print('a frase digitada não é um palíndromo'.format(frase))
