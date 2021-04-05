def notas(*n, sit=False):
    """→ Função para análisar as notas de vários alunos.

    :param sit: Mostrar ou não a situação da turma, o padrão é False
    :type sit: bool, optional
    :return: várias informações sobre a turma
    :rtype: Dicionário
    """
    notas = dict()
    cont = maior = menor = media = 0
    for nota in n:
        cont += 1
        media += nota
        if cont == 1:
            maior = nota
            menor = nota
        else:
            if nota > maior:
                maior = nota
            if nota < menor:
                menor = nota
    media = media / cont
    notas['total'] = cont
    notas['maior'] = maior
    notas['menor'] = menor
    notas['média'] = media
    if sit:
        if media > 9:
            sit = 'Ótima'
        elif media > 7:
            sit = 'Boa'
        elif media > 5:
            sit = 'Dá pra melhorar'
        elif media < 5:
            sit = 'Ruim'
        notas['situação'] = sit
    return notas


print(notas(8.7, 9.5, 9, 10, 9.2, 9.6, sit = True))