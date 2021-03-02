from datetime import datetime

sexo = str(input('''\033[1mdigite [F] para feminino e [M] para masculino
insira seu sexo:''')).upper()
if sexo == 'M':
    ano = int(input('insira o ano de seu nascimento: '))
    atual = datetime.now().year
    idade = atual - ano
    print('você nasceu em {} e tem {} anos em {}'.format(ano, idade, atual))
    if idade < 18:
        print('ainda faltam {} anos para você se alistar.'.format((idade - 18) * -1))
        print('seu alistamento vai ser em {}'.format(ano + 18))
    elif idade == 18:
        print('já está na hora de você se alistar.')
    elif idade > 18:
        print('já se passaram {} anos do tempo de se alistar.'.format((18 - idade) * -1))
        print('seu alistamento foi em {}'.format(atual - (18 - idade) * - 1))
elif sexo == 'F':
    print('Você é do sexo feminino e não faz parte do alistamento obrigatório.')
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
