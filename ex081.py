listanum = list()
while True:
    listanum.append(int(input('Insira um número: ')))
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]? ')).strip().upper()
    if resp == 'N':
        break
print('══' * 20)
print(f'Foram digitados {len(listanum)} números')
print('══' * 20)
print('Os valores em ordem decrescente:')
for n, l in enumerate(sorted(listanum, reverse=True)):
    ordem = sorted(listanum, reverse=True)[-1]
    if l == ordem:
        print(l)
    else:
        print(l, end=' - ')
print('══' * 20)
if 5 in listanum:
    print(f'O valor 5 está na lista na posição {listanum.index(5)}')
else:
    print('O valor 5 não foi encontrado')
print('══' * 20)