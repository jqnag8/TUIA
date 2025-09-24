def cont_digits(n: int) -> int:
    """
        Cuenta los dígitos de un número natural
    """
    if n < 1:
        raise ValueError("Número no natural")
    if n < 10:
        return 1
    return 1 + cont_digits(n // 10)


# TEST
def test_cont_digits():
    assert cont_digits(10) == 2
    assert cont_digits(1234) == 4

    
