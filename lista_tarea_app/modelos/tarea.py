
#====================================
# tarea.py
#====================================
# Clase que representa el modelo de una Tarea individual
class Tarea:
    def __init__(self, id: int, descripcion: str):
        self._id = id
        self._descripcion = descripcion
        self._completado = False

    # GETTERS
    @property
    def id(self):
        return self._id
   
    @property
    def descripcion(self):
        return self._descripcion
    
    @property
    def completado(self):
        return self._completado

    # SETTERS
    
    @descripcion.setter
    def descripcion(self, nueva_descripcion: str):
        self._descripcion = nueva_descripcion

    # MÉTODOS
    
    def marcar_completada(self):
        self._completado = True

        