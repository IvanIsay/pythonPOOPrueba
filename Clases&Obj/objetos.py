
from Personaje import *

#1. Solicitud de atributos de los objetos
print("")
print("###### Datos Heroe ###### ")
especieH= input("Ingresa la especie del Heroe")o
nombreH= input("Ingresa el nombre del Heroe")
alturaH= input("Ingresa la altura del Heroe")
recargaH= int(input("Cuantas Balas recargaras al Heroe"))

print("")
print("###### Datos Villano ###### ")
especieV= input("Ingresa la especie del villano")
nombreV= input("Ingresa el nombre del villano")
alturaV= input("Ingresa la altura del villano")
recargaV= int(input("Cuantas Balas recargaras al Villano"))


#2. Crear objeto heroe y villano

heroe= Personaje(especieH,nombreH,alturaH)
villano= Personaje(especieV,nombreV,alturaV)




#3. Usar Atributos y Metodos de Heroe
print("")
print("###### Atributos y Metodos Heroe ###### ")
print("El personaje se llama: "+ heroe.getNombre() )
print("pertenece a la especie: "+ heroe.getEspecie() )
print("y tiene una altura de : "+ heroe.getAltura() )

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargaH)


#3. Usar Atributos y Metodos de Villano
print("")
print("###### Atributos y Metodos Villano ###### ")
print("El personaje se llama: "+ villano.getNombre() )
print("pertenece a la especie: "+ villano.getEspecie() )
print("y tiene una altura de : "+ villano.getAltura() )

villano.correr(False)
villano.lanzarGranadas()
villano.recargarArma(recargaV)