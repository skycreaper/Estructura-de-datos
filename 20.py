"""
@author: Juan Camilo Sarmiento
version: 3.7.4
"""
print(" *** Genere dos listas con la suma de los numeros negativos y numeros positivos *** \n")
numeros = (-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5)
print("Tupla inicial es: {}".format(numeros) )
print((sum([x for x in numeros if x < 0]), sum([x for x in numeros if x > 0]))) 