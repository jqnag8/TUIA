def triangular(n: int) -> int:
    """
    Calcula el n-ésimo número triangular
    """
    if n == 1:
        return n
    return n + triangular(n - 1)


# TEST
def test_triangular() -> None:
    assert triangular(5) == 15
    assert triangular(1) == 1
    assert triangular(7) == 28
