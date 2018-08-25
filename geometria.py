import math
from matrices import*

def perimetroTriangulo(puntos):
    perimetro = 0
    resultante = vectorResultante(puntos[0],puntos[1])
    perimetro = perimetro + normaVector(resultante)
    resultante = vectorResultante(puntos[1],puntos[2])
    perimetro = perimetro + normaVector(resultante)
    resultante = vectorResultante(puntos[2],puntos[0])
    perimetro = perimetro + normaVector(resultante)
    return perimetro
