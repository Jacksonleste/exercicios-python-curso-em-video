print('\033[31;1m{}CALCULADORA DE MULTAS{}\033[30m'.format(6 * '>', 6 * '<'))
v = int(input('\033[30;1mQual a velocidade do veículo em KM/H?'))
m = (v - 80) * 7
if v > 80:
    print('\033[31mVocê foi multado\n\033[33mO valor da multa é de R${}.'.format(m))
else:
    print('\033[32mParabéns, Você não foi multado.')
