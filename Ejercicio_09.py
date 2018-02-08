# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_09: Condicionales

'''
import random

winMessages= ["Insane dubs!", "Magnific dubs!", "Nice dubs!"]


def calculateDubs(number):
    dubs = random.randint(0, 99999999999)
    if dubs % 7 == 0:
        win = number * 10
        message = ("You rolled %d and won %d points!" % (dubs, win))
    else:
        message = ("You rolled %d and lost!"% (dubs))
    return message



def main():
    rollNumber = int(input("!roll "))
    dubs = calculateDubs(rollNumber)
    print(dubs)


main()
'''


def main():
    carrera = input("Teclea tu carrera: ")
    if carrera == "INT" or carrera == "LAD":
        print("Te equivocaste de salón prro :v")
    else:
        print("Pase usted buen samaritano")

main()
