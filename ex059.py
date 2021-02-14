escolha = 0
n1 = float(input('insira um número:'))
n2 = float(input('insira outro número:'))
while escolha != 5:

    escolha = 0

    escolha = int(input('''
------------------------
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Finalizar programa
    
qual sua escolha: '''))
    if escolha == 1:
        print('A soma dos dos valores {} + {} é igual a {}'.format(n1, n2, n1 + n2))
    elif escolha == 2:
        print('o resultado de {} X {} é igual a {}'.format(n1, n2, n1 * n2))
    elif escolha == 3:
        if n1 > n2:
            print('o número {} é maior que o {}'.format(n1, n2))
        else:
            print('o número {} é maior que o {} '.format(n2, n1))
    elif escolha == 4:
        print('↓ insira novos números abaixo ↓')
        n1 = float(input('insira um número: '))
        n2 = float(input('insira outro número: '))
    elif escolha == 5:
        print('programa finalizado!')
        break
    else:
        print('\033[31mopção inválida!\033[m')