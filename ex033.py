n1 = int(input('insira o primeiro número:'))
n2 = int(input('insira o segundo número:'))
n3 = int(input('insira o segundo número:'))
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('o maior número é {}'.format(maior))

print('o menor número é {}'.format(menor))