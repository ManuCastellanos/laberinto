import random

from EM.Cont.Contenedor import Contenedor


class Habitacion(Contenedor):
    
    #Constructor
    def __init__(self, num, este=None, oeste=None, sur=None, norte=None):
        super().__init__()
        self.num = num
        self.este = este
        self.oeste = oeste
        self.sur = sur
        self.norte = norte

    
    def entrar(self):
        print("Estas en la habitacion-", self.num)


    def entrar_alguien(self, alguien):
        print(alguien, "ha entrado en la habitacion-", self.num)
        alguien.posicion = self

    def caminarAleatorio(self, unBicho):
        numOr = len(self.orientaciones)
        numAl = random.randint(1, numOr)
        orAl = self.orientaciones[numAl - 1]
        orAl.caminar(unBicho)

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
         
        return salida

    # Representación
    def __repr__(self, aStream):
        aStream.write('Hab')
        aStream.write(str(self.num))

    # Testers
    def esHabitacion(self):
        return True