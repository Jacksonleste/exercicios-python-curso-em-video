from random import choice
a1 = str(input('\033[30;1mPrimeiro Aluno:'))
a2 = str(input('Segundo Aluno:'))
a3 = str(input('Terceiro Aluno:'))
a4 = str(input('Quarto Aluno:'))
sor = choice([a1, a2, a3, a4])
print('O Aluno escolhido foi \033[34m{}\033[m'.format(sor))
