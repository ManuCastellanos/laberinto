class Forma():
    def __init__(self):
        self.orientaciones = []
        self.x = 0
        self.y = 0
        
    def pasar(self, unVisitor):
        for orientacion in self.orientaciones:
            orientacion.pasarA(unVisitor,self)
    
    def agregarOrientacion(self, unaOrientacion):
        self.orientaciones.append(unaOrientacion)
    
    def obtenerElemento(self, unaOr):
        return unaOr.obtenerElementoEn(self)
    
    def ponerElemento(self, unaOr, unEM):
        unaOr.ponerElementoEn(unEM, self)
    
    def recorrer(self, unBloque):
        for orientacion in self.orientaciones:
            orientacion.recorrerEn(unBloque, self)   
            
    def __str__(self):
        return f"Forma en ({self.orientaciones})"