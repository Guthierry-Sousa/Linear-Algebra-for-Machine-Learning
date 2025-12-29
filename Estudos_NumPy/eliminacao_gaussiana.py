# Algoritmo - Eliminação Gaussiana

import numpy as np

A = np.array([
    [3,-1,-1],
    [-1, -1,-1],
    [2, 0,-3]
])

b = np.array([5,0,2])

try:
    print(f"Solution = {np.linalg.solve(A,b)}")
except:
    print("Sistema Singular")

# Implementação do Algoritmo

def matriz_aumentada(A,b):

    M = np.column_stack((A,b))

    M = M.astype("float")

    return M

def trocar_linhas(A, linha1, linha2):

    A[[linha1,linha2]] = A[[linha2,linha1]]

    return A

def index_linha_elemento_nao_zero(A, linha_index, aumentada = False):

    M = A.copy()

    if aumentada == True:

        M = M[:,:-1]

    linha = M[linha_index]

    for i, v in enumerate(linha):

        if not np.isclose(v, 0):

            return i
        
    return -1

def index_coluna_elemento_nao_zero(A, coluna_index):

    M = A.copy()

    coluna = M[:,coluna_index]

    for i, v in enumerate(coluna):

        if not np.isclose(v, 0):

            return i
        
    return -1

def eliminacao_gaussiana(A,b):

    det = np.linalg.det(A)

    if np.isclose(det,0):

        return "Sistema Singular"
    
    A = A.copy()
    b = b.copy()

    A = A.astype('float64')
    b = b.astype('float64')

    M = matriz_aumentada(A,b)

    n = len(M)

    for i in range(n):

        candidato_pivo = M[i][i]

        if np.isclose(candidato_pivo, 0):

            index_elemento_nao_zero = index_coluna_elemento_nao_zero(M, i)

            M = trocar_linhas(M, i, index_elemento_nao_zero)

            pivo = M[i][i]

        else:

            pivo = candidato_pivo

        M[i] = (1/pivo) * M[i]

        for j in range(i+1, n):

            valor = M[j,i]

            M[j] = M[j] - valor * M[i]

    return M

def eliminacao_de_gauss_jordan(N):

        M = N.copy()

        n = M.shape[0]

        for i in reversed(range(n)):

            linha_pivo = M[i]

            index = index_linha_elemento_nao_zero(M, i, True)

            for j in range(i):

                valor = M[j][index]

                M[j] = M[j] - valor * linha_pivo

        solucao = M[:,-1]

        return M, solucao

matriz_escalonada = eliminacao_gaussiana(A,b)

print(f"\nMatriz escalonada: ")
print(matriz_escalonada)

try:

    matriz_escalonada_reduzida, x = eliminacao_de_gauss_jordan(matriz_escalonada)

except:

    print("O sistema não possui uma única solução")

else:

    print("\nMatriz Escalonada Reduzida: ")
    print(matriz_escalonada_reduzida)

    print(f"\nSolucao do sistema: {x}")










