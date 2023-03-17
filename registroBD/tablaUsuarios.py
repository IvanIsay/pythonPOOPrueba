from tkinter import *
from logica import *
from tkinter import ttk
import tkinter as tk
        
Ventana= Tk()
Ventana.title("Usuarios Registrados")
Ventana.geometry("900x400")

controlador= logica()

        
seccion1= Frame(Ventana)
seccion1.pack(expand= True, fill= 'both')

seccion2= Frame(Ventana)
seccion2.pack(expand= True, fill= 'both')

titulo= Label(seccion1,text="Usuarios Registrados: ",bg="green", fg="white", font=("Modern", 18)).pack()

col=("id","nom","usu","con")

tabla= ttk.Treeview(seccion1,columns=col)
tabla.heading("#0",text="Id: ")
tabla.heading("#1",text="Nombre: ")
tabla.heading("#2",text="Usuario: ")
tabla.heading("#3",text="Contraseña: ")
tabla.pack(padx = 4, pady = 4)

usuariosBD= controlador.consultatodos()
for nombre,clave in usuariosBD:
    tabla.insert('',0,text=nombre,values=clave)
    


btnDelete= Button(seccion2,text="Eliminar")
btnDelete.pack()

btnUpdate= Button(seccion2,text="Actualizar")
btnUpdate.pack()

Ventana.mainloop()
