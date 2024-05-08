import time

class ModoCompañero():
    
    def actuaC(self, compañero, personaje):
       self.action(compañero,personaje)
       self.dormir(compañero)
       
    def caminar(self, compañero):
        compañero.caminarAleatorio()
    
    def actuar(self, personaje):
        pass
    
    def dormir(self, compañero):
        print(str(compañero)+' se queda dormido')
        time.sleep(5)
    
    def action(self, compañero, personaje):
        print(str(compañero)+' actua')
        compañero.actuar(personaje)
        
    def esCompañero(self):
        return False

    