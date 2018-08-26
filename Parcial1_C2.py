"""
PARCIAL 1 Computacion Grafica Grupo 1
Universidad Tecnologica de Pereira
2018-I
PUNTO C
NUMERAL 2:
Capturar un punto en el plano cartesiano, crear una linea desde el origen hasta el punto, mostrar en la terminal a cuantos
grados se levanta la recta respecto al eje x+
"""

from pygame import*
from geometria import*
from matrices import*
from transformaciones_lineales import*

ANCHO = 600
ALTO = 480

if __name__ == "__main__":
    cont = 0
    punto = []
    origen = [ANCHO/2,ALTO/2]
    unitarioX = [1,0]
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
                if cont<1:
                    punto = list(pygame.mouse.get_pos())
                cont+=1
        if cont>0 and flag==False:
            pantalla.fill(NEGRO)
            dibujarPlano(pantalla,ANCHO,ALTO)
            pygame.draw.line(pantalla,BLANCO,origen,punto)
            pygame.display.flip()
            punto = calcularPuntoPlano(punto,origen)           
            print anguloVectores(unitarioX,vectorResultante([0,0],punto))
            flag=True
