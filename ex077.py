vogais = ('A', 'E', 'I', 'O', 'U')
palavras = ('LAPIS', 'CANETA', 'CURSO', 'VIDEO', 'NOME',
            'CAVALO', 'LAPIS', 'COMPUTADOR', 'INTERPRETE',
            'APRENDER', 'LINGUAGEM', 'PROGRAMAR', 'DESENVOLVER',
            'ESTUDAR')
for c in palavras:
    print(f'\nNa palavra {c} temos as vogais: ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
