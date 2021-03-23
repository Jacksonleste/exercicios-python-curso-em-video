soma = 0
gols = list()
jogador = dict([])
jogador['nome'] = str(input('Nome do jogador: '))
jogador['partidas'] = int(input(f'Número de partidas que {jogador["nome"]} jogou: '))
for c in range(0, jogador['partidas']):
    gols.append(int(input(f'gols na {c+1}ª partida: ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('•═' * 20)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for c, g in enumerate(jogador['gols']):
    print(f'  → Na partida {c+1}, fez {g} gols.')
print(f'Um total de {jogador["total"]} gols.')
print('•═' * 20)
print(jogador)