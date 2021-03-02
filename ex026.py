<<<<<<< HEAD
frase = str(input('\033[30;1minsira uma frase:')).strip()
print('Analisando a frase \033[33m\'{}\''.format(frase))
print('\033[30mexistem \033[31m{}\033[30m letra(s) \033[34m\'A\' '.format(frase.lower().count('a')))
print('\033[30mela aparece na primeira vez na posição \033[31m{}'.format(frase.find('a')+1))
print('\033[30me aparece pela ultima vez na posição \033[31m{}\033[m'.format(frase.rfind('a')+1))
=======
frase = str(input('\033[30;1minsira uma frase:')).strip()
print('Analisando a frase \033[33m\'{}\''.format(frase))
print('\033[30mexistem \033[31m{}\033[30m letra(s) \033[34m\'A\' '.format(frase.lower().count('a')))
print('\033[30mela aparece na primeira vez na posição \033[31m{}'.format(frase.find('a')+1))
print('\033[30me aparece pela ultima vez na posição \033[31m{}\033[m'.format(frase.rfind('a')+1))
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
