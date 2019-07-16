"""
@author: David Santos
version: 3.7.3
"""
print(" *** Dado dos conjuntos realizar las operaciones logicas y guardarlas en una lista su resultado *** \n")
# n, -, diferencia simetrica
a = set('mago')
b = set('maiar')
lista = []
lista.append(a | b)
print ("union: ", a | b)
lista.append(a & b)
print ("interseccion: ", a & b)
lista.append(a - b)
print ("diferencia entre a - b: ", a - b)
lista.append(b - a)
print ("diferencia entre b - a: ", b - a)
lista.append(a ^ b)
print ("diferencia simetrica entre a y b: ", a ^ b)
print("resultados: {}".format(lista) )

