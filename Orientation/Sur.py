from Orientation.Orientacion import Orientacion

class Sur(Orientacion):
    # Patrón: Singleton
    UnicaInstancia = None
    
    def __new__(cls):
        if cls.UnicaInstancia is None:
            cls.UnicaInstancia = super().__new__(cls)
        return cls.UnicaInstancia
    
    def caminar(self, alguien):
        alguien.irAlSur()

    def ponerElemento(self, unEM, unContenedor):
        unContenedor.sur=unEM
    
    def recorrerEn(self, unBloque, unContenedor):
        if unContenedor.sur is not None:
            unContenedor.sur.recorrer(unBloque)
