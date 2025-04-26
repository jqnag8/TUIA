def lista_suma(lista_numeros: list[int]) -> list[int]:
    lista_resultado = list()
    suma_acumulada = 0

    for i in lista_numeros:
        suma_acumulada += i
        lista_resultado.append(suma_acumulada)

    return lista_resultado

print(lista_suma([1, 2, 3]))
