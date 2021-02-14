sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('insira seu sexo [M/F]:')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('\033[31mOPÇÃO INVÁLIDA, TENTE NOVAMENTE!\033[m')
    else:
        if sexo == 'M':
            sexo = 'Masculino'
        elif sexo == 'F':
            sexo = 'Feminino'
        print('Sexo {} registrado com sucesso'.format(sexo))