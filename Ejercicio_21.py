# encoding: UTF-8
# Sebastian Morales Martin
# Ejercicio_22
from random import randint as r
from getpass import getuser as g
user = g()
def generarLista(n):            # genera una lista al azar con parametros de 0 a 255 de longitud n
    lista = []
    for k in range(n):
        numero = r(0, 255)
        lista.append(numero)
    return lista


def encontrarPares(listaAzar):      # busca los numeros pares en la lista creada o la lista vacia
    contador = 0
    for numero in listaAzar:
        if numero % 2 == 0:
            contador += 1
    return contador


def main():
    listaAzar = []
    eleccion = int(input('Bienvenido/a %s\n'
                         '1. Generar lista aleatoria\n'
                         '2. Contar Pares\n'
                         '3. Salir\n'
                         'Cual es tu eleccion? '% user))            # menu de seleccion de funciones
    while eleccion != 3:            # mientras la eleccion no sea 3
        if eleccion == 1:
            n = int(input('Teclea la longitud de la lista: '))
            listaAzar = generarLista(n)
            print('Se genera esta lista: ', listaAzar)
        elif eleccion == 2:
            #n = int(input('Teclea la longitud de la lista: '))
            #listaAzar = generarLista(n)
            pares = encontrarPares(listaAzar)
            print(pares)
        else:
            print('ERROR! Elije un numero correcto.')
        eleccion = int(input('Bienvenido/a %s\n'
                             '1. Generar lista aleatoria\n'
                             '2. Contar Pares\n'
                             '3. Salir\n'
                             'Cual es tu eleccion? '% user))
    print('Adios %s'% user)

main()