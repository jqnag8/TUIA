def recursiva(t: int, k: int) -> int:
    """
        ...
    """
    while (t < 100):
        t += k
        k += 1
    return k


# TEST
def test_recursiva():
    assert recursiva(99, 100) == 101
    assert recursiva(99, 0) == 2
    
