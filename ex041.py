<<<<<<< HEAD
from datetime import datetime

ano = int(input('ano de nascimento: '))
idade: int = datetime.now().year - ano
print('o atleta que tem {} anos'.format(idade))
if idade <= 9:
    print('catégoria: MIRIM')
elif idade <= 14:
    print('catégoria: INFANTIL')
elif idade <= 19:
    print('catégoria: JUNIOR')
elif idade <= 25:
    print('catégoria: SÊNIOR')
elif idade > 25:
    print('sua catégoria é MASTER')
=======
from datetime import datetime

ano = int(input('ano de nascimento: '))
idade: int = datetime.now().year - ano
print('o atleta que tem {} anos'.format(idade))
if idade <= 9:
    print('catégoria: MIRIM')
elif idade <= 14:
    print('catégoria: INFANTIL')
elif idade <= 19:
    print('catégoria: JUNIOR')
elif idade <= 25:
    print('catégoria: SÊNIOR')
elif idade > 25:
    print('sua catégoria é MASTER')
>>>>>>> 747ecd2a336283c5b07a0e67d31be4817f8cd3f4
