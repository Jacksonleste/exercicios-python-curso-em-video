print('\033[31;1m-=' * 15)
print('\033[33manalizador de triângulos')
print('\033[31m-=' * 15)
a = float(input('\033[30mprimeiro segmento:'))
b = float(input('segundo segmento:'))
c = float(input('terceiro segmento:'))
if (b - c) < a < b + c and (a - c) < b < a + b and (a - b) < c < a + b:
    print('segundo a condição de existência os segmentos acima \033[32mPODEM\033[30m formar um triângulo.')
else:
    print('segundo a condição de existência os segmentos acima \033[31mNÃO PODEM\033[30m formar um triângulo.')
