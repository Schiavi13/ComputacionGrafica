from pygame import*
from transformaciones_lineales import*

ANCHO = 600
ALTO = 480


if __name__ == "__main__":
    listaPuntosPol = []
    listaPuntosCar = []
    listaPuntosPantalla = []
    r = 200
    origen = [ANCHO/2,ALTO/2]
    angulo = 0
    nv = input("Ingrese numero de vertices: ")
    incremento = 360/nv
    for i in range(nv):
        angulo = angulo + incremento
        listaPuntosPol.append([r,angulo])
        print angulo
    print listaPuntosPol

    for i in range(nv):
        punto = polaresCart(r,listaPuntosPol[i][1])
        print punto
        listaPuntosCar.append(punto)
    print listaPuntosCar
    
    for i in range(nv):
        punto = calcularPuntoPantalla(listaPuntosCar[i],origen)
        listaPuntosPantalla.append(punto)
    
    pygame.init()
    reloj = pygame.time.Clock()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    dibujarPlano(pantalla,ANCHO,ALTO)
    pygame.display.flip()
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    pygame.draw.circle(pantalla,BLANCO,origen,r,1)
                    pygame.draw.polygon(pantalla,ROJO,listaPuntosPantalla)
        pygame.display.flip()
        reloj.tick(50)