def es_potencia(n: int, b: int) -> bool:
    """
        Retorna True si 'n' es potencia de 'b'
    """

    if b == n:
        return True
    elif b > n:
        return False
    return es_potencia(n // b, b)


# TEST
def test_es_potencia():
    assert es_potencia(8, 2) == True
    assert es_potencia(64, 4) == True
    assert es_potencia(70, 10) == False
    
