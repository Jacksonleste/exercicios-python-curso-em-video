print("══" * 20)
print(f'{"TABELA DE PREÇOS":^40}')
print('══' * 20)
lista = ('Computador', 2700,
         'Notebook', 1500,
         'Mouse', 19.90,
         'Teclado', 149.85,
         'Headset', 189.45,
         'joystick', 155.45,
         'Película', 25)
for c in lista:
    if lista.index(c) % 2 == 0:
        print(f'{c:.<30}R$', end=' ')
    else:
        print(f'{c:.2f}')
print('══' * 20)