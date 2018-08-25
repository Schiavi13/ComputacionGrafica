"""
PARCIAL 1 Computacion Grafica Grupo 1
Universidad Tecnologica de Pereira
2018-I
PUNTO C
NUMERAL 1:
Capturar un punto en la pantalla y dibujar un circulo. Con las teclas RIGHT y LEFT aumentar y disminuir el tamano
"""

from pygame import*
from transformaciones_lineales import*

ANCHO = 600
ALTO = 480

if __name__ == "__main__":
    cont = 0
    centro = []
    radio = 1
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                cont+=1
                if cont == 1:
                    centro = list(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:
                if cont>=1:
                    if event.key == pygame.K_RIGHT:
                        radio+=5
                    if event.key == pygame.K_LEFT and radio>=6:
                        radio-=5
        if cont>=1:
            pantalla.fill(NEGRO)
            pygame.draw.circle(pantalla,VERDE,centro,radio,1)
            pygame.display.flip()


