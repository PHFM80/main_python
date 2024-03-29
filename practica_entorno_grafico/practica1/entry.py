from tkinter import *

#   Configracion de la raiz
raiz = Tk()

mi_frame = Frame(raiz, width="800", height="400")
mi_frame.pack()

# Eqtiqueta y cuadro de texto con coordenadas
# cuadro_texto = Entry(mi_frame).place(x=100, y=100)

# nombre_label = Label(mi_frame, text="Nombre: ").place(x=120, y=100)

# Eqtiqueta y cuadro de texto con grilla
vacia_label = Label(mi_frame, text="")
vacia_label.grid(row=0, column=0)
vacia2_label = Label(mi_frame, text="          ")
vacia2_label.grid(row=1, column=0)
cuadro_texto1 = Entry(mi_frame)
cuadro_texto1.grid(row=1, column=3)

nombre_label1 = Label(mi_frame, text="Nombre: ")
nombre_label1.grid(row=1, column=2)

# etiquetas de nopmbre apellido y direccion con su entry
nombre_label = Label(mi_frame, text="Nombre: ")
nombre_label.grid(row=5, column=1, padx=10, pady=10)
apelllido_label = Label(mi_frame, text="Apellido: ")
apelllido_label.grid(row=6, column=1, padx=10, pady=10)
direccion_label = Label(mi_frame, text="Direccion: ")
direccion_label.grid(row=7, column=1, padx=10, pady=10)
contrasena_label = Label(mi_frame, text="Contraseña: ")
contrasena_label.grid(row=8, column=1, padx=10, pady=10)

nombre_cuadro = Entry(mi_frame)
nombre_cuadro.grid(row=5, column=2, padx=10, pady=10)
nombre_cuadro.config(fg="red", justify="center")
apellido_cuadro = Entry(mi_frame)
apellido_cuadro.grid(row=6, column=2, padx=10, pady=10)
direccion_cuadro = Entry(mi_frame)
direccion_cuadro.grid(row=7, column=2, padx=10, pady=10)
contrasena_cuadro = Entry(mi_frame)
contrasena_cuadro.grid(row=8, column=2, padx=10, pady=10)
contrasena_cuadro.config(show="*")






raiz.mainloop ()
