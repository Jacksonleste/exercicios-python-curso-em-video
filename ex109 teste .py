from ex109 import moeda

num = int(input('Digite o preço : R$'))

print(f'- {moeda.moeda(num)} mais 30% é igual a {moeda.aumentar(num, 30, True)}')
print(f'- {moeda.moeda(num)} menos 10% é igual a {moeda.diminuir(num, 10, True)}')
print(f'- O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'- A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')