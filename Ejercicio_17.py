# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_17: Aproximacion de PI

def aproximarPI(n):         #Aproxima PI con el valor n
    suma = 0
    contador = 19999
    for d in range (1, n+1, 2):
        if contador%2 == 1:
            suma+= 1/d
        else:
            suma-= 1/d
        contador+= 1
    return suma * 4



print(aproximarPI(9999))