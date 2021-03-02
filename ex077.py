<<<<<<< HEAD
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
=======
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
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
