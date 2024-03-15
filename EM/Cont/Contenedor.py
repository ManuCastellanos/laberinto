from EM.ElementoMapa import ElementoMapa # Importamos la clase ElementoMapa para la herencia

class Contenedor(ElementoMapa): # Creamos la clase Contenedor que hereda de ElementoMapa
    
    def __init__(self): # Constructor de la clase (initialization)
        
        super().__init__() # Llamamos al constructor de la clase padre
        self.hijos = []
        self.orientaciones = []

    # Metodos de la clase
    def agregarHijo(self, unEM): #unEM es un ElementoMapa
        self.hijos.append(unEM)
        unEM.set_padre(self)

    def eliminarHijo(self, unEM ):     
        if unEM in self.hijos:
            self.hijos.remove(unEM)
        else:
            print("No se puede eliminar EM")
    
    def agregarOrientacion(self, unaOrientacion):
        self.orientaciones.append(unaOrientacion) #.append al final de la lista, al principio .insert(0, unaOrientacion)
    
    #Patrón: Iterator
    def recorrer(self, unBloque):
        unBloque(self)
        
        for hijo in self.hijos:
            hijo.recorrer(unBloque)
        
        for orientacion in self.orientaciones:
            orientacion.recorrer(unBloque)
        
    def entrar(self):
        pass
    
    def entrar_alguien(self, alguien):
        pass
    
    # Getters y Setters de la clase
    def get_hijos(self):
        return self.hijos

    def set_hijos(self, anObject):
        self.hijos = anObject

    def get_orientaciones(self):
        return self.orientaciones

    def set_orientaciones(self, anObject):
        self.orientaciones = anObject
    
    
    