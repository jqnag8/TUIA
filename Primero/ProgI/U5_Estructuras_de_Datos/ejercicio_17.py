def segunda_dosis(registro_dosis: dict[str, int]) -> list[str]:
    lista_recordatorio = list()

    for dni, vacunas in registro_dosis.items():
        if vacunas == 2:
            lista_recordatorio.append(dni)

    return lista_recordatorio

print(segunda_dosis({"12345678": 2, "98765432": 1, "44765345": 2}))
