
#suma = [x[:] for x in matriz1]
#Recibe una lista de listas de numeros (matriz) y un numero n y retorna la columna numero n de la matriz
import math
def columna(matriz,n):  
    if (n>=0):
        lista =[]
        for i in range(0,len(matriz)):
            if (n<=len(matriz[i])):
                lista.append(matriz[i][n-1])
            else:
                return "Sobrepasa la dimension de la matriz"
        return lista
    else:
        return "La dimension debe ser positiva"

#Recibe un numero n y retorna una matriz identidad de dimension nxn
def matrizIdentidad(n):
    matriz = [[0 for x in range (n)] for y in range (n)] #inicializa la matriz con solo 0
    for i in range(0,n):
        matriz[i][i] = 1
    return matriz

#Recibe dos listas de listas de numeros (matrices) y retorna el producto punto entre dos matrices nxm . mxn
def productoPunto(matriz1,matriz2):
    sum = 0
    for i in range(0,len(matriz1)): #verifica que m1 = nxm y m2 = mxn
        if((len(matriz1[i]) == len(matriz2)) and (len(matriz1) == len(matriz2[i]))):
            for j in range(0,len(matriz1)):
                sum = sum + (matriz1[i][j]*matriz2[j][i])
        else:
            return "El numero de filas de la primer matriz debe ser igual al numero de columnas de la segunda matriz y viceversa"
    return sum

#Recibe una lista de listas de numeros (matriz) y retorna una matriz con todos los valores en 0 de la misma dimension que matriz1
def crearMatrizVacia(matriz1):
    suma = [x[:] for x in matriz1]
    return suma

#Recibe dos listas de listas de numeros (matrices) y retorna un booleano: True si tienen la misma cantidad de filas y False si es el
#caso contrario
def igualdadFilas(matriz1,matriz2): 
    if (len(matriz1)==len(matriz2)): 
        return True
    else:
        return False

#Recibe una lista de listas de numeros (matriz) y retorna cada una de las filas de la matriz por separado
def crearFila(matriz):  
    sublista = []
    for j in range (0,len(matriz)):
        sublista.append(matriz[j])
    return sublista

#Recibe dos listas de listas de numeros (matrices) y retorna la suma de las dos matrices
def sumarMatrices(matriz1,matriz2):
    suma = crearMatrizVacia(matriz1)
    if(igualdadFilas(matriz1,matriz2)): #evalua si tienen mismo numero de columnas
        filaMatriz1 = []    #listas que se llenaran temporalmente con 1 fila de la matriz correspondiente
        filaMatriz2 = []
        for i in range (0,len(matriz1)):
            filaMatriz1 = crearFila(matriz1[i]) #asigna las filas
            filaMatriz2 = crearFila(matriz2[i])
            if(igualdadFilas(filaMatriz1,filaMatriz2)): #evalua si las matrices tienen el mismo
                for j in range (0,len(filaMatriz1)):    #numero de columnas
                    suma[i][j] = filaMatriz1[j] + filaMatriz2[j]
            else:
                return "Ambas matrices deben tener el mismo numero de columnas"
        return suma
    else:
        return "Ambas matrices deben tener el mismo numero de filas"

#Recibe una lista de numeros (vector) y retorna la norma del vector
def normaVector(vector):
    sum = 0
    for i in range(0,len(vector)):
        sum = sum + math.pow(vector[i],2)
    return math.sqrt(sum)

#Recibe dos listas de numeros (vectores) y retorna un booleano: True si tienen la misma dimension y False en el caso contrario
def igualdadDimensionVector(vector1,vector2):
    if len(vector1) == len(vector2):
        return True
    else:
        return False

#Recibe dos listas de numeros (vectores) y retorna el vector resultante entre los vectores
def vectorResultante(vector1,vector2):
    resultante = []
    if igualdadDimensionVector(vector1,vector2):
        for i in range(0,len(vector1)):
            resultante.append(vector2[i]-vector1[i])
        return resultante

#Recibe dos vectores [x,y,...,n] y retorna el producto punto entre ambos
def productoPuntoVectores(vector1,vector2):
    if len(vector1) == len(vector2):
        sum = 0
        for i in range(0,len(vector1)):
            sum = sum + vector1[i]*vector2[i]
        return sum
        

#Recibe una lista de 3 puntos [x,y] y retorna el perimetro del triangulo formado por la union de los puntos
def perimetroTriangulo(puntos):
    perimetro = 0
    resultante = vectorResultante(puntos[0],puntos[1])
    perimetro = perimetro + normaVector(resultante)
    resultante = vectorResultante(puntos[1],puntos[2])
    perimetro = perimetro + normaVector(resultante)
    resultante = vectorResultante(puntos[2],puntos[0])
    perimetro = perimetro + normaVector(resultante)
    return perimetro

#Recibe dos listas [x,y,...,n] de igual dimension y retorna el angulo formado por los vectores que representan
def anguloVectores(vector1,vector2):
    if len(vector1) == len(vector2):
        return math.degrees(math.acos((productoPuntoVectores(vector1,vector2)/(normaVector(vector1)*normaVector(vector2)))))

#Recibe dos numeros que representan los catetos de un triangulo rectangulo y retorna la hipotenusa
def calcularHipotenusa(c_ad,c_op):
    return math.sqrt(math.pow(c_ad,2)+math.pow(c_op,2))

#Recibe dos numeros que representan los catetos de un triangulo rectangulo y retorna los angulos internos del triangulo
def calcularAngulosTRect(c_ad,c_op):
    angulos = [90]
    hipotenusa = calcularHipotenusa(c_ad,c_op)
    angulos.append(round(math.degrees(math.asin(c_op/hipotenusa)),2))
    angulos.append(round(math.degrees(math.asin(c_ad/hipotenusa)),2))
    return angulos

