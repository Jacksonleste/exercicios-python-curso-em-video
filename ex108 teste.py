from ex108 import moeda

num = float(input('Digite o preço : R$'))

print(f'- Aumentando 30%, temos {moeda.moeda(moeda.aumentar(num, 30))}')
print(f'- diminunido 10%, é igual a {moeda.moeda(moeda.diminuir(num, 10))}')
print(f'- O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'- A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')