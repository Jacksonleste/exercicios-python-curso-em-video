<<<<<<< HEAD
salario = float(input('\033[30;1mqual seu salário atual? R$'))
if salario > 1250:
    porcentagem = 10
    aumento = ((salario*10)/100)+salario
else:
    porcentagem = 15
    aumento = ((salario*15)/100)+salario
print('quem ganhava \033[31mR${:.2f}\033[30m, passará a ganhar \033[34mR${:.2f}\033[30m'
=======
salario = float(input('\033[30;1mqual seu salário atual? R$'))
if salario > 1250:
    porcentagem = 10
    aumento = ((salario*10)/100)+salario
else:
    porcentagem = 15
    aumento = ((salario*15)/100)+salario
print('quem ganhava \033[31mR${:.2f}\033[30m, passará a ganhar \033[34mR${:.2f}\033[30m'
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
      '\no aumento será de \033[33m{}%\033[m.'.format(salario, aumento, porcentagem))