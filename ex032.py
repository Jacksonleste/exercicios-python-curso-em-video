from datetime import datetime
ano = int(input('\033[30;1mInsira um ano qualquer para verificar se ele é bissexto:(coloque 0 para o ano atual)'))
if ano == 0:
    ano = datetime.now().year
if ano%4 == 0 and ano%400 == 0 or ano%100 ==0:
    print('\033[34m{}\033[30m é um ano bissexto.'.format(ano))
else:
    print('\033[34m{}\033[30m não é um ano bissexto.'.format(ano))
