import time

class ModoPersonaje():
    
    def actua(self, unPersonaje):
        self.correrse(unPersonaje)
        self.parar(unPersonaje)
        self.caminar(unPersonaje,unPersonaje.posicion)
        
    def correrse(self, unPersonaje):
        print(str(unPersonaje)+' se corre')   
    
    def caminar(self, unPersonaje,unaOr):
       unPersonaje.irA(unaOr)
    
    def parar(self, unPersonaje):
        print(str(unPersonaje)+' se queda quieto parao')
        time.sleep(2)