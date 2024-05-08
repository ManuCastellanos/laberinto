from Mode.ModoBicho import ModoBicho

class Agresivo(ModoBicho):

    def actua(self, unBicho):
        super().actua(unBicho)
    
    def esAgresivo(self):
        return True
    
    def __str__(self):
        return 'Agresivo'

