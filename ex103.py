def ficha(n='<desconhecido>', g= 0):
    """→ Cria a ficha de um jogador.

    :param n: Nome do  jogador, defaults to '<desconhecido>'
    :type n: str, optional
    :param g: Número de gols, defaults to 0
    :type g: int, optional
    """
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gols = str(input('número de gols: '))
if gols.isnumeric():
    gols = gols
else:
    gols = 0
if nome.strip() == '':
    ficha(g=gols)
else:
    ficha(nome, gols)