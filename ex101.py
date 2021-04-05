def voto(an):
    """→ Calcula se seu voto é negado, opcional ou obrigatório de acordo com a idade.
    param an: Ano de nascimento. 
    """
    from datetime import datetime
    atual = datetime.today().year
    idade = atual - an
    if idade < 16:
        return f' Com {idade} anos você não pode votar!'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos seu voto é opcional!'
    else:
        return f'Com {idade} anos seu voto é obrigatório!'


print('══' * 17)
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
print('══' * 17)