def diccionario_personas(lista_nombres: list[str], lista_edades: list[int]) -> dict[str, int]:
    diccionario_resultado = dict()

    for nombre, edad in zip(lista_nombres, lista_edades):
        diccionario_resultado[nombre] = edad

    return diccionario_resultado

print(diccionario_personas(["Juan", "María", "Pedro"], [25, 30, 35]))
