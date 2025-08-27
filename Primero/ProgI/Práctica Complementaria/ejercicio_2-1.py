def ingresoDeDatos() -> dict:
    """
    Esta función solicita al usuario que ingrese los datos presentados
    en la planilla y los devuelve en un diccionario
    """
    dicc = dict()

    nombre_soporte = input("Ingrese el nombre del soporte: ")

    while nombre_soporte != "":
        porcentaje = input("Ingrese el porcentaje de uso: ")

        dicc[nombre_soporte] = int(porcentaje)

        nombre_soporte = input("Ingrese el nombre del soporte: ")

    return dicc


# --- soporte_mas_usado ---
def soporte_mas_usado(base_datos: dict[str, int]) -> tuple:
    """Esta función recibe un diccionario conteniendo los datos ingresados
    por el usuario y devuelve una tupla con el nombre del soporte
    más utilizado y su porcentaje de uso"""
    lista_procesada = base_datos.items()
    valor_max = (0, 0)

    for soporte, porcentaje in lista_procesada:
        if valor_max[1] < porcentaje:
            valor_max = (soporte, porcentaje)

    return valor_max


# --- principal ---
def principal() -> None:
    """Programa principal"""
    baseDeDatos = ingresoDeDatos()

    if baseDeDatos == dict():
        print("No se ingresaron datos")
        return None

    print(soporte_mas_usado(baseDeDatos))

    return None

principal()
