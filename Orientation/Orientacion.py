from abc import ABC, abstractmethod

class Orientacion(ABC):
    def caminar(self, unEnte):
       pass

    def ponerElementoEn(self, unEM, unContenedor):
       pass

    def recorrerEn(self, unBloque, unContenedor):
        pass
    
    def obtenerElementoEn(self, unContenedor):
        pass