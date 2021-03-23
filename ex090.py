aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = int(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 70:
    aluno['situação'] = 'aprovado'
elif aluno['média'] >= 50:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'reprovado'
print('•═' * 20)
for k, v in aluno.items():
    print(f'- {k} é igual a {v}')
