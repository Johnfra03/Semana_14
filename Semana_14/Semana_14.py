import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import re  # Para usar expresiones regulares en la validación

# Función para agregar un evento
def agregar_evento():
    # Obtener los valores de los campos de entrada
    fecha = entrada_fecha.get()
    hora = entrada_hora.get()
    descripcion = entrada_descripcion.get()

    # Validar que todos los campos estén completos
    if fecha and hora and descripcion:
        # Agregar el evento al Treeview
        tree.insert("", "end", values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        # Mostrar mensaje si faltan datos
        messagebox.showwarning("Campos Vacíos", "Todos los campos son obligatorios")

# Función para eliminar un evento seleccionado
def eliminar_evento():
    # Obtener el evento seleccionado
    seleccionado = tree.selection()
    if seleccionado:
        # Confirmar la eliminación del evento
        confirmar = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de eliminar este evento?")
        if confirmar:
            tree.delete(seleccionado)
    else:
        # Mostrar mensaje si no se selecciona un evento
        messagebox.showwarning("Selección Vacía", "Seleccione un evento para eliminar")

# Función para limpiar los campos de entrada después de agregar un evento
def limpiar_campos():
    entrada_hora.delete(0, tk.END)
    entrada_descripcion.delete(0, tk.END)

# Función de validación para permitir solo el formato HH:MM en la hora
def validar_hora(P):
    # Aceptar solo números y los dos puntos ":" en el formato HH:MM
    if P == "" or re.match(r'^\d{0,2}(:?\d{0,2})$', P):  # Permite números y dos puntos
        return True
    else:
        # Mostrar un mensaje de advertencia si el formato es incorrecto
        messagebox.showwarning("Formato Incorrecto", "Solo se permite el formato HH:MM (Ej: 14:30)")
        return False

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Crear Frame para la entrada de datos
frame_entrada = ttk.Frame(root, padding=10)
frame_entrada.pack(fill="x")

# Etiquetas y campos de entrada
ttk.Label(frame_entrada, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)

# Configuración del DateEntry para formato DD/MM/YYYY
entrada_fecha = DateEntry(frame_entrada, width=12, date_pattern='dd/mm/yyyy')
entrada_fecha.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Hora:").grid(row=1, column=0, padx=5, pady=5)

# Validación para permitir solo el formato HH:MM en la hora
vcmd = root.register(validar_hora)  # Registrar la función de validación
entrada_hora = ttk.Entry(frame_entrada, validate="key", validatecommand=(vcmd, "%P"))
entrada_hora.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
entrada_descripcion = ttk.Entry(frame_entrada, width=30)
entrada_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Botón para agregar evento
ttk.Button(frame_entrada, text="Agregar Evento", command=agregar_evento).grid(row=3, columnspan=2, pady=10)

# Crear Frame para la lista de eventos
frame_lista = ttk.Frame(root, padding=10)
frame_lista.pack(fill="both", expand=True)

# Crear el Treeview para mostrar los eventos
columnas = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(frame_lista, columns=columnas, show="headings")
for col in columnas:
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True)

# Crear Frame para los botones de acción
frame_botones = ttk.Frame(root, padding=10)
frame_botones.pack(fill="x")

# Botones de eliminar y salir
ttk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento).pack(side="left", padx=5)
ttk.Button(frame_botones, text="Salir", command=root.quit).pack(side="right", padx=5)

# Ejecutar la aplicación
root.mainloop()
