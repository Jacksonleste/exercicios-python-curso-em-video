<<<<<<< HEAD
print('''\033[31;1m-------------------------
comparador de valores
-------------------------\033[30m''')
num1 = int(input('insira um valor:'))
num2 = int(input('insira outro valor:'))
if num1 > num2:
    print('\033[34mo primeiro valor é maior.')
elif num1 < num2:
    print('\033[34mo segundo valor é maior.')
elif num1 == num2:
=======
print('''\033[31;1m-------------------------
comparador de valores
-------------------------\033[30m''')
num1 = int(input('insira um valor:'))
num2 = int(input('insira outro valor:'))
if num1 > num2:
    print('\033[34mo primeiro valor é maior.')
elif num1 < num2:
    print('\033[34mo segundo valor é maior.')
elif num1 == num2:
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
    print('\033[32mnão existe valor maior, os dois são iguais.')