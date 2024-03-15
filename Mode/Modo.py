import time

class Modo:
    def actua(self, unBicho):
        self.dormir(unBicho)
        self.caminar(unBicho)
        # self.atacar

    def caminar(self, unBicho):
        unBicho.caminarAleatorio()


    def dormir(self, unBicho):
        print(unBicho.printString(), 'duerme')
        time.sleep(2)