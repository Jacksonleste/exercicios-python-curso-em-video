from os import system
def escreva(text):
    tam = len(text)+2
    print('═' * tam)
    print(text)
    print('═' * tam)    

system("cls")
frase = str(input('escreva a frase a ser formatada: '))
system("cls")
escreva(f'   {frase:^} ')