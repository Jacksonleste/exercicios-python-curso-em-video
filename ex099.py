from time import sleep


def maior(*numeros):
    cont = 0
    print('══' * 25)
    print(f'Analisando os valore passados...')
    maior = 0
    for e,c in enumerate(numeros):
        if e == 0:
            maior = c
        else:
            if c > maior:
                maior = c
        print(c, end=' ')
        cont += 1
        sleep(0.4)
    print(f'foram informados {cont} valores.')
    print(f'e o maior número informado foi {maior}')
    print('══' * 25)



maior(4, 54, 98, 20, 2, 150, 3, 6, 95)
maior(2, 9, 5, 20, 34, 12, 15)
maior(5)
maior()
