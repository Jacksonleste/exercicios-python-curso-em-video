def leiaint(tex=None):
    """recebe somente valores inteiros.

    :param tex: texto da entrada, defaults to None
    :type tex: [type], optional
    :return: [description]
    :rtype: [type]
    """
    while True:
        print(tex, end='')
        num = input().strip()
        if num.isnumeric() == False:
            print('\033[31;1mValor inválido, insira um número!\033[m')
        else:
            break
    return num


num = leiaint('Insira um número: ')
print(f'Você acabou de digitar um número {num}.')
