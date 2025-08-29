def sub_string(st_1: str, st_2: str) -> int:
    """
        Encuentra la primera posicion de la primer aparicion de 'st_2' en 'st_1'
    """
    if st_1.startswith(st_2):
        return 0
    return 1 + sub_string(st_1[1:], st_2)


# TEST
def test_sub_string() -> None:
    assert (sub_string("Hola", "ola")) == 1
    assert (sub_string("Hola", "a")) == 3
