<<<<<<< HEAD
print('GERADOR DE PA')
print('=-' * 10)
termo1 = int(input('Insira o primeiro termo: '))
raz = int(input('insira a razão: '))
pa = termo1
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont != total:
        cont = cont + 1
        pa = pa + raz
        print(pa, end=' → ')
    print('PAUSA')
    mais = int(input('quantos termos você quer mostar a mais? '))
=======
print('GERADOR DE PA')
print('=-' * 10)
termo1 = int(input('Insira o primeiro termo: '))
raz = int(input('insira a razão: '))
pa = termo1
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont != total:
        cont = cont + 1
        pa = pa + raz
        print(pa, end=' → ')
    print('PAUSA')
    mais = int(input('quantos termos você quer mostar a mais? '))
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
print('você encerou o programa! foram mortrados {} termos dessa PA'.format(total))