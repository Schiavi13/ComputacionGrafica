from pygame import*
from transformaciones_lineales import*

ANCHO = 600
ALTO = 480

#cardioide r = a(1+cos(theta))
#rosa polar r = a(cos(K*theta))  k impar = k petalos, k par = 2k petalos
if __name__ == "__main__":
    
    origen = [ANCHO/2,ALTO/2]
    theta = 0
    a = 100
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
        r = a*(1-math.cos(math.radians(theta)))
        punto_cart = polaresCart(r,theta)
        punto_pantalla = calcularPuntoPantalla(punto_cart,origen)
        pygame.draw.circle(pantalla,ROJO,punto_pantalla,1,1)
        theta += 0.5       
        pygame.display.flip()
        reloj.tick(50)