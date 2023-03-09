from tkinter import *
from logica import *
from tkinter import ttk
import tkinter as tk
        
Ventana= Tk()
Ventana.title("Usuarios Registrados")
Ventana.geometry("900x400")
        
seccion1= Frame(Ventana)
seccion1.pack(expand= True, fill= 'both')

titulo= Label(seccion1,text="Usuarios Registrados: ",bg="green", fg="white", font=("Helvetica", 18)).pack()

col=("id","nom","usu","con")

tabla= ttk.Treeview(seccion1,columns=col)
tabla.heading("#0",text="Id: ")
tabla.heading("#1",text="Nombre: ")
tabla.heading("#2",text="Usuario: ")
tabla.heading("#3",text="Contraseña: ")
tabla.pack(padx = 4, pady = 4)

Ventana.mainloop()
