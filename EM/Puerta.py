from EM.ElementoMapa import ElementoMapa
from EM.ElementoMapa import ElementoMapa


class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False

    
    def __str__(self):
        return "Puerta de hab" + str(self.lado1.num) + " a hab" + str(self.lado2.num)

    def entrar(self,alguien):
        if self.abierta:
            if self.lado1 == alguien.posicion:
                self.lado2.entrar(alguien)
                alguien.posicion = self.lado2
            else:
                self.lado1.entrar(alguien)
                alguien.posicion = self.lado1    
        else:
            print(str(alguien)+" HA PEGADO UN PORTAZO")
    
    def abrir(self):
        self.abierta = True
        print("Puerta abierta")
    
    def cerrar(self):
        self.abierta = False
        print("Puerta cerrada")
    
    #testing
    def esPuerta (self):
        return True
    