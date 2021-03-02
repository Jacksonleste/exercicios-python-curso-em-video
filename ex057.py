<<<<<<< HEAD
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
=======
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
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
        print('Sexo {} registrado com sucesso'.format(sexo))