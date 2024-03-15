from EM.Hoj.Deco.Decorator import Decorator

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
    
    def __str__(self):
        if self.activa == False:
            return f"Bomba-" + "(Desactivada)"
        else:
            return f"Bomba-" + "(Activada)"
        
        