"""
@author: David Santos
version: 3.7.3
"""
print(" *** Ingresar un numero y calcular la suma desde el 1 hasta el numero ingresado *** \n")
cont = 0
n = 1
m = 11
while True:
    rta = input("Desea continuar s/n ? ")
    if rta == 'n' or rta == 'N' or rta == 'no' or rta == 'NO' or rta == 'No':
        break
    else:
        if cont == 0:
            for i in range(n, m):
                print("* %d" % i)
        elif cont > 0:
            n += 10
            m += 10
            for i in range(n, m):
                print("* %d" % i)
    cont += 1
