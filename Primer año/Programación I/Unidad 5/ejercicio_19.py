def diccionario_resultados(lista_diccionarios_alumnos: list[dict[str, list[int]]]) -> dict[str, list[int]]:
    diccionario_final = dict()

    for resultados_legajo in lista_diccionarios_alumnos:
        diccionario_final.update(resultados_legajo)

    return diccionario_final

print(diccionario_resultados([{"legajo_12": [1, 2, 3], "legajo_13": [4, 5, 6]},
                              {"legajo_14": [7, 8, 9]},
                              {"legajo_15": [10, 11, 12], "legajo_16": [13, 14, 15]}]))
