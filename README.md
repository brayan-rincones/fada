# Miniproyecto FADA

#### Integrantes
* David Santiago Cortés

* Alejandro Orozco

* Brayan Rincones


#### Ideas
Aquí pueden escribir sus ideas para la solución que decidan hacer, y luego yo las paso al informe, este va a ser como el borrador y pues si alguno
de ustedes también sabe latex también lo podrían pasar al informe, que es el archivo informe.tex

Idea para enfrentar el problema por medio de la complejidad O(nlogn):
En la descripcion del problema tenemos una serie de elmentos que, de alguna manera, hay que ordenarlos para dar con el espectaculo final. Al tener que organizar ascendentemente los escenarios de acuerdo a las grandezas de cada animal, ademas de organizar las partes acorde a las grandezas de las escenas que conlleve, se considera que este problema se puede llevar a cabo mediante el ordenamiento de Mergesort, cuando ya tengamos definido las caracteristicas de los animales, estos seran almacenados en arreglos, tanto nombres en un arreglo, como grandezas respectivas en otro arreglo, los cuales seran los datos de entrada. Ya organizados los animales en un escenario por una funcion auxiliar, esta misma es llamada adentro del mergesort, con esto estamos organizando las partes finales acorde a operaciones como tamaños de medias de grandezas de los escenarios. Extrayendo los datos, podemos obtener la media total de grandeza, el animal que mas participo, escena de mayor grandeza, menor grandeza asi como el que menos lo hizo mediante contadores, abstraccion y almacenamiento en nuevos arreglos de los resultados finales, cada operacion con su respectiva funcion dentro del algoritmo. 

#### Formato archivos de entrada.
Se me ocurre que el formato de los archivos de entrada puede ser el siguiente:
```
n
m
k
[animales]
[grandezas]
parte1
parte2
...
partem
```
Por ejemplo
```
6
3
2
["gato", "libelula", "ciempies", "nutria", "perro", "tapir"]
[3, 2, 1, 6, 4, 5]
[["tapir", "nutria", "perro"], ["tapir","perro", "gato"],["ciempies", "tapir", "gato"],["gato", "ciempies", "libelula"]]
[["tapir", "nutria", "perro"], ["ciempies", "tapir", "gato"]]
[["gato", "ciempies", "libelula"], ["tapir", "perro", "gato"]]
```
