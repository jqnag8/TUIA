def promedio_alumnos(dict_alumnos: dict[str, list[int | float]]) -> None:
    for alumno, notas in dict_alumnos.items():
        suma_acumulada = 0
        for i in notas:
            suma_acumulada += i
        promedio = suma_acumulada / len(notas)
        print(f"El promedio de {alumno} es {promedio:.2f}")


promedio_alumnos({"Juan": [8, 9.5 , 10], "Maria": [7.2, 8, 9], "Pedro": [6.5, 7, 8]})
