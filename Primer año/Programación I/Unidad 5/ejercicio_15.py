def contador_numeros(lista_numeros: list[int]) -> dict[int, int]:
    contador = {}

    for numero in lista_numeros:
        if numero in contador:
            contador[numero] += 1
        else:
            contador[numero] = 1
    return contador


print(contador_numeros([1, 2, 8, 3, 4, 5, 4, 6, 7, 8, 10, 9, 10]))
