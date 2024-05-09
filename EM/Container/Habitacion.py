import random

from EM.Container.Contenedor import Contenedor


class Habitacion(Contenedor):
    
    #Constructor
    def __init__(self, num, este=None, oeste=None, sur=None, norte=None):
        super().__init__(num)



    def entrar(self, alguien):
        print(alguien, "ha entrado en la habitacion-", self.num)
        alguien.posicion = self
        
        if alguien.compi is not None:
            alguien.compi.posicion = self
        else:
            alguien.compi=alguien.juego.buscarCompiEn(alguien.posicion)
            if alguien.compi is not None:
                alguien.compi.posicion = self
            
    def caminarAleatorio(self, unEnte):
        numOr = len(self.forma.orientaciones)
        numAl = random.randint(1, numOr)
        orAl = self.forma.orientaciones[numAl - 1]
        orAl.caminar(unEnte)
    
        
    # To String
    def __str__(self):
        salida= f"*Habitacion {self.num}\n"
        
        salida += f"Norte: {self.forma.norte}\n"
        salida += f"Sur: {self.forma.sur}\n"
        salida += f"Este: {self.forma.este}\n"
        salida += f"Oeste: {self.forma.oeste}\n"
        
        for hijo in self.hijos:
            salida += "\n"+ hijo.__str__() + "\n"
        return salida


    # Testers
    def esHabitacion(self):
        return True