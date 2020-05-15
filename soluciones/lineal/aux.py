#!/usr/bin/env python3

# Implementación de Counting Sort
# Ordena una lista de tuplas en orden ascendente en O(n).
# Cada tupla tiene la forma (llave:valor) valor es un entero de 0 a k
def sort(lista, k):
    C = [0 for i in range(k+1)]
    B = [None for i in range(len(lista))]
    
    for j in range(len(lista)):
        C[lista[j][1]] += 1
    
    for i in range(1,k+1):
        C[i] = C[i] + C[i-1]
    
    for j in range(len(lista)-1, -1,-1):
        index = C[lista[j][1]] - 1
        B[index] = lista[j][0] # B solo contiene los animales.
        C[lista[j][1]] -= 1

    return B

# Función hash.
def hash(key:str, context:list) -> list:
    for scene in context: # Itera sobre cada escena de la apertura ordenada
