def aumentar(n, p):
    res = n + (n/100) * p
    return res

def diminuir(n, p):
    res = n - (n/100) * p
    return res

def metade(n):
    res = n / 2
    return res
def dobro(n):
    res = n * 2
    return res


def moeda(n):
    res = f'{n:.2f}'
    res = str(res).replace(".", ",")
    res = f'R${res}'
    return res