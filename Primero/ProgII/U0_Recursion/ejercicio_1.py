# Ejercicio 1
def repite_hola(repes: int) -> None:
    """
        Recibe un número e imprime en pantalla 'hola' la cantidad de veces que se le ingresa al programa
    """
    if (repes < 0):
        return "Error: Número no natural"
    elif (repes == 0):
        return
    print("Hola")
    return repite_hola(repes - 1)

# repite_hola(5)

# Ejercicio 2
def repite_holaV2(repes: int) -> None:
    """
        Recibe un número e imprime en pantalla 'hola' la cantidad de veces que se le ingresa al programa
    """
    if (repes < 0):
        return "Error: Número no natural"
    elif (repes == 0):
        print("")
        return
    print("Hola", end = '')
    return repite_hola(repes - 1)

repite_holaV2(3)
