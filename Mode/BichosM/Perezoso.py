from Mode.ModoBicho import ModoBicho

class Perezoso(ModoBicho):

    def actua(self, unBicho):
        super().actua(unBicho)
        
    def esPerezoso(self):
        return True
    
    def __str__(self):
        return 'Perezoso'

