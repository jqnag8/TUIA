def historial_dolar() -> tuple[int, int, int, int, int]:
    """
    Se ingresan 5 valores que seran el valor del dólar en 5 días distintos y se guardará en una tupla
    """

    tupla_historial = list()  # luego se convierte a tupla

    for i in range(1,6):
        valor_ingresar = input(f"Ingrese el valor del dólar el día {i}: ")

        try:
            valor_ingresar = int(valor_ingresar)
        except ValueError:
            return "Valor incorrecto"

        tupla_historial.append(valor_ingresar)

    return tuple(tupla_historial)


print(historial_dolar())
