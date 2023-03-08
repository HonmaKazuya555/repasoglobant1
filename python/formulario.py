import tkinter as tk

# Crear ventana
ventana = tk.Tk()

# Crear etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(ventana, text="Bienvenido al formulario")
etiqueta_bienvenida.pack()

# Crear etiqueta y campo para el nombre
etiqueta_nombre = tk.Label(ventana, text="Nombre:")
etiqueta_nombre.pack()
campo_nombre = tk.Entry(ventana)
campo_nombre.pack()

# Crear etiqueta y campo para la edad
etiqueta_edad = tk.Label(ventana, text="Edad:")
etiqueta_edad.pack()
campo_edad = tk.Entry(ventana)
campo_edad.pack()

# Función que se ejecuta al hacer clic en el botón
def enviar_formulario():
    nombre = campo_nombre.get()
    edad = campo_edad.get()
    etiqueta_resultado.config(text=f"Tu nombre es {nombre} y tienes {edad} años.")

# Crear botón para enviar el formulario
boton_enviar = tk.Button(ventana, text="Enviar", command=enviar_formulario)
boton_enviar.pack()

# Crear etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack()

# Ejecutar ventana
ventana.mainloop()