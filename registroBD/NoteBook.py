from tkinter import *
from logica import *
from tkinter import ttk
import tkinter as tk

controlador= logica()

def ejecutaInsert():
    controlador.IngresarUsuario(var1.get(),var2.get(),var3.get())
        
Ventana= Tk()
Ventana.title("Ventana con Pestañas")
Ventana.geometry("500x300")
nombre= StringVar()

panel= ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

pestaña1= ttk.Frame(panel)
pestaña2= ttk.Frame(panel)
pestaña3= ttk.Frame(panel)
pestaña4= ttk.Frame(panel)


titulo= Label(pestaña1,text="Registro Usuario",bg="black", fg="white", font=("Helvetica", 18)).pack()

var1 = tk.StringVar()
lblNombre= Label(pestaña1,text="Nombre: ").pack()
txtNombre= Entry(pestaña1,textvariable=var1).pack()


var2 = tk.StringVar()
lblCorreo= Label(pestaña1,text="Correo:" ).pack()
txtCorreo= Entry(pestaña1,textvariable=var2).pack()
        
var3 = tk.StringVar()
lblContra= Label(pestaña1,text="Contraseña:" ).pack()
txtContra= Entry(pestaña1,textvariable=var3).pack()        

botonAcesso= Button(pestaña1,text="Guardar Usuario", bg="green", command=ejecutaInsert )
botonAcesso.pack()




panel.add(pestaña1,text="Agregar Usuarios")
panel.add(pestaña2,text="Consultar Usuarios")
panel.add(pestaña3,text="Pestaña3")
panel.add(pestaña4,text="Pestaña4")

Ventana.mainloop()