from tkinter import Tk,Button,Frame,messagebox

#5.MessageBox
def mostrarMensajes():
    print(messagebox.showinfo("showinfo", "Information"))
    print(messagebox.showerror("showerror", "Error"))
    print(messagebox.askokcancel(message="¿Desea continuar?", title="Título"))



#1.Ventana
Ventana= Tk()
Ventana.title("2 Frames")
Ventana.geometry("500x300")


#2.Secciones
seccion1= Frame(Ventana,bg="red")
seccion1.pack(expand= True, fill= 'both')

seccion2= Frame(Ventana,bg="gray")
seccion2.pack(expand= True, fill= 'both')


#3.Botones 

botonazul= Button(seccion1,text="blue", fg="blue",command=mostrarMensajes)
botonazul.place(x=60,y=60,  width=100, height=30)


botonnegro= Button(seccion2,text="black", fg="black")
botonnegro.configure(height=2,width=10)
botonnegro.grid(row=0, column=1)

botonamarillo= Button(seccion2,text="yellow", fg="yellow")
botonamarillo.configure(height=2,width=5 )
botonamarillo.grid(row=1, column=2)

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




