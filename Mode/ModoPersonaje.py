import time

class ModoPersonaje():
    
    def caminar(self, unPersonaje,unaOr):
       unPersonaje.irA(unaOr)
    
    def parar(self, unPersonaje):
        print(str(unPersonaje)+' se queda quieto parao')
        time.sleep(2)