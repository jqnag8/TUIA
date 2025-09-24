def reversaR(ln: list[int]) -> list[int]:
    """
        Retorna la lista inversa usando recursión.
    """
    if not ln:
        raise ValueError("Empty list")
    if len(ln) == 1:
        return [ln[0]]
    return reversaR(ln[1:]) + [ln[0]]


# TEST
def test_reversaR() -> None:
    assert reversaR([1, 2, 3]) == [3, 2, 1]
    assert reversaR([2]) == [2]


# reversaI
def reversaI(ln: list[int]) -> list[int]:
    resultado: list[int] = list()

    for i in range(len(ln) - 1, -1, -1):
        resultado.append(ln[i])

    return resultado


# TEST
def test_reversaI() -> None:
    assert reversaI([1, 2, 3]) == [3, 2, 1]
    assert reversaI([2]) == [2]
