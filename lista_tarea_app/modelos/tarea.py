
#====================================
# tarea.py
#====================================
# Clase que representa el modelo de una Tarea individual
class Tarea:
    # Metodo constructor que inicializa los atributos de la tarea
    def __init__(self, id: int, descripcion: str):
        self._id = id
        self._descripcion = descripcion
        self._completado = False

    # GETTERS
    # Decorador que permite acceder al ID de la tarea como una propiedad de solo lectura
    @property
    def id(self):
        return self._id
    
    # Decorador que permite acceder a la descripción de forma segura
    @property
    def descripcion(self):
        return self._descripcion
    # Decorador que permite consultar si la tarea está completada
    @property
    def completado(self):
        return self._completado

    # SETTERS
    # Permite modificar la descripción de la tarea después de haber sido creada
    @descripcion.setter
    def descripcion(self, nueva_descripcion: str):
        self._descripcion = nueva_descripcion

    # MÉTODOS
    # Cambia el estado interno de la tarea a completado (True)
    def marcar_completada(self):
        self._completado = True

        