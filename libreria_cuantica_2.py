import math
def conjugadoComplejo(a):
    return (a[0],a[1]*-1)

def Restacomplejos(a,b):
    return (a[0]-b[0], a[1]-b[1])

def sumaComplejos(a,b):
    return (a[0]+b[0],a[1]+b[1])

def multiComplejos(a,b):
    real =(a[0]* b[0])-(a[1]* b[1])
    imaginaria = (a[0]* b[1])+(a[1]* b[0])
    return (real,imaginaria)

def suma_vectores(vec1,vec2):
    vectorSuma = [[[0,0] for j in range(1)]for i in range(len(vec1))]
    for i in range(len(vec1)):
        for j in range(1):
            vectorSuma[i][j][0] = vec1[i][0] + vec2 [i][0]
            vectorSuma[i][j][1] = vec1[i][1] + vec2 [i][1]
    return vectorSuma

def inverso_aditivo(vec1):
    vectorAdicion = [[[0,0] for j in range(1)]for i in range(len(vec1))]
    for i in range(len(vec1)):
        for j in range(1):
            vectorAdicion[i][j][0] = vec1[i][0] * -1
            vectorAdicion[i][j][1] = vec1[i][1] * -1
    return vectorAdicion

def multi_escalar_vector(vec1,escalar):
    vectorResultado = [[[0,0] for j in range(1)]for i in range(len(vec1))]
    for i in range(len(vec1)):
        for j in range(1):
            var = multiComplejos(vec1[i],escalar)
            vectorResultado[i][j][0] = var[0] 
            vectorResultado[i][j][1] = var[1]
    return vectorResultado

def suma_matrices(matriz1,matriz2):
    matriz_adicion = [[[0,0] for j in range(len(matriz1))]for i in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            var = sumaComplejos(matriz1[i][j],matriz2[i][j])
            matriz_adicion[i][j][0] = var[0]
            matriz_adicion[i][j][1] = var[1]
    return matriz_adicion

def inversa_aditiva_matriz(matriz1):
    matriz_inversa = [[[0,0] for j in range(len(matriz1))]for i in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            matriz_inversa[i][j][0] = matriz1[i][j][0] * -1
            matriz_inversa[i][j][1] = matriz1[i][j][1] * -1
    return matriz_inversa

def multi_escalar_matriz(matriz1,escalar):
    matriz = [[[0,0] for j in range(len(matriz1))]for i in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            var = multiComplejos(matriz1[i][j],escalar)
            matriz[i][j][0] = var[0]
            matriz[i][j][1] = var[1]
    return matriz

def transpuesta_matriz(matriz1):
    matriz = [[[0,0] for j in range(len(matriz1))]for i in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            if i == j:
                matriz[i][j] = matriz1[i][j]
            else:
                matriz[i][j] = matriz1[j][i]
    return matriz

def conjugada_matriz(matriz1):
    matriz = [[[0,0] for j in range(len(matriz1))]for i in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            var = conjugadoComplejo(matriz1[i][j])
            matriz[i][j] = var
    return matriz

def conjugada_vector(vec1):
    vector = [[[0,0] for j in range(1)]for i in range(len(vec1))]
    for i in range(len(vec1)):
        for j in range(1):
            var = conjugadoComplejo(vec1[i])
            vector[i][j] = var
    return vector

def matriz_transpuesta_conjugada(matriz1):
    var1 = transpuesta_matriz(matriz1)
    var2 = conjugada_matriz(var1)
    return var2

def multi_matrices(matriz1,matriz2):
    matriz = [[[0,0] for j in range(len(matriz1))]for i in range(len(matriz1))]
    for i in range(len(matriz1)):
        for j in range(len(matriz1)):
            for k in range(len(matriz1[0])):
                var = multiComplejos(matriz1[i][k],matriz2[k][j])
                suma = sumaComplejos(matriz[i][j],var)
                matriz[i][j] = suma
    return matriz



def accion_matriz_vector(matriz1,vector1):
    vector = [[(0,0) for j in range(1)] for i in range(len(vector1))]
    for i in range (len(vector1)):
        for j in range(len(vector1)):
                var = multiComplejos(matriz1[i][j],vector1[j])
                suma = sumaComplejos(vector[i][0],var)
                vector[i][0] = suma
                
    return vector



def producto_Interno(vect1,vect2):
    vector = [(0,0)]
    for i in range(len(vect1)):
        var = multiComplejos(vect1[i],vect2[i])
        suma = sumaComplejos(var,vector[0])
        vector[0] = suma
    return vector









def matriz_Unitaria(m1,m2):
    bandera = True
    m1 = transpuesta_matriz(m1)
    m1 = conjugada_matriz(m1,1)
    unitaria = multi_matrices(m1,m2)
    lista = []
    lista2 = []
    for i in range(len(unitaria)):
        for j in range(len(unitaria)):
            if i == j:
                lista.append(unitaria[i][j])
            else:
                lista2.append(unitaria[i][j])
    for i in range(len(lista)-1):
        if lista[i] == lista[i+1] and lista[i] == [1,0] and lista[i+1] == [1,0] :
            bandera
        else:
            bandera = False
    for i in range(len(lista2)-1):
        if lista2[i] == lista2[i+1] and lista2[i] == [0,0] and lista2[i+1] ==[0,0]:
            bandera
        else:
            bandera = False
            break
    
    return unitaria,bandera

def matriz_Hermitiana(m1,m2):
    bandera = True
    m1 = transpuesta_matriz(m1)
    m2 = conjugada_matriz(m2,1)
    for i in range(len(m1)):
        for j in range(len(m2)):
            if m1[i][j][0] == m2[i][j][0] and m1[i][j][1] == m2[i][j][1]:
                bandera
            else:
                bandera = False
    return(bandera)






def ditancia_Vectores(v1,v2):
    resta = []
    vector = []
    cont = [0,0]
    for i in range(len(v1)):
        for j in range(1):
            x = restaComplejos(v1[i],v2[i])
            resta.append(x)
    v3 = list(conjugada_matriz(resta,2))
    for i in range(len(v1)):
        for j in range(len(v1)):
            primera = multiComplejos(v3[j][i],resta[j])
            vector.append(primera)
        break
    for i in range(len(vector)):
        cont = sumaComplejos(cont,vector[i])
    return cont

def producto_Tensor(v1,v2,parametro):
    if parametro == 1:
        tensor = []
        for i in range(len(v1)):
            for j in range(len(v1)):
                for m in range(len(v2)):
                    x = multiComplejos(v1[j],v2[m])
                    tensor.append(x)
            break
        return tensor
    else:
        tensor = []
        for i in range(len(v1)):
            for j in range(len(v1)):
                for m in range(len(v2)):
                    for n in range(len(v2)):
                        x = multiComplejos(v1[i][m],v2[j][n])
                        y = [0,0]
                        y[0] = round(x[0],1)
                        y[1] = round(x[1],1)
                        tensor.append(y)
        return tensor

def vector_norma(v1): 
    if len(v1) == 0:
        print("No se puede ralizar la operación.")
    else:
        v2 = list(v1)
        v1 = conjugada_matriz(v1,2)
        productoInterno = producto_Interno(v1,v2)
        productoInterno = (productoInterno[0]+productoInterno[1]) ** (1/2)
        productoInterno = round(productoInterno,2)
        return productoInterno
    
            
    
    
    
    
    
    
    
    


            
    

    

def main():
    """vector1 = [(1,3)]
    vector2 = [(2,6)]
    escalar = [1,2]
    matriz1 = [[(1/math.sqrt(2),0),(1/math.sqrt(2),0)],[(1/math.sqrt(2),0),(-1/math.sqrt(2),0)]]
    matriz2 = [[(1,1),(1,1)],[(1,8),(1,5)]]
    a = suma_vectores(vector1,vector2)
    b = inverso_aditivo(vector1)
    c = multi_escalar_vector(vector1,escalar)
    d = suma_matrices(matriz1,matriz2)
    e = inversa_aditiva_matriz(matriz2)
    f = multi_escalar_matriz(matriz1,escalar)
    g = transpuesta_matriz(matriz1)
    h = conjugada_matriz(matriz1)
    i = conjugada_vector(vector1)
    j = matriz_transpuesta_conjugada(matriz1)
    h = multi_matrices(matriz1,matriz2)
    r = matriz_sobre_Vector(matriz2,vector1)
    t = producto_Interno(vector1,vector2)
    w = matriz_Unitaria(matriz1,matriz1)
    ñ = matriz_Hermitiana(matriz1,matriz1)
    ll = accion_matriz_vector(matriz2,vector1)
    sñs = ditancia_Vectores(vector1,vector2)"""
    
    
    
    
main()
