from pygame import*
from transformaciones_lineales import*
from dibujos import*
import random


ANCHO = 600
ALTO = 480

if __name__ == "__main__":
    cont = 0
    random.seed(a=None)
    Triangulo = []
    TrianguloAux = []
    pfijo = []
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    dibujarPlano(pantalla,ANCHO,ALTO)
    origen = [ANCHO/2,ALTO/2]
    pygame.display.flip()
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if cont < 3:
                    Triangulo.append(list(pygame.mouse.get_pos()))
                    TrianguloAux.append(list(pygame.mouse.get_pos()))
                cont+=1         
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if cont >=3:
                        for i in range(0,len(TrianguloAux)):
                            TrianguloAux[i] = calcularPuntoPlano(Triangulo[i],origen)
                        sub = random.randint(0,2)
                        pfijo = TrianguloAux[sub]
                        for i in range(0,len(Triangulo)):
                            Triangulo[i] = calcularPuntoPlano(Triangulo[i],origen)
                            Triangulo[i] = trasladarPuntoNeg(Triangulo[i],pfijo)
                            Triangulo[i] = escalarPunto(Triangulo[i],2)
                            Triangulo[i] = trasladarPunto(Triangulo[i],pfijo)
                            Triangulo[i] = calcularPuntoPantalla(Triangulo[i],origen)
        if cont>=3:
            pantalla.fill(NEGRO)
            dibujarPlano(pantalla,ANCHO,ALTO)
            pygame.draw.polygon(pantalla,VERDE,Triangulo,1)
            pygame.display.flip()
