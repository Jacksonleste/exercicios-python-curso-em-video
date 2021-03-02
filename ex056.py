totalidade = 0
mvelho = 0
mulherv = 0
for p in range(1, 5):
    print('{}{}ª PESSOA{}'.format(6 * '-', p, 6*'-'))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo:[M/F] ')).upper().strip()
    totalidade = totalidade + idade
    if sexo == 'M':
        if p == 1:
            mvelho = idade
            nomemv = nome
        else:
            if idade > mvelho:
                mvelho = idade
                nomemv = nome
    if sexo == 'F' and idade < 20:
        mulherv = mulherv + 1

media = totalidade / 4
print('''
A média de idade do grupo é {:.2f}'''.format(media))
if mvelho == 0:
    print('não há Homens nessa lista')
else:
    print('{} é o Homem mais velho e tem {} anos'.format(nomemv, mvelho))
print('{} Mulheres tem menos de 20 anos'.format(mulherv))
