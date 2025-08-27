def factorial(n: int) -> int | str:
    """
        Calcula el factorial de un numero 'n'
    """

    if (n < 1):
        return "Error: número no natural"
    elif (n == 1):
        return 1
    return n * factorial(n - 1)


def test_factorial():
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(0) == "Error: número no natural"        

