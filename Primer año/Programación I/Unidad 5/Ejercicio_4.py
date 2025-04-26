def fibonacci_lista(n: int) -> list[int]:
    """
        Cacula los n primeros numeros de la serie de fibonacci en forma de lista.
    """

    lista_resultado = [0, 1]

    while len(lista_resultado) != n:
        lista_resultado.append(lista_resultado[-1] + lista_resultado[-2])

    return lista_resultado


print(fibonacci_lista(10))
