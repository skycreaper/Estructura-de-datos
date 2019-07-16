"""
@author: David Santos
version: 3.7.3
"""
print(" *** Ingresar un numero y calcular la suma desde el 1 hasta el numero ingresado *** \n")
num = int(input("Ingrese un numero para calcular: "))
r = 0
for x in range(1, num + 1):
    r += x
    print("*%d" %r)
