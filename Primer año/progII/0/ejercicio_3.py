def misterio(a: int) -> int:
    """
        Retorna la sumatoria de 1's empezando desde 1 hasta 'a'. No admite números negativos
    """
    if (a == 0):
        return a
    return 1 + misterio(a - 1)


"""
    misterio(5) -> 1 + misterio(4) -> 1 + 1 + misterio(3) -> 1 + 1 + 1 + misterio(2) ->
    1 + 1 + 1 + 1 + misterio(1) -> 1 + 1 + 1 + 1 + 1 + misterio(0) -> 1 + 1 + 1 + 1 + 1 + 0 = 5
"""


