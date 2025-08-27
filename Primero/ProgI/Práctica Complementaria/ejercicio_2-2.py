def ingresoDatos() -> list[tuple[str, int]]:
    """
    Esta función solicita al usuario que ingrese los datos presentados
    en la planilla y devuelva una lista de tuplas, donde la primera
    componente es el nombre del estudiante y la segunda componente es
    la nota que obtuvo en el parcial.
    """
    notas = []

    nombre_alumno = input("Ingrese el nombre del alumno: ")

    while (nombre_alumno != ""):
        nota_alumno = int(input("Ingrese la nota del alumno: "))
        resultado = nombre_alumno, nota_alumno

        notas.append(resultado)

        nombre_alumno = input("Ingrese el nombre del alumno: ")

    return notas


# --- promMax ---
def promMax(listaNotas: list[tuple[str, int]]) -> tuple[float, int]:
    """
    Esta función recibe una lista de tuplas donde la primera componente
    es el nombre del estudiante y la segunda componente es la nota
    del estudiante en el parcial , y devuelve la nota promedio del
    curso y la nota más alta del curso tambi é n
    """
    suma_acumulada = 0
    nota_max = listaNotas[0][1]

    for i in range(len(listaNotas)):
        nota_alumno = listaNotas[i][1]
        suma_acumulada += nota_alumno

        if nota_alumno > nota_max:
            nota_max = nota_alumno

    promedio = suma_acumulada / len(listaNotas)

    return promedio, nota_max

# --- principal ---
def principal() -> None:
    """Funcion principal"""
    listaEstudiantes = ingresoDatos()

    if listaEstudiantes == list():
        print("No se ingresaron datos")
        return None

    nota_max = promMax(listaEstudiantes)[1]

    for estudiante, nota in listaEstudiantes:
        if nota == nota_max:
            print(f"{estudiante} consiguió la nota más alta: {nota}")


    return None

principal()
