# ejemplo_2
def bubble_sort(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==valor:
                return True, (i, j)
            return False, None

# Ejemplo de uso
    mi_matriz=[
     [9,3,6],
     [6,3,9],
     [3,6,9]
     ]

valor_a_buscar = 3
encontrado, posicion = buscar_valor(mi_matriz, valor_a_buscar)

if encontrado:
    print(f"El valor {valor_a_buscar} se encuentra en la posicion {posicion}")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")