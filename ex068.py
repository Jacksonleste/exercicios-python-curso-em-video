from random import randint

print(f'''{'=-' * 15}
VAMOS JOGAR PAR OU ÍMPAR
{'=-' * 15}''')
vit = der = 0
while True:
    cpu = randint(0, 10)
    jog = int(input('insira um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('[I/P]: ')).strip().upper()
    soma = jog + cpu
    print('-' * 60)
    print(f'O computador jogou {cpu} e você jogou {jog}. o total de {soma} ', end='')
    if soma % 2 == 0:
        print('DEU PAR')
        result = 'P'
    else:
        print('DEU ÍMPAR')
        result = 'I'
    if result == escolha:
        print('Você venceu!')
        vit += 1
    else:
        print('O computador venceu!')
        break
    print('-' * 60)
    print('Vamos jogar novamente...')
print('-' * 60)
print('FIM DO JOGO!!')
if vit >= 1:
    print('')
    print(f'Você venceu {vit} vezes')
