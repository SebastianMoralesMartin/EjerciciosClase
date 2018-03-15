# encoding: UTF-8
# Sebastian Morales Martín
# Ejercicio_18: Tortuga toad
# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame
from random import randint as ran
ANCHO = 800
ALTO = 525
    # Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)

def mostrarGanador(ventana, ganador):
    fuente = pygame.font.SysFont('monospace', 60)
    animal = 'luigi'
    if ganador == 1:
        animal = 'Toad'
    elif ganador == 2:
        animal = 'Mario'
    texto = fuente.render('Ganó ' + animal + '!!!', 1, NEGRO)
    ventana.blit(texto, (ANCHO//4, ALTO//3))

def moverImagenes(x):
    x += ran(1, 5)
    return x
# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Dimensiones de la pantalla


    # Inicializa el motor de pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))    # Crea la ventana de dibujo
    reloj = pygame.time.Clock()     # Para limitar los fps
    termina = False                 # Bandera para saber si termina la ejecución

    #Crear la imagen
    castle = pygame.image.load('castle.jpg')
    toad = pygame.image.load('toad.png')
    mario = pygame.image.load('Mario.png')
    luigi = pygame.image.load('luigi.png')
    road = pygame.image.load('road.jpg')
    xConejo = 0
    xTortuga = 0
    xLiebre = 0
    xRoad = 0
    hayGanador = False
    ganador = 0


    while not termina:              # Ciclo principal
        # Procesa los eventos que recibe el programa
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        #ventana.blit(castle, (0, 0))
        ventana.blit(road, (xRoad, 0))
        ventana.blit(road, (ANCHO + xRoad, 0))
        ventana.blit(toad, (xTortuga, ALTO//2))
        ventana.blit(mario, (xLiebre, ALTO// 3))
        ventana.blit(luigi, (xConejo, (ALTO//3)*2))
        pygame.display.set_caption('Carrera.py')
        if not hayGanador:
            xRoad -= 20

        if xRoad == -ANCHO:
            xRoad = 0
        if xTortuga < ANCHO-64:
            if not hayGanador:
                xTortuga = moverImagenes(xTortuga)
        else:
            hayGanador = True
            ganador = 1
            pygame.display.set_caption('GANO TOAD!!!')
        if xLiebre < ANCHO-64:
            if not hayGanador:
                xLiebre = moverImagenes(xLiebre)

        else:
            hayGanador = True
            ganador = 2
            pygame.display.set_caption('GANO MARIO!!!')

        if xConejo < ANCHO-64:
            if not hayGanador:
                xConejo = moverImagenes(xConejo)
        else:
            hayGanador = True
            ganador = 3
            pygame.display.set_caption('GANO LUIGI!!!')
        if hayGanador:
            mostrarGanador(ventana, ganador)


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps


    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    dibujar()


main()