print('\033[33;1m-=' * 15)
print('\033[31manalizador de triângulos v2.0')
print('\033[33m-=' * 15)
a = float(input('\033[34mprimeiro segmento:'))
b = float(input('segundo segmento:'))
c = float(input('terceiro segmento: '))
if (b - c) < a < b + c and (a - c) < b < a + b and (a - b) < c < a + b:
    print('\033[32mDe acordo com as condições de existência os segmentos acima podem formar triângulo ', end='')
    if a == b == c:
        print('\033[36mEQUILÁTERO,\033[32m pois todos os lados tem o mesmo valor')
    elif a != b == c or a == b != c or a == c != b:
        print('\033[36mISÓSCELES,\033[32m pois tem dois lados com o mesmo valor e um diferente ')
    elif a != b != c:
        print('\033[36mESCALENO,\033[32m pois todos seus lados tem valores diferentes')
else:
    print('\033[32mde acordo com as condições de existência os segmentos acima \033[31mnão \033[32mpodem formar um triângulo.')