from tkinter import *

#   Configracion de la raiz
raiz = Tk()
raiz.title("Ventana de Pablo")
raiz.config(bg="blue")

#   Configuracion del frame
mi_frame = Frame()
mi_frame.pack(fill="both", expand="True")
mi_frame.config(bg="red")
mi_frame.config(width="800", height="600")

mi_Label1 = Label(mi_frame, text="Hola Mundo")
mi_Label1.place(x=100, y=100)
#CODIGO SIMPLIFICADO
mi_Label1_1 = Label(mi_frame, text="Hola Mundo\nSimplificado", fg="blue", font=("Times New Roman", 15)).place(x=100, y=200)

mi_Label2 = Label(mi_frame, text="Pablo Flores")
mi_Label2.place(x=100, y=300)

imagen = PhotoImage(file="E:\Desarrollo_de_sofware\Practicas_Python\practica_entorno_grafico\practica1\imagenes\homero.png")
mi_Label3 = Label(mi_frame, image=imagen, width="100", height="100")
mi_Label3.place(x=300, y=0)






raiz.mainloop ()
