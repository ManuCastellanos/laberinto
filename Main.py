
from EM.Container.Laberinto import Laberinto
from Game.Juego import Juego
from LaberintoAFactory import LaberintoAFactory 
from Builder.Director import Director


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

#juego.fabricarLaberinto4Habitaciones4BichosFM()
#juego.lanzarHilo(juego.bichos[0])
#print(juego)

#af= LaberintoAFactory()

#juego.fabricarLaberinto4Hab4Bomb4BichosAF(af)

#print(juego)

#BUILDER
#archivo='JSON/lab2hab2bichos.json'
#archivo='JSON/laberinto2hab.json'
archivo= 'JSON/lab2hab2bichos2bombas.json'
archivo= 'JSON/lab4hab4bichos2bom.json'
director= Director()

director.procesar(archivo)
juego= director.getJuego()
juego.activarBombas()
print(juego)

