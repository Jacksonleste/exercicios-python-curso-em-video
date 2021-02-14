n = float(input('\033[30;1mpreço antes da promoção: \033[32R$'))
d = n - ((5/100)*n)
print('\033[30;1mo valor do produto com \033[31m5%\033[30m de desconto é de \033[32mR${:.2f}'.format(d))