print('\033[31;1m-=-'*10)
print('\033[33mCALCULAODRA DE PASSAGEM')
print('até 200KM: R$0,5 por KM')
print('acima de 200KM: R$0,45 por KM')
print('\033[31m-=-'*10)
km = float(input('\033[30mInsira a distância da sua viagem em KM:'))
p1 = km*0.5
p2 = km*0.45
if km <= 200:
    print('uma Viagem de \033[32m{}KM\033[30m custará \033[34mR${:.2f}'.format(km, p1))
else:
    print('uma viagem de \033[32m{}KM\033[30m custará \033[34mR${:.2f}'.format(km, p2))