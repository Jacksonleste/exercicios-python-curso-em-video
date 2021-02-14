decimal = int(input('\033[30;1minsira um número decimal inteiro:'))
conv = int(input('\n\033[33m[1] para binário.'
                 '\n[2] para octal.'
                 '\n[3] para hexadecimal'
                 '\n\033[30minsira a base de conversão:'))
if conv == 1:
    binário = bin(decimal)
    print('\033[33m{}\033[30m convertido em \033[34mBINÁRIO\033[30m é igual a \033[31m{}\033[m'.format(decimal, binário[2:]))
elif conv == 2:
    octal = oct(decimal)
    print('\033[33m{}\033[30m convertido para \033[34mOCTAL\033[30m é igual a \033[31m{}\033[m'.format(decimal, octal[2:]))
elif conv == 3:
    hexa = hex(decimal)
    print(' \033[33m{}\033[30m convertido para \033[34mHEXADECIMAL\033[30m é igual a \033[31m{}\033[m'.format(decimal, hexa[2:]))
else:
    print('\033[31mopção invalida. tente novamente!!!')