n = int(input('insira um número:'))
d = n*2
t = n*3
r = n**(1/2)
print('o número que você digitou foi: \033[36;1m{}\033[m'
      '\nseu dobro é: \033[36;1m{}\033[m'
      '\nseu triplo é: \033[36;1m{}\033[m'
      '\nsua raiz quadrada é: \033[36;1m{:0.3}\033[m'.format(n, d, t, r))
