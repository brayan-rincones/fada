#!/usr/bin/env python3

# Implementación de Counting Sort
# Ordena una lista de tuplas en orden ascendente en O(n).
# Cada tupla tiene la forma (llave:valor) valor es un entero de 0 a k
def sort(lista, k):
    C = [0 for i in range(k)]
    B = [None for i in range(len(lista))] 
    
    for j in range(len(lista)):
        indice = lista[j][1] - 1
        C[indice] = C[indice] + 1

    for i in range(2,k):
        C[i] = C[i] + C[i-1]
    
    for j in range(len(lista)-1, -1,-1):
        indice = lista[j][1] - 1 # Hace las veces de C[A[j]] en el pseudocódigo del libro.
        B[indice] = lista[j]
        C[indice] -= 1
    
    return B
