num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    perg = int(input('Insira um número de 0 a 20: '))
    if 0 <= perg <= 20:
        break
    else:
        print('Valor inválido, tente novamente!')
print(f'Você digitou o número {num[perg]}')
