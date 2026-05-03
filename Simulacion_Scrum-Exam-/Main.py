from Estructura_básica import Tarea
from Estructura_básica import Sprint
from Funcionalidad_de_completar_tareas import Tablero

# Crear sprint
sprint1 = Sprint(1)

# Crear tareas de IA
t1 = Tarea("Implementar BFS", 1)
t2 = Tarea("Implementar DFS", 1)
t3 = Tarea("Implementar UCS", 2)
t4 = Tarea("Pruebas", 3)

# Agregar tareas al sprint
for t in [t1, t2, t3, t4]:
    sprint1.agregar_tarea(t)

# Simular avance
t1.iniciar()
t1.completar()

t2.iniciar()

# Crear tablero
tablero = Tablero()
tablero.actualizar(sprint1.obtener_tareas())

# Mostrar estado
tablero.mostrar()