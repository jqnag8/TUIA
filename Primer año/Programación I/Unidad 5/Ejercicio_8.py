def dia_siguiente(dia: tuple[int, int, int]) -> tuple[int, int, int] | str:
    """
    Recibe un dia como tupla (mes, día, año) y calcula el dia siguiente como otra tupla.
    """

    meses_30_dias = [4, 6, 9, 11]  # Abril, Junio, Septiembre, Noviembre

    mes = dia[0]
    numero = dia[1]
    año = dia[2]

    if (1 <= mes <= 12) and (1 <= numero <= 31) and (1 <= año):
        if mes == 12 and numero == 31:
            return (1, 1, año + 1)
        elif (
            (mes not in meses_30_dias and numero == 31)
            or (mes == 2 and numero == 28)
            or (numero == 30)
        ):
            return (mes + 1, 1, año)
        else:
            return (mes, numero + 1, año)
    else:
        "Fecha no válida"


print(dia_siguiente((12, 31, 2003)))
print(dia_siguiente((1, 29, 2003)))
print(dia_siguiente((2, 28, 204)))
print(dia_siguiente((3, 31, 2005)))
