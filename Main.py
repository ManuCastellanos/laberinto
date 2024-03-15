
from EM.Cont.Laberinto import Laberinto
from Game.Juego import Juego



juego= Juego()

juego.fabricarLaberinto4Habitaciones4BichosFM()

juego.abrirPuertas()
print(juego)

juego.lanzarHilo(juego.bichos[0])

