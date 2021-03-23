soma = cont = 0
time = list()
gols = list()
jogador = dict()
partidas = list()
#ler nome dos jogadores
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partida = int(input(f'Número de partidas que {jogador["nome"]} jogou: '))
    partidas.append(partida)
    for c in range(0, partida):
        gols.append(int(input(f'gols na {c+1}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]?')).strip().upper()[0]
    if resp == 'N':
        break
print('•═' * 30)
print(f'{"Nº":^3}{"Nome":<17}{"Gols":<15}{"Total":<15}')
print('--' * 30)
for k, j in enumerate(time):
    print(f'{k+1:<3}', end='')
    for d in j.values():
        print(f'{str(d):<16} ', end='')
    print()
while True:
    print('•═' * 30)
    num = int(input('Quer ver os dados de qual jogador (999 para parar)? '))
    if num == 999:
        break
    else:
        if num > len(time):
            print(f'ERRO! Não existe jogador {num}')
        else:
            print(f'- O jogador {time[num-1]["nome"]} jogou {partidas[num-1]} partidas.')
            for c, g in enumerate(time[num-1]['gols']):
                print(f'  → Na partida {c+1}, fez {g} gols.')
            print(f'Um total de {time[num-1]["total"]} gols.')