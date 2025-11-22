class Materia:
    def __init__(self, id: str, nombre: str, creditos: int):
        self.id = id 
        self.nombre = nombre
        self.creditos = creditos
            
class Carrera:
    def __init__(self, materias: list[Materia] = list()):
        self.materias = materias
        self.aprobadas: list[tuple[str, int]] = list() # atributo de lista del tipo (Materia, nota)


    def aprobar(self, id_materia: str, nota: int) -> None:
        """
            agrega una materia aprobada a la lista de aprobadas
        """
        for materia in self.materias:
            if materia.id == id_materia:
                self.aprobadas += [(materia, nota)]
                return None
        else:
            print(f"Error: La materia {materia.id} no es parte del plan de estudios")

    
    def __str__(self) -> str:
        suma_creditos: int = 0
        cant_aprobadas = len(self.aprobadas)

        if cant_aprobadas > 0:

            for materia, nota in self.aprobadas:
                suma_creditos += nota

            promedio: int = suma_creditos / cant_aprobadas
            str_resultado: str = "" # string que usamos para imprimir el listado de las materias aprobadas

            for materia, nota in self.aprobadas:
                str_resultado += f"{materia.id} {materia.nombre} ({nota}) "
            
            return f"Créditos: {suma_creditos} -- Promedio: {promedio} -- Materias aprobadas: {str_resultado}"
        else: 
            return f"Créditos: {suma_creditos} -- Promedio: N/A -- Materias aprobadas: 0"


analisis2 = Materia("61.03", "Análisis 2", 8)
fisica2 = Materia("62.01", "Física 2", 8)
algo1 = Materia("75.40", "Algoritmos 1", 6)
c = Carrera([analisis2, fisica2, algo1])
print(c)
c.aprobar("95.14", 7)
c.aprobar("75.40", 10)
c.aprobar("62.01", 7)
print(c)

    
