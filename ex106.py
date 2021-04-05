def escreva(m, cor=False):
    if cor == 'azu':
        cor = '\033[34m'
    if cor == 'verm':
        cor = '\033[31m'
    if cor == 'amare':
        cor = '\033[33m'
    tam = len(m) + 2
    print(f'{cor}═' * tam)
    print(f' {m} ')
    print('═' * tam, end='')
    print('\033[m')


while True:
    escreva('PyHelp', 'azu')
    fun = str(input('\033[1;37mFunção desejada >>> ')).lower().strip()
    if fun == 'fim':
        escreva('PROGRAMA FINALIZADO COM SUCESSO!', 'verm')
        break
    escreva(f'acessando manual de {fun}', 'amare')
    print(f'\033[32m')
    help(fun)
    print('\033[m')
    print()