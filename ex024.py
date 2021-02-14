n = str(input('\033[30;1mqual o nome da sua cidade?'))
primeiro = n.split()[0].lower()
print('a cidade \033[31m{}\033[30m começa com santo? \033[31m{}\033[30m'.format(n.strip(), 'santo' in primeiro))
