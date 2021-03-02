<<<<<<< HEAD
l = float(input('insira a largura da parede em Metros:'))
h = float(input('isira a altura da parede em Metros:'))
a = l*h
tin = a/2
print('\033[30;1ma sua parede tem uma dimensão de \033[36;1m{} x \033[36m{}\033[30m, '
=======
l = float(input('insira a largura da parede em Metros:'))
h = float(input('isira a altura da parede em Metros:'))
a = l*h
tin = a/2
print('\033[30;1ma sua parede tem uma dimensão de \033[36;1m{} x \033[36m{}\033[30m, '
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
      'e sua área é de \033[36;1m{:.3f}m²\033[30;1m, e serão nescessários \033[36;1m{:.3f}L\033[30m de tinta.'.format(l, h, a,tin))