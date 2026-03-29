#====================================
# main.py
#====================================

from ui.app_tkinter import TkinterApp
from servicios.tarea_servicio import TareaServicio

# Punto de entrada principal de la aplicación
def main():
    # 1. Inicializamos la capa de lógica (Servicio).
    servicio = TareaServicio() 
    # 2. Inicializamos la capa de presentación (UI).
    app = TkinterApp(servicio)
    # 3. Ejecutamos el bucle principal de Tkinter.
    app.mainloop()
# Verificamos si el archivo se está ejecutando directamente.
if __name__ == "__main__":
    main()