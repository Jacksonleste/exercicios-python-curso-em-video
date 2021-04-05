def fatorial(num, show=False):
    """→ Calcula o fatorial de um número.

    Args:
        num (int): Número a ser calculado o fatorial .
        show (bool, optional): Mostrar ou não o cálculo. O padrão é: False.

    Returns:
        O valor fatorial de um número com ou sem cálculo.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
                if c == 1:
                    print(f' {c} = ', end='')
                else:
                    print(f' {c} X', end='')
        f *= c
    return f


#programa principal
print(fatorial(5))