from State.Estado import Estado

class Muerto(Estado):
    def actua(self, unEnte):
        print (unEnte, "está tieso, no puede actuar.")
        
    def esAtacadoPor(self, unEnte):
        print (unEnte, "está ya con Dios (muerto), no le puedes atacar.")