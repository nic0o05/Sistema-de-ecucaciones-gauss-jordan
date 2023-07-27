import numpy as np
def gauss_jordan(matriz):
    rows = len(matriz)
    columns = len(matriz[0])

    for i in range(rows):
        # Paso 1: Buscar el pivote máximo en la columna actual
        max_row = i
        for j in range(i + 1, rows):
            if abs(matriz[j][i]) > abs(matriz[max_row][i]):
                max_row = j
                print(matriz)

        # Paso 2: Intercambiar filas si es necesario
        matriz[i], matriz[max_row] = matriz[max_row], matriz[i]
        print(matriz)

        # Paso 3: Convertir el pivote en 1
        pivot = matriz[i][i]
        for j in range(i, columns):
            matriz[i][j] /= pivot
            print(matriz)

        # Paso 4: Convertir otras filas en 0
        for j in range(rows):
            if j != i:
                factor = matriz[j][i]
                for k in range(i, columns):
                    matriz[j][k] -= factor * matriz[i][k]
                    print(matriz)

    return [row[-1] for row in matriz]
    



matriz = [[2, 3, 4, 20],
         [3, -5, -1, -10], 
         [-1, 2, -3, -6]]
solution = gauss_jordan(matriz)
print(solution)
