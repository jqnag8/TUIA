# ---------- Apartado a ----------
def notas_alumnos(lista_alumnos: list[tuple[str, int]]) -> dict[str, list[int]]:
    """
    Función que devuelve un diccionario con los alumnos como claves y una lista de notas como valores.
    """
    dict_resultado = dict()

    for alumno, nota in lista_alumnos:
        if alumno in dict_resultado:
            dict_resultado[alumno].append(nota)
        else:
            dict_resultado[alumno] = [nota]

    return dict_resultado

# ---------- Apartado b ----------
def alumnos_notas(lista_alumnos: list[tuple[str, int]]) -> dict[str, list[int]]:
    """
    Función que devuelve un diccionario con las notas como claves y una lista de alumnos como valores.
    """
    dict_resultado = dict()

    for alumno, nota in lista_alumnos:
        if nota in dict_resultado:
            dict_resultado[nota].append(alumno)
        else:
            dict_resultado[nota] = [alumno]

    return dict_resultado


print(notas_alumnos([("Juan", 8), ("María", 9), ("María", 9)]))
print(alumnos_notas([("Juan", 8), ("María", 8), ("Pedro", 9)]))
