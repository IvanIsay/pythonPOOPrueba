from tkinter import messagebox
import sqlite3
import bcrypt


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
            
    def conexionUsuarios(self):
        try:
            conexion=sqlite3.connect("c:/Users/iigue/OneDrive/Documentos/pythonPOOPrueba/registroBD/Usuariox.db")
            print("Conectado a BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")
     
    def encriptarpass(self,con):
          passPlana=con
          passPlana= passPlana.encode() #convertirla en bytes
          sal= bcrypt.gensalt()
          passHa= bcrypt.hashpw(passPlana,sal)
          print(passHa)
          return passHa
        
    def IngresarUsuario(self,nom,cor,con):
        
        conexion= self.conexionUsuarios()
               
        if( nom== "" or cor == "" or  con == "" ):
             messagebox.showwarning("Cuidado","Formulario Incompleto")
             conexion.close()
        else:
            cursor= conexion.cursor()
            conH= self.encriptarpass(con)
            datos=(nom,cor,conH)
            sqlinsert="insert into registrados(nombre,correo,pass) values(?,?,?)"
            
            cursor.execute(sqlinsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito","Usuario agregado en BD")
            
    def consultatodos(self):
        conexion= self.conexionUsuarios()
        try:
            cursor= conexion.cursor()
            sqlSelect= "select * from registrados"
            cursor.execute(sqlSelect)    
            usuarios= cursor.fetchall()
            conexion.close()
            return usuarios
            
        except sqlite3.OperationalError:
            print("No se pudo conectar a la BD")       
            
            
        """
        PARA ENCRYPTAR PASS
        1. INSTALAR BCRYPT
        - pip install bcrypt
        
        
        """