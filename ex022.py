<<<<<<< HEAD
nome = str(input('\033[30;1mInsira seu nome completo:')).strip()
maiusculas = nome.upper()
minusculas = nome.lower()
letras = nome.replace(' ' , '')
letras2 = len(letras)
letpn = nome.split()
letpn2 = len(letpn[0])
print('''em maiúsculas = \033[32m{}
\033[30mem minúsculas = \033[32m{}
\033[30mletras ao todo = \033[32m{}
=======
nome = str(input('\033[30;1mInsira seu nome completo:')).strip()
maiusculas = nome.upper()
minusculas = nome.lower()
letras = nome.replace(' ' , '')
letras2 = len(letras)
letpn = nome.split()
letpn2 = len(letpn[0])
print('''em maiúsculas = \033[32m{}
\033[30mem minúsculas = \033[32m{}
\033[30mletras ao todo = \033[32m{}
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
\033[30mletras primeiro nome = \033[32m{}\033[m'''.format(maiusculas, minusculas, letras2, letpn2))