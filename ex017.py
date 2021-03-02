<<<<<<< HEAD
from math import hypot
print('\033[30;1;7m{}calculador de hipotenusa{}\033[m'.format('>' * 12, '<' * 12))
co = float(input('\033[30;1mcateto oposto:'))
ca = float(input('cateto adjacente:'))
h = hypot(ca, co)
=======
from math import hypot
print('\033[30;1;7m{}calculador de hipotenusa{}\033[m'.format('>' * 12, '<' * 12))
co = float(input('\033[30;1mcateto oposto:'))
ca = float(input('cateto adjacente:'))
h = hypot(ca, co)
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
print('a hpotenusa mede \033[34m{:.2f}\033[m'.format(h))