from Orientation.Orientacion import Orientacion

class Este(Orientacion):
    #Patrón: Singleton
    UnicaInstancia = None
    
    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def caminar(self, alguien):
        alguien.irAlEste()

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.este=unEM
    
    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.este is not None:
            unContenedor.este.recorrer(unBloque)
