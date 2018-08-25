
#suma = [x[:] for x in matriz1]
#Retorna la columna n de la matriz
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

#Retorna una matriz identidad de dimension nxn
def matrizIdentidad(n):
    matriz = [[0 for x in range (n)] for y in range (n)] #inicializa la matriz con solo 0
    for i in range(0,n):
        matriz[i][i] = 1
    return matriz

#Retorna el producto punto entre dos matrices nxm . mxn
def productoPunto(matriz1,matriz2):
    sum = 0
    for i in range(0,len(matriz1)): #verifica que m1 = nxm y m2 = mxn
        if((len(matriz1[i]) == len(matriz2)) and (len(matriz1) == len(matriz2[i]))):
            for j in range(0,len(matriz1)):
                sum = sum + (matriz1[i][j]*matriz2[j][i])
        else:
            return "El numero de filas de la primer matriz debe ser igual al numero de columnas de la segunda matriz y viceversa"
    return sum

#retorna una matriz con todos los valores en 0 de la misma dimension que matriz1
def crearMatrizVacia(matriz1):
    suma = [x[:] for x in matriz1]
    return suma

#Evalua si dos matrices tienen el mismo numero de filas
def igualdadFilas(matriz1,matriz2): 
    if (len(matriz1)==len(matriz2)): 
        return True
    else:
        return False

#Funcion que crea una lista aparte por cada fila y con cada elemento de la fila de una matriz
def crearFila(matriz):  
    sublista = []
    for j in range (0,len(matriz)):
        sublista.append(matriz[j])
    return sublista

#funcion que suma dos matrices
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

#Retorna la norma de un vector unidimensional
def normaVector(vector):
    sum = 0
    for i in range(0,len(vector)):
        sum = sum + math.pow(vector[i],2)
    return math.sqrt(sum)

#Retorna verdadero si los vectores dados tienen la misma dimension
def igualdadDimensionVector(vector1,vector2):
    if len(vector1) == len(vector2):
        return True
    else:
        return False

#Retorna el vector resultante entre dos vectores
def vectorResultante(vector1,vector2):
    resultante = []
    if igualdadDimensionVector(vector1,vector2):
        for i in range(0,len(vector1)):
            resultante.append(vector2[i]-vector1[i])
        return resultante