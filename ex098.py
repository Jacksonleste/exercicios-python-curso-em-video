from time import sleep
def contador(a, b, c):
    if c < 0:
        c = c*-1
    if c == 0:
        c = 1
    print(f'contando de {a} até {b} de {c} em {c}:')
    if a < b:
        for cont in range(a, b+1, c):
            sleep(0.4)
            print(cont, end=' ')
    if a > b:
        for cont in range(a, b-1, c*-1):
            sleep(0.4)
            print(cont, end=' ' )
    print('FIM!')
    print("▬▬" * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é sua vez de definir a contagem.")
inicio = int(input('Início: '))
fim = int(input('fim: '))
passo = int(input('passo: '))
print()
contador(inicio, fim, passo)