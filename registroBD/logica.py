from tkinter import messagebox
import sqlite3
import bcrypt


class logica:
    
    def __init__(self):
        pass

            
    def conexionUsuarios(self):
        try:
            conexion=sqlite3.connect("C:/Users/lOkY/Documents/GitHub/pythonPOOPrueba/registroBD/Usuariox.db")
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
            sqlinsert="insert into registrados(nombre,correo,contra) values(?,?,?)"
            
            cursor.execute(sqlinsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Exito","Usuario agregado en BD")
            
    
    def buscaUsuario(self,id):
        conexion= self.conexionUsuarios()
        if( id == "" ):
             messagebox.showwarning("Cuidado","Escribe un Id Valido")
             conexion.close()

        else: 
            
            try:
                cursor= conexion.cursor()
                sqlSelect= "select * from registrados where id ="+id
                cursor.execute(sqlSelect)    
                usuario= cursor.fetchall()
                conexion.close()
                return usuario
            
            except sqlite3.OperationalError:
                print("Error Consulta")       
            
    
    
    
    
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
            print("Error Consulta")       
            
            
        """
        PARA ENCRYPTAR PASS
        1. INSTALAR BCRYPT
        - pip install bcrypt
        
        
        """