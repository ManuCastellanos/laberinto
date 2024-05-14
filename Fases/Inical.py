from Fases.Fase import Fase

class Inicial(Fase):
    def esInicial(self):
        return True
    
    def agregarIniProta(self, prota, juego):
        juego.puedeIniProta(prota)
        