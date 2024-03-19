from EM.ElementoMapa import ElementoMapa


class Pared(ElementoMapa):
    def __init__(self):
        super().__init__()

    def entrar(self,alguien):
        print(str(alguien)+" se ha chocado con una pared")
        
    #Testing
    def esPared(self):
        return True
    
    def __str__(self):
        return "Pared"