"""
PARCIAL 1 Computacion Grafica Grupo 1
Universidad Tecnológica de Pereira
2018-I
PUNTO A
NUMERAL 1:
Usando el raton y sus eventos dibujar una cruz, mover la cruz con las teclas(UP,DOWN,RIGHT,LEFT)
"""
import pygame
from pygame.locals import* 
from transformaciones_lineales import*

ANCHO = 600
ALTO = 480

if __name__ == "__main__":
    listaPos = []
    cont = 0
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cont%2 == 0:
                    listaPos.append(list(pygame.mouse.get_pos()))
                else:
                    listaPos.append(list(pygame.mouse.get_pos()))
                cont+=1
            if event.type == pygame.KEYDOWN:
                if event.key == K_DOWN:
                    if cont>1:
                        for i in range(0,len(listaPos)):
                            listaPos[i][1]=listaPos[i][1]+5
                if event.key == K_UP:
                    if cont>1:
                        for i in range(0,len(listaPos)):
                            listaPos[i][1]=listaPos[i][1]-5
                if event.key == K_LEFT:
                    if cont>1:
                        for i in range(0,len(listaPos)):
                            listaPos[i][0]=listaPos[i][0]-5
                if event.key == K_RIGHT:
                    if cont>1:
                        for i in range(0,len(listaPos)):
                            listaPos[i][0]=listaPos[i][0]+5
        if cont>1 and (cont%2==0):
            pantalla.fill(NEGRO)
            for i in range(0,len(listaPos)-1,2):
                pygame.draw.line(pantalla,VERDE,listaPos[i],listaPos[i+1])
            pygame.display.flip()
