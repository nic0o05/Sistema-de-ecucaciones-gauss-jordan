def concatenate_matrices(a, b):
    # Concatenar las matrices a y b
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    
    if rows_a != rows_b:
        raise ValueError("Las matrices deben tener el mismo número de filas.")
    
    result = []
    for i in range(rows_a):
        row = a[i] + b[i]
        result.append(row)
    
    return result

def divide_row(row, divisor):
    # Dividir una fila por un divisor
    return [element / divisor for element in row]

def subtract_rows(row1, row2, factor):
    # Restar un múltiplo de una fila a otra fila
    return [element1 - (factor * element2) for element1, element2 in zip(row1, row2)]

def gauss_jordan(matrix_a, matrix_b):
    # Concatenar la matriz A y la matriz B
    matrix_extended = concatenate_matrices(matrix_a, matrix_b)

    # Aplicar eliminación hacia adelante
    rows, cols = len(matrix_extended), len(matrix_extended[0])
    for i in range(rows):
        pivot = matrix_extended[i][i]
        print(f"\nPaso {i+1}: Dividir la fila {i+1} por el pivote {pivot}")
        print_matrix(matrix_extended)
        matrix_extended[i] = divide_row(matrix_extended[i], pivot)
        for j in range(rows):
            if j != i:
                factor = matrix_extended[j][i]
                print(f"\nPaso {i+1}: Restar {factor} veces la fila {i+1} de la fila {j+1}")
                matrix_extended[j] = subtract_rows(matrix_extended[j], matrix_extended[i], factor)
                print_matrix(matrix_extended)

    # Obtener la solución
    solution = [[row[-1]] for row in matrix_extended]
    return solution

def print_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    variables = []
    for i in range(rows):
        if i < 3:
            variables.append(chr(88 + i))
        elif i == 3:
            variables.append("D")
        else:
            variables.append(chr(97 + i - 4))

    for i in range(rows):
        equation = ''
        for j in range(cols - 1):
            equation += f"{matrix[i][j]:.2f}{variables[j]} + "
        equation += f"{matrix[i][-1]:.2f}"
        print(equation)
    print()

cantidad_matrices = 1
matrices_a = []
matrices_b = []

for _ in range(cantidad_matrices):
    print(f"\nSISTEMA DE ECUACIONES")
    filas = int(input("Ingrese la cantidad de ecuaciones: "))
    columnas = filas + 1  # El tamaño de la matriz aumenta debido a la columna de términos independientes
    matriz_a = []
    matriz_b = []

    # Obtener los elementos de la matriz A (Incógnitas)
    print("Ingrese los elementos de la matriz A (Las incógnitas), ej: X, Y, Z ... :")
    for _ in range(filas):
        row = []
        for _ in range(filas):
            element = float(input("Ingrese la incógnita: "))
            row.append(element)
        matriz_a.append(row)

    # Obtener los elementos de la matriz B (Soluciones)
    print("Ingrese los elementos de la matriz B (Las soluciones de las ecuaciones), \n ej: solución de la primer ecuación, luego la de la segunda ... :")
    for _ in range(filas):
        element = float(input("Ingrese la solución: "))
        matriz_b.append([element])

    matrices_a.append(matriz_a)
    matrices_b.append(matriz_b)

# Resolver los sistemas de ecuaciones y mostrar las soluciones
for i in range(cantidad_matrices):
    print(f"\nSistema de Ecuaciones {i + 1}:")
    solucion = gauss_jordan(matrices_a[i], matrices_b[i])
    variables = []
    for j in range(len(solucion)):
        if j < 3:
            variables.append(chr(88 + j))
        elif j == 3:
            variables.append("D")
        else:
            variables.append(chr(97 + j - 4))
    for j in range(len(solucion)):
        print(f"{variables[j]} = {solucion[j][0]}")


