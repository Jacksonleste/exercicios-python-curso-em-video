<<<<<<< HEAD
contcinq = contvint = contdez = contum = 0
print(f'''{'═' * 23}
    BANCO PYTHON
{'═' * 23}''')
num = int(input('qual o valor a ser sacado: R$'))
while True:
    cinq = num - 50
    vint = num - 20
    dez = num - 10
    um = num - 1
    if cinq >= 0:
        num = cinq
        contcinq += 1
    elif vint >= 0:
        contvint += 1
        num = vint
    elif dez >= 0:
        contdez += 1
        num = dez
    elif um >= 0:
        contum += 1
        num = um
    else:
        break
if contcinq > 0:
    print(f'Total de {contcinq} cédulas de R$50')
if contvint > 0:
    print(f'Total de {contvint} cédulas de R$20')
if contdez > 0:
    print(f'Total de {contdez} cédulas de R$10')
if contum > 0:
    print(f'Total de {contum} cédulas de R$1')
print(f'''{'═' * 23}
    VOLTE SEMPRE!''')
=======
contcinq = contvint = contdez = contum = 0
print(f'''{'═' * 23}
    BANCO PYTHON
{'═' * 23}''')
num = int(input('qual o valor a ser sacado: R$'))
while True:
    cinq = num - 50
    vint = num - 20
    dez = num - 10
    um = num - 1
    if cinq >= 0:
        num = cinq
        contcinq += 1
    elif vint >= 0:
        contvint += 1
        num = vint
    elif dez >= 0:
        contdez += 1
        num = dez
    elif um >= 0:
        contum += 1
        num = um
    else:
        break
if contcinq > 0:
    print(f'Total de {contcinq} cédulas de R$50')
if contvint > 0:
    print(f'Total de {contvint} cédulas de R$20')
if contdez > 0:
    print(f'Total de {contdez} cédulas de R$10')
if contum > 0:
    print(f'Total de {contum} cédulas de R$1')
print(f'''{'═' * 23}
    VOLTE SEMPRE!''')
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
