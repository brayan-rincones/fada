#!/usr/bin/env python3
import sys, json

N = 0
M = 0
K = 0

animales = []
grandezas = []
partes = []
# Se encarga de "traducir" cada línea del archivo entrada
# a tipos de datos trabajables.
def procesar_entrada(archivo):
    with open(archivo) as _input:
        lineas = _input.read()
    
    lineas = lineas.splitlines()
    N,M,K = int(lineas[0]), int(lineas[1]), int(lineas[2])
    
    animales = json.loads(lineas[3])
    grandezas = json.loads(lineas[4])
    
    for i in range(5, (M-1)+6):
        _parte = json.loads(lineas[i])
        partes.append(_parte)

procesar_entrada(sys.argv[1])
