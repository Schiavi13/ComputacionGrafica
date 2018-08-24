"""
PARCIAL 1 Computacion Grafica Grupo 1
Universidad Tecnológica de Pereira
2018-I
PUNTO B
NUMERAL 2:
Dibujar un plano cartesiano, capturar dos puntos con el mouse(solamente en el primer cuadrante), dibujar una linea entre los
puntos, al pulsar la tecla "ESPACIO" desplazarla al cuarto cuadrante
"""
import pygame, math
from pygame import*
from transformaciones_lineales import dibujarPlano

ANCHO=600
ALTO=480

if __name__=="__main__":
    cont = 0
    origen = [ANCHO/2,ALTO/2]
    punto1 = [0,0]
    punto2 = [0,0]
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    dibujarPlano(pantalla)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cont == 0:
                    pos1 = list(pygame.mouse.get_pos())
                    punto1 = [origen[0]+pos1[0],origen[1]-pos1[1]]
                if cont == 1:
                    pos2 = list(pygame.mouse.get_pos())
                    punto2 = [origen[0]+pos2[0],origen[1]-pos2[1]]              
                cont+=1 
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    punto1 = [pos1[0],origen[1]+pos1[1]]
                    punto2 = [pos2[0],origen[1]+pos2[1]]
                cont+=1
        if cont==2:
            pantalla.fill(NEGRO)
            dibujarPlano(pantalla)
            pygame.draw.line(pantalla,VERDE,pos1,pos2)
            pygame.display.flip()
        if cont>2:
            pantalla.fill(NEGRO)
            dibujarPlano(pantalla)
            pygame.draw.line(pantalla,VERDE,punto1,punto2)
            pygame.display.flip()
