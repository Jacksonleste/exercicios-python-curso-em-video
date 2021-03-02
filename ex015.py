dias = int(input('\033[30;1mquantos dias o carro ficou alugado?'))
km = float(input('quantos KM o carro andou?'))
preço1 = dias*60
preço2 = km*0.15
print('o carro ficou por \033[32m{}\033[30m dias alugados e andou um total de \033[32m{}KM\033[30m. '
      '\nsabendo que cada dia custa \033[32mR$60\033[30m e cada KM rodado custa \033[32mR$0.15\033[30m. '
      '\no total a pagar é de \033[32mR${:.3f}\033[m'.format(dias, km, (preço1+preço2)))