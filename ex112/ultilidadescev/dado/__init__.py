def leiadinheiro(text=''):
    while True:
        n = ''
        print(text ,end='')
        n = input().replace(',', '.')
        try:
            float(n)
            n = float(n)
            break
        except:
            print('\033[31;1mValor inválido, insira um valor monetário.\033[m')
    return n