from EM.Hoj.Hoja import Hoja

class Decorator(Hoja):
    def __init__(self, em):
        super().__init__()
        self.em = em

    #Getters and Setters
    def get_em(self):
        return self.em
    
    def set_em(self, em):
        self.em = em
    