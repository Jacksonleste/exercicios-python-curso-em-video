<<<<<<< HEAD
listanum = list()
for c in range(0, 5):
    num = int(input('Insira um valor: '))
    if c == 0:
        listanum.append(num)
        print('Adicionado ao final da lista...')
    else:
        for lugar, n in enumerate(listanum):
            if num < n:
                listanum.insert(lugar, num)
                print(f'Adicionado na posição {lugar}')
                break
            elif num > listanum[-1]:
                listanum.append(num)
                print(f'Adicionado ao final da lista')
                break
print('══' * 30)
print(f'os valores digitados em ordem foram: {listanum}')
=======
listanum = list()
for c in range(0, 5):
    num = int(input('Insira um valor: '))
    if c == 0:
        listanum.append(num)
        print('Adicionado ao final da lista...')
    else:
        for lugar, n in enumerate(listanum):
            if num < n:
                listanum.insert(lugar, num)
                print(f'Adicionado na posição {lugar}')
                break
            elif num > listanum[-1]:
                listanum.append(num)
                print(f'Adicionado ao final da lista')
                break
print('══' * 30)
print(f'os valores digitados em ordem foram: {listanum}')
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
