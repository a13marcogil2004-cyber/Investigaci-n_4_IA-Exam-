class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.estado = "Pendiente"

    def iniciar(self):
        self.estado = "En progreso"

     def completar(self):
        self.estado = "Completada"

class sprint:
    def __init__(self, numero):
        self.numero = numero
        self.tareas = []

     def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        
