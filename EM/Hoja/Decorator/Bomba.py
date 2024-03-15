from EM.Hoja.Decorator.Decorator import Decorator

class Bomba(Decorator):
    def __init__(self):
        self.activa = False

    def desactivar(self):
        self.activa = False
        print('Bomba desactivada')

    def activar(self):
        self.activa = True
        print('Bomba activada')

    def get_activa(self):
        return self.activa

    def set_activa(self, value):
        self.activa = value

    #Testings
    def esBomba(self):
        return True
    
    #No hacer caso a este metodo
    def entrar(self):
        pass
    
    def entrar_alguien(self, alguien):
        pass  
    
    def recorrer(self):
        pass

