class Personaje:
    
    #Constuctor con paramentros de inializacion
    def __init__ (self, esp,nom, alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    
    #Metodos Personaje
    
    def correr(self,status):
        if(status):
            print("El personaje "+ self._nombre +" esta corriendo")
        else:
            print("El personaje "+ self._nombre +" se detuvo")
    
    def lanzarGranadas(self):
            print("El personaje "+ self._nombre +" lanzo una granada") 
            
    def recargarArma(self, municiones):
        cargador= 10
        cargador= cargador + municiones
        print("El arma tiene "+ str(cargador) +" balas")
        
    def __pensar(self):
        print("El personaje esta pensando") 


# Definimos Getters y Setters

    # getter method
    def getEspecie(self):
        return self.__especie
      
    def setEspecie(self, x):
        self._especie = x

    def getNombre(self):
        return self.__nombre
      
    def setNombre(self, x):
        self.__nombre = x
        
    def getAltura(self):
        return self.__altura
      
    def setAltura(self, x):
        self.__altura = x