#!/usr/bin/env python3
import sys, json
import pprint
import aux

N = 0
M = 0
K = 0

parts = []
# Se encarga de "traducir" cada línea del archivo entrada
# a tipos de datos trabajables.
def process_input(file):
    with open(file) as _input:
        lines = _input.readlines()
    
    global N,M,K 
    N,M,K= int(lines[0]), int(lines[1]), int(lines[2]) 
    
    animals = json.loads(lines[3])
    greatness = json.loads(lines[4])
    global animals_dict
    animals_dict = dict(zip(animals, greatness)) # Diccionario (animal:grandeza)

    for i in range(5, (M-1)+6):
        _part = json.loads(lines[i])
        parts.append(_part)
 
scenes_greatness = []
# Ordena la apertura. Por cada escena se crea una lista que tendrá tres tuplas (animal:valor) correspondientes
# a los tres animales de la escena (línea 35). En la línea 36 se ordena está lista de tuplas y se reemplaza en la lista
# de apertura(opening), en las líneas 39-44 se calculan las grandezas de cada escena y se ordena la apertura de acuerdo a esto.
def sort_opening():
    opening = parts[0]
    for i,_scene in enumerate(opening): # O((m-1)*k)
        _tuple = [(animal, animals_dict[animal]) for animal in _scene] # O(3) 
        opening[i] = aux.sort(_tuple,N) # O(3)
        
        _list_of_greatnesses = list( zip(*_tuple))[1] # O(3)
        _greatness_sum = sum(_list_of_greatnesses) # Grandeza total para la escena actual.
        scenes_greatness.append(_greatness_sum)
    
    scenes_with_greatness = list(zip(opening, scenes_greatness)) #O((m-1)*k)
    return aux.sort(scenes_with_greatness, max(scenes_greatness))
    
# Ordena las partes que ocurren después de la apertura.
# Esto se logra por medio de un diccionario que mapea escenas de la apertura
# sin ordenar, a escenas de la apertura ordenadas (localmente).
def sort_rest_of_parts():
    sorted_opening = sort_opening()
    dic = {str(key):aux.hash( str(key), sorted_opening) for key in parts[0]}
    pprint.pprint(dic)
    exit()

    #for part in parts[1:]: # O(M-1)
     #   for scene in part: # O(K) --> O((M-1)K)
            
            

process_input(sys.argv[1])
sort_rest_of_parts()
