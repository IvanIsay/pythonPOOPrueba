from tkinter import Tk,Button,Frame,messagebox


#5.MessageBox
def mostrarMensajes():
    messagebox.showinfo("showinfo", "Information")
    messagebox.showerror("showerror", "Error")
    print(messagebox.askokcancel(message="¿Desea continuar?", title="Título"))

#6.Agregar Botones  
def agregarbotones():
    botonverde.config(text="+")
    botonNuevo= Button(seccion3,text="Nuevo", bg="green")
    botonNuevo.configure(height=3,width=5 )
    botonNuevo.pack()

#1.Ventana
Ventana= Tk()
Ventana.title("3 Frames")
Ventana.geometry("600x400")


#2.Secciones
seccion1= Frame(Ventana,bg="red")
seccion1.pack(expand= True, fill= 'both')

seccion2= Frame(Ventana,bg="gray")
seccion2.pack(expand= True, fill= 'both')

seccion3= Frame(Ventana,bg="pink")
seccion3.pack(expand= True, fill= 'both')



#3.Botones 

botonazul= Button(seccion1,text="azul", fg="blue",command=mostrarMensajes)
botonazul.place(x=60,y=60,  width=100, height=30)


botonnegro= Button(seccion2,text="negro", fg="black")
botonnegro.configure(height=2,width=10)
botonnegro.grid(row=0, column=1)

botonamarillo= Button(seccion2,text="amarillo", fg="yellow")
botonamarillo.configure(height=2,width=5 )
botonamarillo.grid(row=1, column=2)

botonverde= Button(seccion3,text="verde", fg="green",command=agregarbotones )
botonverde.configure(height=3,width=5 )
botonverde.pack()


#4.Posicionamiento

#Main
Ventana.mainloop()




'''
showinfo()
showwarning()
showerror()
askquestion()
askyesno()
askokcancel()
askyesnocancel()
askretrycancel()
'''




