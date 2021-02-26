from time import sleep
cont = 0
listanum = list()
while True:
    num = int(input('Insira um número: '))
    print('processando', end='')
    for t in range(0, 3):
        sleep(0.5), print('.', end='')
    if num not in listanum:
        listanum.append(num)
        print('\nNúmero cadastrado com sucesso!')
    else:
        print('\nNúmero duplicado, não adicionado!')
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Quer continuar [S/N]? ')).strip().upper()
    if escolha == 'N':
        break
print('══' * 15)
print('Você digitou os números: ', end='')
ordem = sorted(listanum)
for n in ordem:
    cont += 1
    if n != ordem[-1]:
        print(n, end=' - ')
    else:
        print(n, end='')
