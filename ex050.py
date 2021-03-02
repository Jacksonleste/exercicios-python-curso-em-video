<<<<<<< HEAD
soma = 0
cont = 0
for num in range(1, 7):
    num = int(input('insira o {}º número:'.format(num)))
    if num % 2 == 0:
        soma += num
        cont += 1

=======
soma = 0
cont = 0
for num in range(1, 7):
    num = int(input('insira o {}º número:'.format(num)))
    if num % 2 == 0:
        soma += num
        cont += 1

>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
print('a soma entre os {} números pares digitados é {}'.format(cont, soma))