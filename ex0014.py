cel = float(input('\033[30;1mqual a temperatura em C°?'))
far = 1.8*cel+32
ke = cel+273.15
print(' a tempreatura \033[31m{}C°\033[30m equivale a \033[36m{:.2f}F°\033[30m e \033[36m{}K°\033[m '.format(cel, far, ke))