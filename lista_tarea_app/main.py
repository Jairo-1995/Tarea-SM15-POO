#====================================
# main.py
#====================================

from ui.app_tkinter import TkinterApp
from servicios.tarea_servicio import TareaServicio


def main():
    
    servicio = TareaServicio() 
    app = TkinterApp(servicio)
    app.mainloop()
if __name__ == "__main__":
    main()