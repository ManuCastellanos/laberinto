class ElementoMapa():
    def __init__(self):
        self.padre = None
        self.comandos = []
        
    def es_padre(self, anObject):
        self.padre = anObject

    def esBomba(self):
        return False

    def esHabitacion(self):
        return False

    def esPared(self):
        return False

    def esPuerta(self):
        return False

    def esArmario(self):
        return False
    
    def esParedBomba(self):
        return False
    
    def esTunel(self):
        return False
    
    def agregarComando(self, unComando, receptor):
        self.comandos.append(unComando)
        unComando.receptor = receptor
    
    def quitarComando(self, unComando):
        if self.comandos is not None:
            self.comandos.remove(unComando)
    
    def obtenerComandos(self,alguien):
        return self.comandos
            
    #Patrón: Iterator
    def recorrer(self, unBloque):
       unBloque(self)

    def entrar(self,alguien):
        pass
    
    def cerrar(self,alguien):
        pass
    
    def strComandos(self):
        salida = ""
        for comando in self.comandos:
            salida += comando.__str__()
        return salida