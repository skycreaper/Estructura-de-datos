"""
@author: David Santos
version: 3.7.3
"""
print(" *** Mostrar la suma de los numeros pares e impares de 1 a 100 *** \n")
r = 0
res = 0
c = 0
cont = 0
for x in range(1, 101):
    if x % 2 == 0:
        r += x
        c += 1
    else:
        res += x
        cont += 1
print("Suma de los pares es: %d Promedio: %f" %(r, r/c) )    
print("Suma de los impares es: %d Promedio: %f" %(res, res/cont) )