import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    """ Muestra un mensaje de alerta"""
    messagebox.showinfo("Mensaje", "¡Hola, este es un mensaje de alerta!")
    
root = tk.Tk ()
root.title("Ejercicio 1")

#Agregar una etiqueta de titulo con el nonbre "nonbre del usuario"
etiqueta_usuario =tk.Label(root, text =    "nombre de usuari:")
etiqueta_usuario.pack(pady=5)


boton =tk.Button(root,text=" Mostrar mensaje" , command=mostrar_mensaje)
boton.pack(pady=20)

boton1 =tk.Button(root,text="Segundo boton" , command=mostrar_mensaje)
boton1.pack(pady=20)

#configuarar tamaño de la ventana
root.geometry("800x600")

#Establecer un color de fondo
root.configure(bg="purple")

#Ejecutar el bucle principal la apliacacion
root.mainloop()