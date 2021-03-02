<<<<<<< HEAD
peso = float(input('insira seu peso:(KG)'))
alt = float(input('insira sua altura(M)'))
imc = peso / (alt * alt)
print('seu IMC é de {:.1f}, e você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do seu peso ideal')
elif imc < 25:
    print('no seu peso ideal')
elif imc < 30:
    print('em sobrepeso')
elif imc <= 40:
    print('obeso')
elif imc > 40:
    print('com obesidade mórbida')
=======
peso = float(input('insira seu peso:(KG)'))
alt = float(input('insira sua altura(M)'))
imc = peso / (alt * alt)
print('seu IMC é de {:.1f}, e você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do seu peso ideal')
elif imc < 25:
    print('no seu peso ideal')
elif imc < 30:
    print('em sobrepeso')
elif imc <= 40:
    print('obeso')
elif imc > 40:
    print('com obesidade mórbida')
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
