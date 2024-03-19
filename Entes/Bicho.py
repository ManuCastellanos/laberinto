from Entes.Ente import Ente 

class Bicho(Ente):
    # Constructor
    def __init__(self):
        super().__init__()

    def esBicho(self):
        return True
    
    def actua(self):
        self.modo.actua(self)
        
    # Metodos Caminar
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)
    
    # Como el toString de Java
    def __str__(self):
        return "Bicho " + str(self.modo)
    
