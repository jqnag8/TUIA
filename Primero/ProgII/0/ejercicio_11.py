def valor_max(ln: list[int]) -> int:
    """
        Calcula el mayor valor de una lista de int's de al menos un elemento.
    """
    if ln == []:
        return 0
    if ln[0] > valor_max(ln[1:]):
        return ln[0]
    else:
        return valor_max(ln[1:])

# TEST
def test_valor_max():
    assert valor_max([1, 2, 3, 4]) == 4
    assert valor_max([0, 0, 0]) == 0
    
    
