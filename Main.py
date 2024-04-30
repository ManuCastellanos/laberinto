from EM.Container.Laberinto import Laberinto
from Game.Juego import Juego
from LaberintoAFactory import LaberintoAFactory 
from Builder.Director import Director
from Orientation.Norte import Norte
from Orientation.Este import Este
from Orientation.Oeste import Oeste
from Orientation.Sur import Sur


juego= Juego()

#juego.fabricarLaberinto2Habitaciones()
#print(juego)

#juego.fabricarLaberinto2HabitacionesFM()
#print(juego)

#juego.fabricarLaberinto2HabitacionesFMD()
#juego.abrirPuertas()
#print(juego)

#juego.fabricarLaberinto2Habitaciones2BombasFM()
#juego.activarBombas()
#print(juego)

# juego.fabricarLaberinto4Habitaciones4BichosFM()
# juego.lanzoBichos()
# print(juego)

#af= LaberintoAFactory()

#juego.fabricarLaberinto4Hab4Bomb4BichosAF(af)

#print(juego)
# juego.fabricarLaberintoPersonajes()
# print(juego)

#BUILDER
#archivo='JSON/lab2hab2bichos.json'
#archivo='JSON/laberinto2hab.json'
#archivo= 'JSON/lab2hab2bichos2bombas.json'
# archivo= 'JSON/lab4hab4bichos2bom.json'
archivo='JSON/lab4habTunelArm.json'
director= Director()

director.procesar(archivo)
juego= director.getJuego()
juego.abrirPuertas()
juego.iniProta("Imbécil")
print(juego)

