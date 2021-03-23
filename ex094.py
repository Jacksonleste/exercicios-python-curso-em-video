totpesoas = somaidade = 0
pessoas = list()
dados = dict()
while True:
    print('══' * 14)
    dados['nome'] = str(input('Nome: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()
        if sexo not in 'MF':
            print('Resposta inválida! Responda somente com M ou F.')
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    totpesoas += 1
    pessoas.append(dados.copy())
    dados.clear
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar[S/N]: ')).strip().upper()
        if resp not in 'SN':
            print('Resposta inválida! Responda apenas S ou N.')
    if resp == 'N':
        break
for i in pessoas:
    somaidade += i['idade']
media = somaidade / totpesoas
print('•═' * 20)
print(f'→ Foram cadastradas {totpesoas} pessoas.')
print(f'→ A média de idade das pessoas cadastradas é {media:.1f} anos')
print('→ As mulheres cadastradas foram:')
for m in pessoas:
    if m['sexo'] == 'F':
        print(f'   - {m["nome"]}')
print('→ As pessoas com idade acima da média são:')
for i in pessoas:
    if i['idade'] > media:
        print(f'   - nome: {i["nome"]}, sexo: {i["sexo"]}, idade: {i["idade"]}')
print('>>>>>ENCERADO<<<<<')