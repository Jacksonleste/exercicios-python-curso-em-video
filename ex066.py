soma = cont = 0
while True:
    num = int(input('insira um número [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print('')
print(f'A soma dos {cont} números digitados é {soma}')
