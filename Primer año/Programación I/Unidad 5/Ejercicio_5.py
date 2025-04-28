def ingreso_datos() -> list[str] | int:
    lista_datos_ingresar = [
        "Nombre",
        "Apellido",
        "Localidad",
        "Edad",
        "DNI",
        "Carrera",
        "Año de ingreso",
    ]
    datos_personales = list()

    for dato_ingresar in lista_datos_ingresar:
        dato = input(f"Ingesar {dato_ingresar}: ")

        try:
            dato = int(dato)
        except ValueError:
            pass

        datos_personales.append(dato)

    return datos_personales


# print(ingreso_datos())

# ---------- Ejercicio b ----------

def calcula_años_cursado(lista_datos: list[any]) -> None:

    años_cursados = 2025 - lista_datos[6]

    lista_datos.append(años_cursados)

    print(f"{lista_datos[0]} {lista_datos[1]} lleva cursando {lista_datos[7]} años.")


# calcula_años_cursado(ingreso_datos())
    

# ---------- Ejercicio b ----------
def recolectar_datos() -> list[list[any]]:
    basedatos = list()
    lista_datos = ingreso_datos()

    while type(lista_datos[0]) is str:

        basedatos.append(lista_datos)
        lista_datos = ingreso_datos()

    return basedatos

print(recolectar_datos())
