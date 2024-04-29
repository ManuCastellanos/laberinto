import random

from EM.Container.Contenedor import Contenedor


class Armario(Contenedor):
    
    #Constructor
    def __init__(self, num, este=None, oeste=None, sur=None, norte=None):
        super().__init__(num)
        self.este = este
        self.oeste = oeste
        self.sur = sur
        self.norte = norte


    def entrar(self, alguien):
        print(alguien, "está en el armario", self.num)
        alguien.posicion = self
 
        
    # To String
    def __str__(self):
        salida= f"*Armario {self.num}\n"
        
        salida += f"Este: {self.este}\n"
        salida += f"Oeste: {self.oeste}\n"
        salida += f"Sur: {self.sur}\n"
        salida += f"Norte: {self.norte}"
        
        for hijo in self.hijos:
            salida +=+ hijo.__str__() + "\n"
        return salida


    # Testers
    def esArmario(self):
        return True