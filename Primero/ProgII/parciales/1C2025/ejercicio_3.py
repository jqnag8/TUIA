class Evento:
    def __init__(self, codigo_evento: str, nombre: str, fecha: str, hora: str, capacidad: int) -> Evento:
        self.codigo_evento = codigo_evento
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.capacidad = capacidad

    def __str__(self):
        return f"{self.codigo}, {self.nombre}, {self.nombre}, {self.fecha}, {self.hora}, {self.capacidad}"
        
    # Ejercicio 2

class ReservarEvento:
    def __init__(self, dni_cliente, nombre_cliente, evento, numero_asistentes) :
        self.dni = dni_cliente
        self.nombre = nombre_cliente
        self.evento = evento
        self.numero_asistentes = numero_asistentes

    
    def __str__(self):
        return f"{self.dni}, {self.nombre}, {self.evento}, {self.numero_asistentes}"
        
    # Ejercicio 3

class SistemaEventos:
    def __init__(self):
        self.eventos: dict[str, Evento] = dict()
        self.reservas: dict[str, list[ReservarEvento]] = dict()

    def agregar_evento(self, evento: Evento):
        self.eventos[evento.codigo_evento] = evento

        return None

    def eliminar_evento(self, codigo_evento: str) -> None:
        for codigo in self.eventos:
            if codigo_evento == codigo:
                self.eventos.pop(codigo)

        return None

    def mostrar_eventos(self):
        for evento in self.eventos.values():
            print(evento)

        return None


    def devolver_capacidad_restante(self, codigo):
        capacidad_total = self.eventos(codigo).capacidad
        suma_acumulada = 0

        for reserva in self.reservas(codigo):
            suma_acumulada += reserva.numero_asistentes
            
    
   
