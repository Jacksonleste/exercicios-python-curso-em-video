nota1 = float(input('insira sua primeira nota: '))
nota2 = float(input('insira sua segunda nota: '))
media = (nota1 + nota2) / 2
print('sua média foi {:.2f}'.format(media))
if media < 5.0:
    print('Você foi reprovado.')
elif 7 > media >= 5.0 :
    print('Você está de recuperação.')
elif media >= 7.0:
    print('Parabéns, você foi aprovado.')