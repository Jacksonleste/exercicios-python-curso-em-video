lista = ('Internacional', 'Flamengo', 'Atlético-MG', 'São paulo', 'Fluminense', 'Palmeiras', 'Grêmio', 'Santos',
         'Athletico-PR', 'Corinthians', 'Bragantino', 'Ceará-SC', 'Atlético-GO', 'Sport Recife', 'Fortaleza',
         'Bahia', 'Vasco da gama', 'Goiás', 'Coritiba', 'Botafogo')
print('══'* 15)
for classif ,time in enumerate(lista):
    print(f'{classif + 1:0>2}º {time}')
print('══' * 15)
print('os cinco primeiros colocados são:')
for classif, time in enumerate(lista[0:5]):
    print(f'{classif + 1:0>2}º {time}')
print('══' * 15)
print('Os quatro últimos colocados são:')
classif = 16
for time in lista[-4:]:
    print(f'{classif}º {time}')
    classif += 1
print('══' * 15)
print('Times em ordem alfabética:')
for time in sorted(lista):
    print(time)
print('══' * 15)
posição = lista.index('Santos') + 1
print(f'o Santos está na {posição}ª posição ')
print('══' * 15)