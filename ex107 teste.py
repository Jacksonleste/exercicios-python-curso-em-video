from ex107 import moeda

num = int(input('Digite o preço : R$'))

print(f'- R${num} mais 30% é igual a R${moeda.aumentar(num, 30)}')
print(f'- R${num} menos 10% é igual a R${moeda.diminuir(num, 10)}')
print(f'- O dobro de R${num} é R${moeda.dobro(num)}')
print(f'- A metade de R${num} é R${moeda.metade(num)}')