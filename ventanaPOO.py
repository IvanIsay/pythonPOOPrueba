
from tkinter import Tk,Button,Frame

Ventana= Tk()
Ventana.title("2 Frames")
Ventana.geometry("500x300")



seccion1= Frame(Ventana,bg="red")
seccion1.pack(expand= True, fill= 'both')

seccion2= Frame(Ventana,bg="gray")
seccion2.pack(expand= True, fill= 'both')

botonazul= Button(seccion1,text="blue", fg="blue")
botonazul.pack()

botonnegro= Button(seccion2,text="black", fg="black")
botonnegro.pack()

Ventana.mainloop()



#1.Ventana
#2.Secciones
#3.Botones 