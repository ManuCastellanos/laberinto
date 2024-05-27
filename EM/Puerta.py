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
                
    def __str__(self):
        return "Puerta de hab" + str(self.lado1.num) + " a hab" + str(self.lado2.num) + " acciones: " + str(self.strComandos())

    def entrar(self,alguien):
        if self.abierta:
            if self.lado1 == alguien.posicion:
                self.lado2.entrar(alguien)
                alguien.posicion = self.lado2
            else:
                self.lado1.entrar(alguien)
                alguien.posicion = self.lado1    
            
            if not alguien.esBicho():
                if alguien.compi is not None:
                    alguien.compi.posicion = alguien.posicion    
        else:
            print(str(alguien)+" HA PEGADO UN PORTAZO")
    
    def abrir(self,alguien):
        self.abierta = True
        if(self.abierta == True):
            print("Puerta abierta por Dios")
        else:
            print("Puerta abierta por", alguien)

        for comando in self.comandos:
            if comando.esAbrir():
                self.quitarComando(comando)
                self.agregarComando(Cerrar(), self)

    def cerrar(self, alguien):
        self.abierta = False
        if(self.abierta == False):
            print("Puerta cerrada por Dios")
        else:
            print("Puerta cerrada por ", alguien)
        for comando in self.comandos:
            if comando.esCerrar():
                self.quitarComando(comando)
                self.agregarComando(Abrir(), self)
                
        
    #testing
    def esPuerta (self):
        return True
    