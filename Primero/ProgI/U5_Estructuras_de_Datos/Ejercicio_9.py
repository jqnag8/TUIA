def dia_siguiente(dia: tuple[int, str, int]) -> tuple[int, str, int] | str:
    """
    Recibe un dia como tupla (mes, día, año) y calcula el dia siguiente como otra tupla.
    """

    meses_30_dias = ["abril", "junio", "septiembre", "noviembre"]  # Abril, Junio, Septiembre, Noviembre
    meses_del_anio = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
    ]

    mes = dia[0]
    numero = dia[1]
    año = dia[2]

    if (mes in meses_del_anio) and (1 <= numero <= 31) and (1 <= año):
        if mes == meses_del_anio[-1] and numero == 31:
            return (meses_del_anio[0], 1, año + 1)
        elif (
            (mes not in meses_30_dias and numero == 31)
            or (mes == meses_del_anio[1] and numero == 28)
            or (numero == 30)
        ):
            return (meses_del_anio[meses_del_anio.index(mes) + 1], 1, año)
        else:
            return (mes, numero + 1, año)
    else:
        "Fecha no válida"


print(dia_siguiente(("diciembre", 31, 2003)))
print(dia_siguiente(("enero", 29, 2003)))
print(dia_siguiente(("febrero", 28, 204)))
print(dia_siguiente(("marzo", 31, 2005)))
