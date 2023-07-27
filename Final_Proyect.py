import numpy as np

def gauss_jordan(matriz_a, matriz_b):
    # Concatena la matriz A y la matriz B
    matriz_extendida = np.concatenate((matriz_a, matriz_b), axis=1)

    # Aplicar eliminación hacia adelante
    filas, columnas = matriz_extendida.shape
    for i in range(filas):
        pivot = matriz_extendida[i][i]
        print(f"\nPaso {i+1}: Dividir la fila {i+1} por el pivote {pivot}")
        print(matriz_extendida)
        matriz_extendida[i] /= pivot
        for j in range(filas):
            if j != i:
                factor = matriz_extendida[j][i]
                print(f"\nPaso {i+1}: Restar {factor} veces la fila {i+1} de la fila {j+1}")
                matriz_extendida[j] -= factor * matriz_extendida[i]
                print(matriz_extendida)

    # Obtiene la solución
    solucion = matriz_extendida[:, -1].reshape(-1, 1)
    return solucion

cantidad_matrices = 1
matrices_a = []
matrices_b = []

for i in range(cantidad_matrices):
    print(f"\nSISTEMA DE ECUACIONES")
    filas = int(input("Ingrese la cantidad de ecuaciones: "))
    columnas = filas + 1  # El tamaño de la matriz aumenta debido a la columna de términos independientes
    matriz_a = np.zeros((filas, filas))
    matriz_b = np.zeros((filas, 1))

    # Obtiene los elementos de la matriz A (Incógnitas)
    print("Ingrese los elementos de la matriz A (Las incógnitas), ej: X, Y, Z ... :")
    for j in range(filas):
        for k in range(filas):
            matriz_a[j][k] = float(input(f"Ingrese la incógnita [{j}][{k}]: "))

    # Obtiene los elementos de la matriz B (Soluciones)
    print("Ingrese los elementos de la matriz B (Las soluciones de las ecuaciones), \n ej: solución de la primer ecuación, luego la de la segunda ... :")
    for j in range(filas):
        matriz_b[j][0] = float(input(f"Ingrese las soluciones [{j}][0]: "))

    matrices_a.append(matriz_a)
    matrices_b.append(matriz_b)

# Resuelve los sistemas de ecuaciones y muestra las soluciones
for i in range(cantidad_matrices):
    print(f"\nSistema de Ecuaciones {i + 1}:")
    solucion = gauss_jordan(matrices_a[i], matrices_b[i])
    print(f"\nValores (El valor de la primera incógnita es el de más arriba y a partir de ese va desde arriba hacia abajo)\nX\nY\n...\n{solucion}")
