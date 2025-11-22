def replicar(ln: list[int], n: int) -> list[int]:
    """
    Replica 'n' veces la cantidad de elementos de una lista de enteros.
    """
    if not ln:
        raise ValueError("Empty list")

    resultado: list = list()

    if len(ln) == 1:
        for _ in range(n):
            resultado += [ln[0]]
        return resultado

    for _ in range(n):
        resultado += [ln[0]]
    return resultado + replicar(ln[1:], n)


# TEST
def test_replicar() -> None:
    assert replicar([1, 2, 3], 2) == [1, 1, 2, 2, 3, 3]
    assert replicar([1], 2) == [1, 1]
