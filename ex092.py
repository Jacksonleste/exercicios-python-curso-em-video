from datetime import date
anoatual = date.today().year
dados = dict()
dados['nome'] = str(input('Nome: ')).capitalize()
ano = int(input('Ano de nascimento: '))
dados['idade'] = anoatual - ano
dados['ctps'] = int(input('CTPS: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['aposentadoria'] = dados['contratação'] - ano + 35
    dados['salário'] = int(input('Salário: R$'))
print('•═' * 20)
for k, v in dados.items():
    print(f'- {k} é igual a {v}')
 