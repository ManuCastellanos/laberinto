import random

from EM.Container.Contenedor import Contenedor


class Habitacion(Contenedor):
    
    #Constructor
    def __init__(self, num, este=None, oeste=None, sur=None, norte=None):
        super().__init__()
        self.num = num
        self.este = este
        self.oeste = oeste
        self.sur = sur
        self.norte = norte


    def entrar(self, alguien):
        print(alguien, "ha entrado en la habitacion-", self.num)
        alguien.posicion = self

    def caminarAleatorio(self, unEnte):
        numOr = len(self.orientaciones)
        numAl = random.randint(1, numOr)
        orAl = self.orientaciones[numAl - 1]
        orAl.caminar(unEnte)

    def irAlEste(self, alguien):
        self.este.entrar(alguien)

    def irAlOeste(self, alguien):
        self.oeste.entrar(alguien)
    
    def irAlSur(self, alguien):
        self.sur.entrar(alguien)
    
    def irAlNorte(self, alguien):
        self.norte.entrar(alguien)
    
        
    # To String
    def __str__(self):
        salida= f"*Habitacion {self.num}\n"
        
        salida += f"Este: {self.este}\n"
        salida += f"Oeste: {self.oeste}\n"
        salida += f"Sur: {self.sur}\n"
        salida += f"Norte: {self.norte}\n"
        
        for hijo in self.hijos:
            salida += hijo.__str__() + "\n"
        return salida


    # Testers
    def esHabitacion(self):
        return True