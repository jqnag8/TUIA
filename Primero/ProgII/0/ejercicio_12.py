def iterativa(ln: list[int]) -> int:
    """
        Retorna la productoria de los elementos de una lista
    """
    if not ln:
        raise ValueError("Empty list")
    if len(ln) == 1: 
        return ln[0]
    return ln[0] * iterativa(ln[1:])


# TEST
def test_iterativa():
    assert iterativa([1, 2, 3]) == 6
    assert iterativa([2, 10, 1]) == 2
