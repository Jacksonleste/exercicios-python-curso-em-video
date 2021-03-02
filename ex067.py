    num = int(input('Quer ver a tabuada de qual número: '))
    print('═' * 35)
    if num < 0:
        print('FIM DO PROGRAMA, VOLTE SEMPRE!')
        break
    for c in range(0, 11):
        print(f'{num} x {c} = {num * c}')
    print('═' * 35)