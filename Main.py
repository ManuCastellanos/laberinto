
from EM.Cont.Laberinto import Laberinto
from Game.Juego import Juego


laberinto= Laberinto()

j1=Juego(laberinto).fabricarLaberinto2Habitaciones()

j2=Juego(laberinto).fabricarLaberinto2HabitacionesFM()

j3= Juego(laberinto).fabricarLaberinto2HabitacionesFMD()

j2 = Juego(laberinto).fabricarLaberinto2Habitaciones2BombasFM()

j4= Juego(laberinto).fabricarLaberinto4Habitaciones4BichosFM()

