mais18 = totalhomem = menor20 = 0
while True:
    idade = int(input('insira sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('insira seu sexo [M/F]: ')).strip().upper()
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Quer continuar [S/N]?')).strip().upper()
    if idade >= 18:
        mais18 += 1
    if sexo == 'M':
        totalhomem += 1
    if sexo == 'F' and idade < 20:
        menor20 += 1
    if mais == 'N':
        print('PROGRAMA FINALIZADO!')
        break
    print('=-' * 15)
print(' ')
print('FORAM CADASTRADOS:')
print(f'{mais18} pessoas com mais de 18 anos.')
print(f'{totalhomem} Homens')
print(f'{menor20} Mulheres com menos de 20 anos')
