class Bicho:
    
    # Constructor
    def __init__(self):
        self.modo = None
        self.vidas = 0
        self.poder = 0
        self.posicion = None

    # Getters y setters
    def get_modo(self):
        return self.modo

    def set_modo(self, modo):
        self.modo = modo

    def get_vidas(self):
        return self.vidas

    def set_vidas(self, vidas):
        self.vidas = vidas

    def get_poder(self):
        return self.poder

    def set_poder(self, poder):
        self.poder = poder

    def get_posicion(self):
        return self.posicion

    def set_posicion(self, posicion):
        self.posicion = posicion

    # Accion
    def actua(self):
        self.modo.actua(self)

    # Metodos Caminar
    def caminarAleatorio(self):
        self.posicion.caminarAleatorio(self)

    def irAlEste(self):
        self.posicion.irAlEste(self)

    def irAlNorte(self):
        self.posicion.irAlNorte(self)

    def irAlOeste(self):
        self.posicion.irAlOeste(self)

    def irAlSur(self):
        self.posicion.irAlSur(self)
    
    # Como el toString de Java
    def __str__(self):
        return "Bicho es " + str(self.modo)
    
    def printOn(self, aStream):
        aStream.nextPutAll('Bicho-')
        aStream.nextPutAll(str(self.modo))