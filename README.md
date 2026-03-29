# Lista de Tareas (POO26)

Aplicación de escritorio en Python para gestionar tareas simples con interfaz gráfica de Tkinter.

## 📁 Estructura del proyecto

- `main.py`: punto de entrada de la aplicación.
- `modelos/tarea.py`: clase `Tarea` (modelo con id, descripción y completado).
- `servicios/tarea_servicio.py`: lógica de negocio (agregar, completar, eliminar).
- `ui/app_tkinter.py`: interfaz gráfica, eventos y presentación.

## ▶️ Cómo ejecutar

1. Abrir terminal en carpeta raíz (`lista_tarea_app` o el nivel superior si corresponde).
2. Ejecutar:

```bash
python main.py
```

## 🧩 Patrones de diseño

- Separación MVC / MVS ligera:
  - Modelo: `Tarea` almacena atributos y métodos de estado.
  - Servicio: `TareaServicio` administra operaciones y persistencia en memoria.
  - Vista/Controlador: `TkinterApp` renderiza y maneja eventos de usuario.

## 🎯 Manejo de eventos explicados

En `ui/app_tkinter.py`:

- `configurar_eventos()`:
  - `self.entry.bind("<Return>", ...)`: permite crear tareas con Enter para un flujo rápido.
  - `self.tree.bind("<Double-1>", ...)`: doble clic completa la tarea para evitar clicks adicionales en botón.

- `agregar_tarea()`:
  - Valida texto no vacío y delega en `servicio.agregar_tarea`.
  - Inserta fila en `Treeview` con tag `pendiente`.

- `completar_tarea(event=None)`:
  - Maneja invocación por botón o doble clic.
  - Si no hay selección y la acción se ejecuta desde botón, notifica al usuario.
  - Actualiza estado en el servicio y refresca vista con tag `completado`.

- `eliminar_tarea()`:
  - Verifica selección y luego elimina del servicio y del `Treeview`.

## ✅ Funcionalidades

- Añadir tarea
- Marcar como completada
- Eliminar tarea
- Interacción por teclado (Enter)
- Interacción por mouse (doble clic)
- Feedback visual con colores por estado

## 🛠️ Comentarios de código

Los comentarios dentro de `ui/app_tkinter.py` han sido extendidos para explicar la lógica de las decisiones de eventos, cómo funciona la separación de responsabilidades, y por qué se usan `bind()` para teclado y ratón.
