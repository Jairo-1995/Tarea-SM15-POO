#=================================
# tareas_ui.py
#=================================
import tkinter as tk
from tkinter import ttk, messagebox

class TkinterApp(tk.Tk):
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Lista de Tareas")
        self.geometry("600x450")
        self.configure(bg="#5f8abb")  # Fondo azul oscuro profesional

        self.configurar_estilos()
        self.crear_widgets()
        self.configurar_eventos()

    def configurar_estilos(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")  # Tema base para mayor personalización

        # Configuración de la Tabla (Treeview)
        self.style.configure("Treeview", 
                             background="#ecf0f1", 
                             foreground="#5887b6", 
                             fieldbackground="#f5fdff", 
                             rowheight=30,
                             font=("Segoe UI", 10))
        self.style.map("Treeview", background=[("selected", "#3168DD")])
        self.style.configure("Treeview.Heading", 
                             background="#34495e", 
                             foreground="white", 
                             font=("Segoe UI", 11, "bold"))

    def crear_widgets(self):
        # Título
        titulo = tk.Label(self, text="MIS TAREAS", font=("Segoe UI", 30, "bold"), 
                         bg="#4c84bd", fg="#ecf0f1")
        titulo.pack(pady=10)

        # Entrada
        self.entry = tk.Entry(self, font=("Segoe UI", 12), width=35, 
                             relief="flat", bd=5)
        self.entry.pack(pady=10)

        # Botones
        frame_botones = tk.Frame(self, bg="#5298C0")
        frame_botones.pack(pady=5)

        # Estilos específicos para botones (usando botones estándar para colores más fáciles)
        self.btn_agregar = tk.Button(frame_botones, text="✚ Añadir tarea", command=self.agregar_tarea,
                                   bg="#7052dd", fg="white", font=("Segoe UI", 10, "bold"), 
                                   padx=10, relief="flat", cursor="hand2")
        self.btn_agregar.grid(row=0, column=0, padx=5)

        self.btn_completar = tk.Button(frame_botones, text="✔ Marcar como Completado", command=self.completar_tarea,
                                     bg="#57ce8c", fg="white", font=("Segoe UI", 10, "bold"), 
                                     padx=10, relief="flat", cursor="hand2")
        self.btn_completar.grid(row=0, column=1, padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="✘ Eliminar tarea", command=self.eliminar_tarea,
                                    bg="#e74c3c", fg="white", font=("Segoe UI", 10, "bold"), 
                                    padx=10, relief="flat", cursor="hand2")
        self.btn_eliminar.grid(row=0, column=2, padx=5)

        # Tabla
        self.tree = ttk.Treeview(self, columns=("ID", "Descripción", "Estado"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Estado", text="Estado")
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Estado", width=100, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=10, padx=20)

        # Feedback Visual: Configuración de colores por estado
        # Rojo claro para pendientes/incompletos
        self.tree.tag_configure("pendiente", background="#dbaca9", foreground="#c0392b", font=("Segoe UI", 10, "bold")) 
        # Verde para completados
        self.tree.tag_configure("completado", background="#beecd2", foreground="#197A36", font=("Segoe UI", 10, "italic")) 

    def configurar_eventos(self):
        """Configura los manejadores de eventos avanzados usando .bind()"""
        
        # Evento de Teclado: Agregar tarea al presionar Enter en el campo de entrada
        self.entry.bind("<Return>", lambda e: self.agregar_tarea())

        # Evento de Ratón: Marcar como completada al hacer doble clic sobre un ítem
        self.tree.bind("<Double-1>", lambda e: self.completar_tarea(e))

    def agregar_tarea(self):
        descripcion = self.entry.get()
        tarea = self.servicio.agregar_tarea(descripcion)

        if tarea:
            # Insertar nueva tarea con estado inicial
            self.tree.insert("", "end", values=(tarea.id, tarea.descripcion, "Pendiente"), tags=("pendiente",))
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "La descripción de la tarea no puede estar vacía.")

    def completar_tarea(self, event=None):
        seleccionado = self.tree.selection()
        if not seleccionado:
            # Si no hay selección y no viene de un evento de ratón, avisar al usuario
            if event is None:
                messagebox.showinfo("Info", "Por favor, selecciona una tarea para completar.")
            return

        item = self.tree.item(seleccionado)
        id_tarea = int(item["values"][0])

        tarea = self.servicio.completar_tarea(id_tarea)

        if tarea:
            # Feedback Visual: Cambiamos el texto a [Hecho] y aplicamos el tag verde
            self.tree.item(seleccionado,
                           values=(tarea.id, tarea.descripcion, "[✅tarea completada]"),
                           tags=("completado",))
            
            # Quitar la selección para que se aprecie el color verde de fondo
            self.tree.selection_remove(seleccionado)

    def eliminar_tarea(self):
        seleccionado = self.tree.selection()
        if not seleccionado:
            return messagebox.showinfo("Info", "Por favor, selecciona una tarea para eliminar.")

        item = self.tree.item(seleccionado)
        id_tarea = int(item["values"][0])

        eliminado = self.servicio.eliminar_tarea(id_tarea)

        if eliminado:
            self.tree.delete(seleccionado)