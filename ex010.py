r = float(input('quantos dinheiro você possui na carteira? R$'))
d = r/5.52
eu = r/6.53
yen = r/0.053
print('\033[33;1mR${:.2f} \033[30m=> \033[34mUS${:.2f}'.format(r, d))
print('\033[33mR${:.2f} \033[30m=> \033[34m€{:.2f}'.format(r, eu))
print('\033[33mR${:.2f} \033[30m=> \033[34m¥{:.2f}'.format(r, yen))