from Comandos.Abrir import Abrir
from Comandos.Cerrar import Cerrar
from EM.ElementoMapa import ElementoMapa
from EM.ElementoMapa import ElementoMapa


class Puerta(ElementoMapa):
    def __init__(self, lado1, lado2):
        super().__init__()
        self.lado1 = lado1
        self.lado2 = lado2
        self.abierta = False
        self.pasada= False
        self.agregarComando(Abrir(),self)
        self.agregarComando(Cerrar(),self)
                
    def __str__(self):
        return "Puerta de hab" + str(self.lado1.num) + " a hab" + str(self.lado2.num) + " abierta: " + str(self.abierta)

    def entrar(self,alguien):
        if self.abierta:
            if self.lado1 == alguien.posicion:
                self.lado2.entrar(alguien)
                alguien.posicion = self.lado2
            else:
                self.lado1.entrar(alguien)
                alguien.posicion = self.lado1    
                
            if alguien.compañero is not None:
                alguien.compañero.posicion = alguien.posicion    
        else:
            print(str(alguien)+" HA PEGADO UN PORTAZO")
    
    def abrir(self,alguien):
        self.abierta = True
        print("Puerta abierta por", alguien)

    def cerrar(self, alguien):
        self.abierta = False
        print("Puerta cerrada", alguien)
    
    #testing
    def esPuerta (self):
        return True
    