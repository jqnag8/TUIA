def contar_ocurrencias_rec(lista: list, valor) -> int:
    if not lista:
        return 0

    if lista[0] == valor:
        return 1 + contar_ocurrencias_rec(lista[1:], valor)
    else:
        return contar_ocurrencias_rec(lista[1:], valor)

def test_contar_ocurrencias_rec():
    assert contar_ocurrencias_rec([1,2,3], 2) == 1
    assert contar_ocurrencias_rec([1,1,1,1,1,1], 1) == 6
    assert contar_ocurrencias_rec([1,1,1,1,1,1], 3) == 0


def contar_ocurrencias_it(lista, valor) -> int:
    contador = 0

    for x in lista:
        if x == valor:
            contador += 1

    return contador

def test_contar_ocurrencias_it():
    assert contar_ocurrencias_it([1,2,3], 2) == 1
    assert contar_ocurrencias_it([1,1,1,1,1,1], 1) == 6
    assert contar_ocurrencias_it([1,1,1,1,1,1], 3) == 0
