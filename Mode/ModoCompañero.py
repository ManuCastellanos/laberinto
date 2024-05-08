import time

class ModoCompañero():
    
    def __init__(self):
        pass
    
    
    def action(self, compañero, personaje):
       self.caminar(compañero)
       self.actua(compañero,personaje)
       self.dormir(compañero)
       
    def caminar(self, compañero):
        orientacion= compañero.obtenerOrientacionAleatoria()
        compañero.irA(orientacion)
    
    def dormir(self, compañero):
        print(str(compañero)+' se queda dormido')
        time.sleep(5)
    
    def actua(self, compañero, personaje):
        print(str(compañero)+' actua')
        compañero.actuar(personaje)
        
    def esCompañero(self):
        return False

    