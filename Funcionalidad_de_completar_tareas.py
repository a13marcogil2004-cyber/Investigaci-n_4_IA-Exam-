class Tablero:
    def __init__(self):
        self.pendiente = []
        self.en_progreso = []
        self.completadas = []

    def actualizar(self, tareas):
        # Limpiar listas
        self.pendiente.clear()
        self.en_progreso.clear()
        self.completadas.clear()

        for t in tareas:
            if t.estado == "Pendiente":
                self.pendiente.append(t)
            elif t.estado == "En progreso":
                self.en_progreso.append(t)
       