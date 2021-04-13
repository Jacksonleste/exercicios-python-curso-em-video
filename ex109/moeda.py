def moeda(n):
    """→ Função que formata moeda. 

    :param n: Valor a ser formatado
    :type n: Numerico
    :return: valor formatado ex:"R$25,00"
    :rtype: string
    """
    return f'R${n:.2f}'.replace('.', ',')

def aumentar(n, p, form=False):
    """→ aumenta um valor usando porcentagem.

    :param n: valor a ser aumentado.
    :type n: numerico
    :param p: porcentagem do acréscimo.
    :type p: numerico
    :param form: Se deseja ou não formatar como moeda, defaults to False
    :type form: bool, optional
    :return: Valor númerico ou formatad como moeda.
    :rtype: numerico ou string
    """
    res = n + (n/100) * p
    if form:
        res = moeda(res)
    return res


def diminuir(n, p, form=False):
    """→ diminui um valor usando porcentagem.

    :param n: valor a ser descontado.
    :type n: numerico
    :param p: porcentagem do desconto.
    :type p: numerico
    :param form: Se deseja ou não formatar como moeda, defaults to False
    :type form: bool, optional
    :return: Valor númerico ou formatad como moeda.
    :rtype: numerico ou string
    """
    res = n - (n/100) * p
    if form:
        res = moeda(res)
    return res


def metade(n, form=False):
    """→ Calcula a metade de um valor.

    :param n: O valor a ser calculado.
    :type n: numerico
    :param form: , defaults to False
    :param form: Se deseja ou não formatar como moeda, defaults to False
    :type form: bool, optional
    :return: Valor númerico ou formatad como moeda.
    :rtype: numerico ou string
    """
    res = n / 2
    if form:
        res = moeda(res)
    return res


def dobro(n, form=False):
    """→ Calcula o dobro de um valor.

    :param n: O valor a ser calculado.
    :type n: numerico
    :param form: , defaults to False
    :param form: Se deseja ou não formatar como moeda, defaults to False
    :type form: bool, optional
    :return: Valor númerico ou formatad como moeda.
    :rtype: numerico ou string
    """
    res = n * 2
    if form:
        res = moeda(res)
    return res
