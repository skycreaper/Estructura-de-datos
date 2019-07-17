"""
@author: Juan Camilo Sarmiento
version: 3.7.4
"""
print(" *** Redactar un script el cual genere un conjunto usando conjuntos"+ 
    "por comprensión con los números del 1 al 21 que sean impares y que sean divisible por 3. *** \n")
print (set(x for x in range(1,22) if x % 2 != 0 if x % 3 == 0))