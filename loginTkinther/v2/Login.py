from tkinter import *
from logica import *
import tkinter as tk

class login:
    
    
    def __init__(self):
        
        axc= logica()

        def ejecutaVal():
         axc.validarCredenciales(self.__var1.get(),self.__var2.get())
         
        self.__Ventana= Tk()
        self.__Ventana.title("Login")
        self.__Ventana.geometry("300x150")
        
        self.__seccion1= Frame(self.__Ventana)
        self.__seccion1.pack(expand= True, fill= 'both')

        self.__titulo= Label(self.__seccion1,text="Login POO",bg="black", fg="white", font=("Helvetica", 18)).pack()

        self.__var1 = tk.StringVar()
        self.__lblCorreo= Label(self.__seccion1,text="Correo: ").pack()
        self.__txtCorreo= Entry(self.__seccion1 ,textvariable=self.__var1,takefocus=True).pack()


        self.__var2 = tk.StringVar()
        self.__lblContra= Label(self.__seccion1,text="Contraseña: ").pack()
        self.__txtContra= Entry(self.__seccion1,show="++" ,textvariable=self.__var2).pack()


        self.__botonAcesso= Button(self.__seccion1,text="Acceder", bg="green", command=ejecutaVal )
        self.__botonAcesso.pack()

        #Main
        self.__Ventana.mainloop()
