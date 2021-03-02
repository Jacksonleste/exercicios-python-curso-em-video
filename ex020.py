<<<<<<< HEAD
from random import shuffle
a1 = str(input('\033[30;1mPrimeiro Aluno:'))
a2 = str(input('Primeiro Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
=======
from random import shuffle
a1 = str(input('\033[30;1mPrimeiro Aluno:'))
a2 = str(input('Primeiro Aluno: '))
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
print('a ordem de apresentação será:\n \033[34m{}\033[m'.format(lista))