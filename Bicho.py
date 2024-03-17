class Bicho:
    
    # Constructor
    def __init__(self):
        self.modo = None
        self.vidas = 0
        self.poder = 0
        self.posicion = None

    # Accion
    def actua(self):
        self.modo.actua(self)

    # Metodos Caminar
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)
    
    # Como el toString de Java
    def __str__(self):
        return "Bicho es " + str(self.modo)
    
    def irAlNorte(self):
        self.posicion.irAlNorte(self)
    
    def irAlSur(self):
        self.posicion.irAlSur(self)
    
    def irAlEste(self):
        self.posicion.irAlEste(self)
    
    def irAlOeste(self):
        self.posicion.irAlOeste(self)
    