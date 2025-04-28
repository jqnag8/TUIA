def suma_tiempos(tiempo_1: tuple[int, int, int], tiempo_2: [int, int, int]) -> tuple[int, int, int]:
    """
        Calcula la suma de dos tiempos dados en forma de tupla de la forma (segundos, minutos, horas)
    """

    segundos = tiempo_1[0] + tiempo_2[0]
    segundos_restantes = segundos % 60
    minutos = tiempo_1[1] + tiempo_2[1] + segundos // 60
    minutos_restantes = minutos % 60
    horas = tiempo_1[2] + tiempo_2[2] + minutos // 60

    return (segundos_restantes, minutos_restantes, horas)


print(suma_tiempos((50, 30, 3), (20, 30, 6)))

    
