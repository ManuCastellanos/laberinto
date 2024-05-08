import time

class ModoBicho():
    def actua(self, unBicho):
        self.dormir(unBicho)
        self.caminar(unBicho)
        # self.atacar

    def caminar(self, unBicho):
        unBicho.caminarAleatorio()


    def dormir(self, unBicho):
        print(str(unBicho)+' duerme')
        time.sleep(2)
    
    def atacar(self, unBicho):
        unBicho.atacar()