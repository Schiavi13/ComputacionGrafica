"""
PARCIAL 1 Computacion Grafica Grupo 1
Universidad Tecnologica de Pereira
2018-I
PUNTO B
NUMERAL 1:
Capturar dos puntos con el raton y dibujar dos lineas que partan desde los puntos hasta la posicion actual del raton
"""
import pygame
from pygame.locals import*
from transformaciones_lineales import*

ANCHO = 600
ALTO = 480

if __name__=="__main__":
    cont = 0
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cont == 0:
                    pos1 = list(pygame.mouse.get_pos())                   
                if cont == 1:
                    pos2 = list(pygame.mouse.get_pos())                  
                cont+=1   
        if cont>1:
            pos3 = list(pygame.mouse.get_pos())
            pantalla.fill(NEGRO)
            pygame.draw.line(pantalla,VERDE,pos1,pos3)
            pygame.draw.line(pantalla,BLANCO,pos2,pos3)
            pygame.display.flip()
