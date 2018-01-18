#encoding: UTF-8
#Autor: Sebastian Morales Martin
#Ejemplo

from random import randint as rani

tijeras = 3
papel = 2
piedra = 1

eleccionComputadora= rani(1,3)

print("-----------------------------------")
print("\n")
print("piedraPapelYTijeras.py")
print("\n")
print("-----------------------------------")
print("\n")
print("1 = piedra")
print("\n")
print("2 = papel")
print("\n")
print("3 = tijeras")
print("\n")
print("-----------------------------------")


eleccionHumano = input("Introduce tu respuesta, usa la guía arriba para basar tu eleccion: ")


if eleccionComputadora == 1 and eleccionHumano == 3:
    respuesta = "La computadora elije Piedra, tu piedres"
elif eleccionComputadora == 2 and eleccionHumano == 1:
    respuesta = "La computadora elije Papel, tu pierdes"
elif eleccionComputadora == 3 and eleccionHumano == 2:
    respuesta ="La computadora elije Tijeras, tu pierdes"
elif eleccionComputadora and eleccionHumano == 3:
    respuesta = "Los dos escogieron Tijeras, empate!"
elif eleccionComputadora and eleccionHumano == 2:
    respuesta = "Los dos escogieron Papel, empate!"
elif eleccionComputadora and eleccionHumano == 1:
    respuesta = "Los dos escogieron Piedra, empate!"
elif eleccionComputadora == 3 and eleccionHumano == 1:
    respuesta = "la computadora elije Tijeras, ganas!"
elif eleccionComputadora == 2 and eleccionHumano == 3:
    respuesta = "La computadora elije Papel, ganas!"
elif eleccionComputadora == 1 and eleccionHumano == 2:
    print("La computadora elige piedra, ganas!")