#=================================
# tareas_servicio.py
#=================================
from modelos.tarea import Tarea

class TareaServicio:
    def __init__(self):
        self.tareas = []
        self.contador_id = 1


    def agregar_tarea(self, descripcion: str):
        if descripcion.strip() == "":
            return None
        
        tarea = Tarea(self.contador_id, descripcion)
        self.tareas.append(tarea)
        self.contador_id += 1
        return tarea

  
    def listar_tareas(self):
        return self.tareas

    
    def completar_tarea(self, id_tarea: int):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
              
                tarea.marcar_completada()
                return tarea
        return None
  
    def eliminar_tarea(self, id_tarea: int):
        for tarea in self.tareas:
            if tarea.id == id_tarea:
                self.tareas.remove(tarea)
                return True
        return False
