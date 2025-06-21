import tkinter as tk
from tkinter import messagebox


def mostrar_edad():
    """Muestra la edad"""
    messagebox.showinfo("Edad", "¡Mi edad actual es de 18 años!")

def mostrar_direccion():
    """Muestra la dirección"""
    messagebox.showinfo("Dirección", "Mi dirección es el Jicaro Nueva Segovia")

root = tk.Tk()
root.title("Ejercicio Primer parcial.Cristopher.Valladares")

# Label centrado arriba
label_nombre = tk.Label(root, text="Mi nombre es Cristopher Valladares", bg="purple", fg="white", font=("Arial", 16, "bold"))
label_nombre.pack(pady=(60, 40), anchor="center")

# Crear un frame para los botones (más abajo)
frame_botones = tk.Frame(root, bg="purple")
frame_botones.pack(pady=100)

# Botón para mostrar la edad (izquierda)
boton_edad = tk.Button(frame_botones, text="Edad", command=mostrar_edad, width=15)
boton_edad.pack(side="left", padx=40)

# Botón para mostrar la dirección (derecha)
boton_direccion = tk.Button(frame_botones, text="Dirección", command=mostrar_direccion, width=15)
boton_direccion.pack(side="right", padx=40)

# Configurar tamaño de la ventana
root.geometry("800x600")

# Establecer un color de fondo
root.configure(bg="purple")

# Ejecutar el bucle principal de la aplicación
root.mainloop()