def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = input(f"Ingrese primero: La incognita ´X´ luego ´Y´, luego ´Z´ y por ultimo la solucion, y repita ese proceso [{i}][{j}]: ")
            fila.append(elemento)
        matriz.append(fila)
    return matriz

cantidad_matrices = 1
matrices = []

for i in range(cantidad_matrices):
    print(f"\nMatriz {i + 1}")
    filas = int(input("Ingrese la cantidad de incognitas que tendra su sistema"))
    columnas = 4
    matriz = crear_matriz(filas, columnas)
    matrices.append(matriz)

# Imprime las matrices creadas
for i, matriz in enumerate(matrices):
    print(f"\nMatriz {i + 1}:")
    for fila in matriz:
        print(fila)