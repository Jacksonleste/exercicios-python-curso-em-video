from time import sleep

print('=-' * 12)
print('CONTAGEM REGRESSIVA')
print('=-' * 12)
for c in range(10, -1, -1):
    sleep(1)
    print(c)
print('''
{}
*  FELIZ ANO NOVO!!!! *
{}'''.format('* ' * 12, '* ' * 12))