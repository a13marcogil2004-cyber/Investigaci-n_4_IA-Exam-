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
            elif t.estado == "Completada":
                self.completadas.append(t)

    def mostrar(self):
        print("\n=== TABLERO SCRUM ===")

        print("\nPendiente:")
        for t in self.pendiente:
            print("-", t.nombre)

        print("\nEn progreso:")
        for t in self.en_progreso:
            print("-", t.nombre)

        print("\nCompletadas:")
        for t in self.completadas:
            print("-", t.nombre)