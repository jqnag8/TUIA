def imprime_repetidos(lista_elementos: list[any]) -> None:
    i = 0

    while i < len(lista_elementos):
        if lista_elementos[i] in lista_elementos[i + 1:]:
            print(f"{lista_elementos[i]} se repite")
        i += 1

    return None

imprime_repetidos([1,2,3,4,5,1,3])
