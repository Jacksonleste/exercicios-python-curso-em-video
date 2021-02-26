expressao = list(str(input('Insira uma expressão matemática: ')))
par = list()
abre = list()
fecha = list()
while True:
    if '(' in expressao:
        expressao.remove('(')
        par.append('(')
        if ')' in expressao:
            expressao.remove(')')
            par.append(')')
    else:
        break
for v in par:
    if v == '(':
        abre.append(v)
    elif v == ')':
        fecha.append(v)
print('═•' * 20)
if ')' in expressao or len(abre) != len(fecha):
    print('A expressão digitada NÃO É VÁLIDA.')
else:
    print('A expressão digitada É VÁLIDA')
