"""
PARCIAL 1 Computacion Grafica Grupo 1
Universidad Tecnologica de Pereira
2018-I
PUNTO A
NUMERAL 1:
En el plano cartesiano capturar dos puntos, luego construir un triangulo con estos puntos y el origen, mostrar el perimetro
del triangulo
"""
import pygame
from pygame.locals import* 
from transformaciones_lineales import* 
from Dibujos import dibujarTriangulo
from matrices import*

ANCHO = 600
ALTO = 480

if __name__ == "__main__":
    cont = 0
    listaPos = []
    origen = [ANCHO/2,ALTO/2]
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    dibujarPlano(pantalla,ANCHO,ALTO)
    pygame.display.flip()
    fin = False
    flag = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                if cont<3:
                    listaPos.append(list(pygame.mouse.get_pos()))
        if cont==2:
            pantalla.fill(NEGRO)
            dibujarPlano(pantalla,ANCHO,ALTO)
            listaPos.append(origen)
            dibujarTriangulo(pantalla,listaPos[0],listaPos[1],listaPos[2])
            pygame.display.flip()
            if not flag:
                print listaPos
                print perimetroTriangulo(listaPos)
                flag = True

