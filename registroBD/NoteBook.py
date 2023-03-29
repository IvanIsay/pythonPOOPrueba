from tkinter import *
from logica import *
from tkinter import ttk
import tkinter as tk

controlador= logica()

def ejecutaInsert():
    controlador.IngresarUsuario(var1.get(),var2.get(),var3.get())
    
def ejecutaBusqueda():
    usuario= controlador.buscaUsuario(varBus.get())
    for usu in usuario:
        cad= str(usu[0])+" "+usu[1]+" "+ usu[2]+" "+ str(usu[3])

    print(cad)
    

    


Ventana= Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")
nombre= StringVar()

panel= ttk.Notebook(Ventana)
panel.pack(fill='both', expand='yes')

pestaña1= ttk.Frame(panel)
pestaña2= ttk.Frame(panel)
pestaña3= ttk.Frame(panel)
pestaña4= ttk.Frame(panel)
pestaña5= ttk.Frame(panel)


# Pestaña1: Formulario Registro

titulo= Label(pestaña1,text="Registro Usuario", fg="blue", font=("Modern", 18)).pack()

var1 = tk.StringVar()
lblNombre= Label(pestaña1,text="Nombre: ").pack()
txtNombre= Entry(pestaña1,textvariable=var1).pack()


var2 = tk.StringVar()
lblCorreo= Label(pestaña1,text="Correo:" ).pack()
txtCorreo= Entry(pestaña1,textvariable=var2).pack()
        
var3 = tk.StringVar()
lblContra= Label(pestaña1,text="Contraseña:" ).pack()
txtContra= Entry(pestaña1,textvariable=var3).pack()        

botonAcesso= Button(pestaña1,text="Guardar Usuario", command=ejecutaInsert )
botonAcesso.pack()


# Pestaña2: Buscar Usuario

titulo= Label(pestaña2,text="Buscar usuario", fg="green", font=("Modern", 18)).pack()

varBus = tk.StringVar()
lblid= Label(pestaña2,text="Id: ").pack()
txtid= Entry(pestaña2,textvariable=varBus).pack()

botonBusqueda= Button(pestaña2,text="Buscar Usuario", command= ejecutaBusqueda)
botonBusqueda.pack()

subtitulo= Label(pestaña2,text="Registrado: ", fg="blue", font=("Modern", 15)).pack()

textBus= tk.Text(pestaña2,height=5,width=52).pack()



panel.add(pestaña1,text="Agregar Usuarios")
panel.add(pestaña2,text="Buscar Usuario")
panel.add(pestaña3,text="Consultar Usuarios")
panel.add(pestaña4,text="Actualizar Usuario")
panel.add(pestaña5,text="Eliminar Usuario")

Ventana.mainloop()





