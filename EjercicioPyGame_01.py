# encoding: UTF-8
# Sebastian Morales Martin
# EjercicioPyGame_01: circulos

# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Dimensiones de la pantalla
    ANCHO = 800
    ALTO = 800
    # Colores
    NEGRO = (0, 0, 0)
    BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255]
    VERDE_BANDERA = (0, 122, 0)
    ROJO = (255, 0, 0)
    NARANJA = (255, 122, 122)

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
        '''
        pygame.draw.rect(ventana, VERDE_BANDERA, (30, 30, ANCHO-60, ALTO-60), 5)
        pygame.draw.circle(ventana, NARANJA, (ANCHO//2, ALTO//2), 200, 2)
        '''
        for numero in range(30, ANCHO+60, 60):
            for y in range(30, ALTO+60, 60):
                if numero % 2 == 0 and y % 2 == 0:
                    width = 0
                else:
                    width = 2
                pygame.draw.circle(ventana, (222, 0, 255), (numero, y), 30, 1)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(40)          # 40 fps

    # Después del ciclo principal
    pygame.quit()   # termina pygame


def main():
    dibujar()


main()