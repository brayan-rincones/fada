#!/usr/bin/env python3
import sys, json
import aux

N = 0
M = 0
K = 0

animales = []
grandezas = []
partes = []
animales_y_grandezas = []
# Se encarga de "traducir" cada línea del archivo entrada
# a tipos de datos trabajables.
def procesar_entrada(archivo):
    with open(archivo) as _input:
        lineas = _input.readlines()
    
    N,M,K = int(lineas[0]), int(lineas[1]), int(lineas[2])
    
    animales = json.loads(lineas[3])
    grandezas = json.loads(lineas[4])
    
    for i in range(5, (M-1)+6):
        _parte = json.loads(lineas[i])
        partes.append(_parte)

    animales_y_grandezas = list(zip(animales, grandezas)) # Lista de tuplas (animal:grandeza)
    animales_y_grandezas = aux.sort(animales_y_grandezas, N)

procesar_entrada(sys.argv[1])
