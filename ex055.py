<<<<<<< HEAD
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('insira o peso da {}º pessoa:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso foi {}Kg'.format(maior))
=======
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('insira o peso da {}º pessoa:'.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('o maior peso foi {}Kg'.format(maior))
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
print('o menor peso foi {}Kg'.format(menor))