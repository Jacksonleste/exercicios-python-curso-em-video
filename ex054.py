from datetime import datetime

maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input('insira o ano de nascimento da {}º pessoa:'.format(c)))
    idade = datetime.now().year - ano
    if idade < 21:
        menor += 1
    else:
        maior += 1
print('''
Ao todo temos {} pessoas maiores de de idade'''.format(maior))
print('e também temos {} menores'.format(menor))
