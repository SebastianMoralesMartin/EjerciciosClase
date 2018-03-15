# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla
import pygame
import math
from random import randint




ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO= (0,0,0)
def dibujarEsquinas(ventana, numero):
    listaCoordenadas = []
    radio = 400
    for angulo in range(0, 360, 360//numero):       # calcula las esquinas del circulo y las dibuja
        #angulo = angulo -1
        a = math.radians(angulo)
        x = int(radio * math.cos(a))
        y = int(radio * math.sin(a))
        #pygame.draw.circle(ventana, NEGRO, (x + ANCHO // 2, ALTO // 2 - y), 10)
        coordenada = (x + ANCHO // 2,ALTO // 2 - y)
        listaCoordenadas.append(coordenada)
    for numero in listaCoordenadas:                 # for anidado en donde por cada coordenada del circulo, dibuja lineas para los demas segmentos
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        for valor in listaCoordenadas:
            pygame.draw.line(ventana, ROJO, (numero),(valor), 1)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(esquinas):
    # Dimensiones de la pantalla


    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(NEGRO)

        # Dibujar, aquí haces todos los trazos que requieras

        pygame.draw.circle(ventana, BLANCO, (ANCHO//2, ALTO//2), 400, 1)

        dibujarEsquinas(ventana, esquinas)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(1)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    esquinas = int(input('Cantidad de Esquinas: '))
    while esquinas != 1:
        dibujar(esquinas)
        esquinas = int(input('Cantidad de Esquinas: '))



main()