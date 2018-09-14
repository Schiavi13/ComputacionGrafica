import math, pygame
#constantes para los colores
VERDE = [0,255,0]
ROJO = [255,0,0]
AZUL = [0,0,255]
NEGRO = [0,0,0]
BLANCO = [255,255,255]

#Traslada un punto
def trasladarPunto(punto,tras):
    x=int(punto[0])+int(tras[0])
    y=int(punto[1])+int(tras[1])
    return [x,y]

#escala un punto una proporcion dada
def escalarPunto(punto,proporcion):
    x=int((punto[0])*proporcion)
    y=int(punto[1]*proporcion)
    return [x,y]

#Dibuja un plano cartesiano con origen en el medio de la pantalla
def dibujarPlano(pantalla,ANCHO,ALTO):
    pygame.draw.line(pantalla,VERDE,[0,ALTO/2],[ANCHO,ALTO/2])
    pygame.draw.line(pantalla,VERDE,[ANCHO/2,0],[ANCHO/2,ALTO])

#Rota un punto un angulo theta dado en sentido horario
def rotarPuntoCW(punto,theta):
    theta = math.radians(theta)
    x = int(round((math.cos(theta)*punto[0])-(math.sin(theta)*punto[1])))
    y = int(round((math.sin(theta)*punto[0])+(math.cos(theta)*punto[1])))
    return [x,y]

#Rota un punto un angulo dado en sentido antihorario
def rotarPuntoACW(punto,theta):
    theta = math.radians(theta)
    x = int(round((math.cos(theta)*punto[0])+(math.sin(theta)*punto[1])))
    y = int(round((math.sin(theta)*(-punto[0]))+(math.cos(theta)*punto[1])))
    return [x,y]

#Calcula el punto en el plano cartesiano al que correspone una posicion de pantalla
def calcularPuntoPlano(punto,origen):
    x = punto[0]-origen[0]
    y = origen[1]-punto[1]
    return [x,y]

#Calcula el punto en la pantalla al que corresponde una posicion en el plano cartesiano
def calcularPuntoPantalla(punto,origen):
    x = punto[0] + origen[0]
    y = origen[1] - punto[1]
    return [x,y]

#Pasa de coordenadas cartesianas a coordenadas polares
def cartPolares(punto):
    r = math.sqrt((punto[0]**2)+(punto[1]**2))
    theta = math.degrees(math.acos(p[0]/r))
    return [r,theta]

#Pasa de coordenadas polares a coordenadas cartesianas
def polaresCart(r,theta):
    x = int(r*(math.cos(math.radians(theta))))
    y = int(r*(math.sin(math.radians(theta))))
    return [x,y]
