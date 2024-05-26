from EM.Hoj.Hoja import Hoja

class Tunel(Hoja):
    def __init__(self):
        super().__init__()
        self.laberinto = None
    
    def esTunel(self):
        return True
    
    def entrar(self,alguien):
        if self.laberinto == None:
            self.laberinto = alguien.juego.clonarLaberinto()
            
            for hab in self.laberinto.hijos:
                for tunel in hab.hijos:
                    if tunel.esTunel():
                        tunel.laberinto = alguien.juego.laberinto
            self.laberinto.entrar(alguien)
            print("\n\n Entrando al laberinto"+str(self.laberinto.num))
        
        print ("Saliendo a laberinto" + str(self.laberinto.num))
        
    def __str__(self):
        if self.laberinto == None:
            return "Tunel sin laberinto"
        
        else:
            laberinto = f"tiene el laberinto {self.laberinto.num}\n"
        
        return f"Tunel {laberinto}"
    
        #def aceptar (self, visitante):
        #visitante.visitarTunel(self)
    