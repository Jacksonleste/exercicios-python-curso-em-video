<<<<<<< HEAD
casa = float(input('\033[30;1mInsira o valor da casa que você deseja comprar: R$'))
salário = float(input('Insira seu salário: R$'))
tempo = int(input('Em quantos anos você pretende pagar?'))
mensalidade = casa/(tempo*12)
print('para pegar uma casa de \033[36mR${}\033[30m em \033[36m{}\033[30m anos o valor da pretação vai ser de \033[36mR${:.3f}\033[30m'.format(casa,tempo,mensalidade))
if mensalidade >= salário*0.3:
    print('\033[31mdescupe, infelizmente seu empréstimo não foi aprovado\033[m')
else:
    print('\033[32mseu empréstimo foi aprovado.')
=======
casa = float(input('\033[30;1mInsira o valor da casa que você deseja comprar: R$'))
salário = float(input('Insira seu salário: R$'))
tempo = int(input('Em quantos anos você pretende pagar?'))
mensalidade = casa/(tempo*12)
print('para pegar uma casa de \033[36mR${}\033[30m em \033[36m{}\033[30m anos o valor da pretação vai ser de \033[36mR${:.3f}\033[30m'.format(casa,tempo,mensalidade))
if mensalidade >= salário*0.3:
    print('\033[31mdescupe, infelizmente seu empréstimo não foi aprovado\033[m')
else:
    print('\033[32mseu empréstimo foi aprovado.')
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
