s1 = float(input('\033[30;1minsira seu salário antes do aumento:'))
p = (15/100)*s1
s2 = s1+p
print('um funcionário que recebia um salário de \033[31m>R${:.2f}<\033[30m com \033[36m15%\033[30m de aumento passa a receber \033[34m>R${:.2f}<'.format(s1, s2))