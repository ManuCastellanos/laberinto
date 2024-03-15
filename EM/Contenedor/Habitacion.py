import random

from EM.Contenedor import Contenedor


class Habitacion(Contenedor):
    
    #Constructor
    def __init__(self, num, este=None, oeste=None, sur=None, norte=None):
        self.num = num
        self.este = este
        self.oeste = oeste
        self.sur = sur
        self.norte = norte

    #Getters y Setters
    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num

    def get_este(self):
        return self.este

    def set_este(self, este):
        self.este = este

    def get_oeste(self):
        return self.oeste

    def set_oeste(self, oeste):
        self.oeste = oeste

    def get_sur(self):
        return self.sur

    def set_sur(self, sur):
        self.sur = sur

    def get_norte(self):
        return self.norte

    def set_norte(self, norte):
        self.norte = norte

    #Metodos de la clase
    def recorrer(self, unBloque):
        unBloque(self)
        self.este.recorrer(unBloque)
        self.oeste.recorrer(unBloque)
        self.sur.recorrer(unBloque)
        self.norte.recorrer(unBloque)
    
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
        return "Hab" + str(self.num)

    # Representación
    def __repr__(self, aStream):
        aStream.write('Hab')
        aStream.write(str(self.num))

    # Testers
    def esHabitacion(self):
        return True