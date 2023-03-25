import libvecspaces as lvs
import salto_clasico_cuantico as scc
import numpy as np
import math

def modulo_cua(c):
    return c.real**2+c.imag**2

def normal(v):
    b = 0
    for i in range(len(v)):
        b += modulo_cua(v[i])
    b = math.sqrt(b.real)
    return b
def normalizar(v):
    norma = normal(v)
    for i in range(len(v)):
        v[i] = v[i]*(1/norma)
    return v

def probabilidad(vector,pos):
    if pos < len(vector):
        if normal(vector)!= 1:
            vector = normalizar(vector)
        xj_2 = modulo_cua(vector[pos])
        y = 0
        for i in range(len(vector)):
            y += modulo_cua(vector[i])
        return xj_2/y
    else:
        return "Posicion excede el limite del vector"

def transicion(v1,v2):
    b = lvs.producintern(v2,v1)
    b = b/(normal(v1)*normal(v2))
    prob = modulo_cua(b)
    return prob

def media(matrix,ket):
    if normal(ket) != 1:
        ket = normalizar(ket)
    resp = lvs.hermitiana(matrix)
    if resp == "La matriz NO es hermitiana" or resp == "Error, tamaño de matriz incorrecto":
        return resp
    else:
        la_media = lvs.producintern(lvs.accionmsobrev(matrix,ket),ket)
        return la_media.real
def varianza(matrix,ket):
    if normal(ket) != 1:
        ket = normalizar(ket)
    resp = lvs.hermitiana(matrix)
    if resp == "La matriz NO es hermitiana" or resp == "Error, tamaño de matriz incorrecto":
        return resp
    else:
        matrix_identidad = [[0 for i in range(len(matrix))]for j in range(len(matrix))]
        for i in range(len(matrix_identidad)):
            for j in range(len(matrix_identidad)):
                if i == j:
                    matrix_identidad[i][j] = 1
        operador = lvs.multescma(media(matrix,ket),lvs.invma(matrix_identidad))
        delta = lvs.summa(matrix,operador)
        delta_cuadrado = lvs.productoma(delta,delta)
        var = media(delta_cuadrado,ket)
        return var

def valores_propios(matrix):
    matrix = np.array(matrix)
    valores = np.linalg.eigvals(matrix)
    return valores
def vectores_propios(matrix):
    matrix = np.array(matrix)
    valores, vectores = np.linalg.eig(matrix)
    return vectores

def transitar_a_vectores_propios(matrix,ket):
    if normal(ket) != 1:
        ket = normalizar(ket)
    vectores = vectores_propios(matrix)
    prob = []
    for i in range(len(vectores)):
        proba = transicion(ket,vectores[i])
        prob.append(proba)
    return prob

def finalstate(seq,ket):
    actual_state = ket
    verificador = True
    for i in range(len(seq)):
        unitaria = lvs.unitario(seq[i])
        if unitaria == "La matriz NO es unitaria" or unitaria == "Error, tamaño de matriz incorrecto":
            verificador = False
            break
    if verificador:
        for i in range(len(seq)):
            actual_state = lvs.accionmsobrev(seq[i],actual_state)
        return actual_state
    else:
        return "Alguna de las matrices no son unitarias"


if __name__ == "__main__":
    #print(media([[1,-1j],[1j,2]],[math.sqrt(2)/2,(math.sqrt(2)/2)*1j]))
    # print(varianza([[1,-1j],[1j,2]],[math.sqrt(2)/2,(math.sqrt(2)/2)*1j]))
    # print(probabilidad([-3-1j,-2j,1j,2],2))
    # print(transicion([1,-1j],[1j,1]))
    # print(valores_propios([[1,0],[0,-1]]))
    # print(vectores_propios([[1, 0], [0, -1]]))
    # print(transitar_a_vectores_propios([[-1,-1j],[1j,1]],[1/2,1/2]))
    #print(finalstate([[[(1 + 1j)/2, (1 - 1j)/2], [(1 - 1j)/2, (1 + 1j)/2]],[[1, 0], [0, 1j]]],[1j, 2j]))

    # 4.3.1
    # print(vectores_propios([[0,1],[1,0]]))

    # 4.3.2
    #print(transitar_a_vectores_propios([[0, 1], [1, 0]], [0, 1]))
    # print(valores_propios([[0, 1], [1, 0]]))
    # print(media([[0, 1], [1, 0]], [0, 1]))

    # 4.4.1
    #A =[[0,1],[1,0]]
    #c = (2**(1/2))/2
    #B = [[c,c],[c,-c]]
    #multi = lvs.productoma(A,B)
    #print(lvs.unitario(A))
    #print(lvs.unitario(B))
    #print(lvs.unitario(multi))

    # 4.4.2
    #c = 1/math.sqrt(2)
    #billar = [[0,c,c,0,],[1j*c,0,0,c],[c,0,0,1j*c],[0,c,-c,0]]
    #billar1 = [[0,c,c,0,],[c,0,0,-c],[c,0,0,c],[0,-c,c,0]]
    #state = scc.complejos(billar,[1,0,0,0],3)
    #state1 = scc.calculo(billar1,[1,0,0,0],3)
    #print(state)
    #print(state1)

