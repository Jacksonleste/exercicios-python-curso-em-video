def area(l, c):
    print(f'A área do terreno {l}x{c} é igual a {l*c}m²')


print('Controle de terrenos')
print('-'*25)
largura = int(input('insira a largura(m): '))
comprimento = int(input('insira o comprimento(m): '))

area(largura, comprimento)