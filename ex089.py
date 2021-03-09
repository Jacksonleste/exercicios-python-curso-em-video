cont = 0
lista = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append([nome, nota1, nota2])
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print('•═' * 30)
print(f'{"Nº":<4}{"Nome":<12}{"média":<8}')
print('--' * 20)
for l in lista:
    cont += 1
    print(f'{cont:<4}{l[0]:<12}{(l[1] + l[2]) / 2:<8.2f}')  

while True:
    cont = 0
    print('•═' * 30)
    notind = int(input('Insira o número do aluno para ver suas notas (999 para parar): '))
    for l in lista:
        cont += 1
        if cont == notind:
            print()
            print(f'''aluno: {l[0]}
nota 1: {l[1]}
nota 2: {l[2]}''')
    if notind == 999:
        break