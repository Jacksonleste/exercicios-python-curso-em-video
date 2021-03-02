<<<<<<< HEAD
from math import floor
print('\033[1;30;7m{}insira um número decimal para ver sua parte inteira:{}\033[30;47;0m'.format('>' * 12,'<' * 12 ))
n = float(input('\033[30;1mnumero:'))
int = floor(n)
print('a parte inteira de \033[31m{}\033[30m é \033[34m{}\033[m'.format(n, int))
#forma de fazer sem importar bibliotecas
'''num = float(input('insira um valor:'))
=======
from math import floor
print('\033[1;30;7m{}insira um número decimal para ver sua parte inteira:{}\033[30;47;0m'.format('>' * 12,'<' * 12 ))
n = float(input('\033[30;1mnumero:'))
int = floor(n)
print('a parte inteira de \033[31m{}\033[30m é \033[34m{}\033[m'.format(n, int))
#forma de fazer sem importar bibliotecas
'''num = float(input('insira um valor:'))
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
print('a parte inteira de {} é {:.0f}'.format(num, num))'''