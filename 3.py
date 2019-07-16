"""
@author: David Santos
version: 3.7.3
"""
print(" *** Dada una lista de numeros complejos obtener el doble de la parte real y el triple de la parte imaginaria en dos listas diferentes *** ")
complejos = [(1+3j), (2-5j), (4+2j), (5-5j), (20+3j), (3.1415+2j)]
print("la lista de complejos es: {} \n".format(complejos) )
doble = [(x.real * 2) for x in complejos]
triple = [(x.imag * 3j) for x in complejos]
print ("el doble de la parte real en la lista de complejos es {}".format(doble) )
print ("el triple de la parte imaginaria en la lista de complejos es {}".format(triple) )