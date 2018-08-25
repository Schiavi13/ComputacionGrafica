import math, pygame

VERDE = [0,255,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
NEGRO = [0,0,0]
BLANCO = [255,255,255]

def dibujarTriangulo(pantalla,punto1,punto2,punto3):
    pygame.draw.line(pantalla,VERDE,punto1,punto2)
    pygame.draw.line(pantalla,VERDE,punto2,punto3)
    pygame.draw.line(pantalla,VERDE,punto3,punto1)