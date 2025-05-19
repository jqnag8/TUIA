def proporcion_directa(total: int, cantidad: int) -> str:
    """
    Calcula la proporcin directa entre dos numeros
    """
    return f"{(cantidad * 100) // total}%"


# --- Ejercicio 1.a ---
contador_E = 0
contador_D = 0
contador_O = 0

for x in range(150):
    tipo_menu = input("Ingresar el tipo de menú: (E/D/O) ")

    match tipo_menu:
        case "E" | "e":
            contador_E += 1
        case "D" | "d":
            contador_D += 1
        case "O" | "o":
            contador_O += 1
        case "":
            break
        case _:
            print("No existe tal tipo de menú.")


print(
    f"Se vendieron, {proporcion_directa(150, contador_E)} menúes de estudiantes, {proporcion_directa(150, contador_D)} "
    f"menúes de docentes y {proporcion_directa(150, contador_O)} menúes de otros."
)

# --- Ejercicio 1.b ---
cantidad_total = int(input("Ingrese la cantidad de menúes que se vendieron: "))
contador_E = 0
contador_D = 0
contador_O = 0

for x in range(cantidad_total):
    tipo_menu = input("Ingresar el tipo de menú: (E/D/O) ")

    match tipo_menu:
        case "E" | "e":
            contador_E += 1
        case "D" | "d":
            contador_D += 1
        case "O" | "o":
            contador_O += 1
        case "":
            break
        case _:
            print("No existe tal tipo de menú.")

print(
    f"Se vendieron, {proporcion_directa(cantidad_total, contador_E)} menúes de estudiantes, {proporcion_directa(cantidad_total, contador_D)} "
    f"menúes de docentes y {proporcion_directa(cantidad_total, contador_O)} menúes de otros."
)

# --- Ejercicio1.c ---
contador_E = 0
contador_D = 0
contador_O = 0
contador_total = 0

while True:
    tipo_menu = input("Ingresar el tipo de menú: (E/D/O) ")

    match tipo_menu:
        case "E" | "e":
            contador_E += 1
            contador_total += 1
        case "D" | "d":
            contador_D += 1
            contador_total += 1
        case "O" | "o":
            contador_O += 1
            contador_total += 1
        case "":
            break
        case _:
            print("No existe tal tipo de menú.")

print(
    f"Se vendieron, {proporcion_directa(contador_total, contador_E)} menúes de estudiantes, {proporcion_directa(contador_total, contador_D)} "
    f"menúes de docentes y {proporcion_directa(contador_total, contador_O)} menúes de otros."
)
