"""
@author: David Santos
version: 3.7.3
"""
print (" *** Dada una tupla de tuplas de 2 enteros genere numeros complejos con la tupla de tuplas *** \n")
enteros = ((2, 1), (15, 3), (22, 8), (13, 4), (1, 1), (78, 225) )
print("La tupla de tuplas de 2 numeros enteros es: {}".format(enteros))
lista = [ (x[0] + (x[1] * 1j)) for x in enteros]
tupla = tuple(lista)
print("la tupla de tuplas con numeros complejos es: {}".format(tupla) )