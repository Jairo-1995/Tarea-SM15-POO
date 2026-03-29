#=================================
# tareas_servicio.py
#=================================
from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        # Lista en memoria que almacenará los objetos de tipo Tarea
        self.tareas = []
        # Contador incremental para asignar un ID único a cada tarea nueva
        self.contador_id = 1

    # Método para crear y guardar una nueva tarea
    def agregar_tarea(self, descripcion: str):
        if descripcion.strip() == "":
            return None
        
        # Instanciamos una nueva Tarea con el ID actual y la descripción 
        tarea = Tarea(self.contador_id, descripcion)
        self.tareas.append(tarea)
        self.contador_id += 1
        return tarea
    
    # Método para obtener todas las tareas registradas
    def listar_tareas(self):
        return self.tareas

    # Busca una tarea por su ID y cambia su estado a completado
    def completar_tarea(self, id_tarea: int):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                # Utilizamos el método del modelo para marcarla como hecha
                tarea.marcar_completada()
                return tarea
        return None
    
    # Busca una tarea por su ID y la quita de la lista
    def eliminar_tarea(self, id_tarea: int):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False
