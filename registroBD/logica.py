from tkinter import messagebox
import sqlite3


class logica:
    
    def __init__(self):
        self.__correoC= "iiguerra@outlook.com"
        self.__contraC="1a2b3c4d"
        
    def validarCredenciales(self,correo,contra):
        
        if(correo == "" or contra == ""):
             messagebox.showwarning("Cuidado","Usuario y contraseña debe contener algo")
        else:
            if(self.__correoC == correo and self.__contraC == contra):
                messagebox.showinfo("Exito","Bienvenido al sistema")
            else:
                messagebox.showerror("Error","Revisa tus credenciales")
            
 
    def IngresarUsuario(self,nom,cor,con):
        
        try:
            conexion=sqlite3.connect("Usuarios.db")
            print("Conectado a BD")
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
                 
        if(cor == "" or con == "" or nom== ""):
             messagebox.showwarning("Cuidado","Formulario Incompleto")
        else:
            conexion.execute("insert into usuario(nombre,correo,pass) values(?,?,?)",(nom,cor,con))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito","Usuario agregado en BD")