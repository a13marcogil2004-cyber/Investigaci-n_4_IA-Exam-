class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = "Pendiente"

class sprint:
    def __init__(self, numero):
        self.numero = numero
        self.tareas = []