from EM.ElementoMapa import ElementoMapa # Importamos la clase ElementoMapa para la herencia

class Contenedor(ElementoMapa): # Creamos la clase Contenedor que hereda de ElementoMapa
    
    def __init__(self): # Constructor de la clase (initialization)
        super().__init__() # Llamamos al constructor de la clase padre
        self.hijos = []
        self.forma= None
        self.norte= None
        self.sur= None
        self.este= None
        self.oeste= None
        
    
    def __init__(self, num):
        super().__init__()
        self.num= num
        self.hijos = []
        self.orientaciones = []
        self.norte= None
        self.sur= None
        self.este= None
        self.oeste= None
        self.forma= None
        
    # Metodos de la clase
    def ponerElementoEn(self, unaOr, unEM): 
        self.forma.ponerElemento(unaOr, unEM)
        
    def obtenerElementoEn(self, unaOr):
        return self.forma.obtenerElemento(unaOr)
    
    def agregarHijo(self, unEM): #unEM es un ElementoMapa
        self.hijos.append(unEM)
        unEM.es_padre(self)

    def eliminarHijo(self, unEM ):     
        if unEM in self.hijos:
            self.hijos.remove(unEM)
        else:
            print("No se puede eliminar EM")
    
    def agregarOrientacion(self, unaOrientacion):
       self.forma.agregarOrientacion(unaOrientacion)

    
    def irAlEste(self, alguien):
        self.este.entrar(alguien)

    def irAlOeste(self, alguien):
        self.oeste.entrar(alguien)
    
    def irAlSur(self, alguien):
        self.sur.entrar(alguien)
    
    def irAlNorte(self, alguien):
        self.norte.entrar(alguien)
        
    #Patrón: Iterator
    def recorrer(self, unBloque):
        unBloque(self)
        
        for hijo in self.hijos:
            hijo.recorrer(unBloque)
        
        for orientacion in self.orientaciones:
            orientacion.recorrerEn(unBloque, self)
        
    def entrar(self,alguien):
        pass
    


    
    
    