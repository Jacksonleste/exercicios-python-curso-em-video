lista = [[], []]
for c in range(0, 7):
    n = int(input(f'Insira o {c+1}º valor: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
print('•═' * 25)
print(f'Os numeros pares são: {sorted(lista[0])}')
print(f'Os numeros ímpares são: {sorted(lista[1])}') 
print('•═' * 20)