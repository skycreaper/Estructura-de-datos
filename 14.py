"""
@author: David Santos
version: 3.7.3
"""
print(" *** imprimir la suma de los primeros 10 enteros usando ciclos for y while, listas, tuplas y conjuntos por comprehension *** \n")
#ciclo for
def loopFor():
    print("Ciclo For")
    res = 0
    for x in range(10):
        res += x
        print(res)
#ciclo while
def loopWhile():
    i = 0
    r = 0
    print("Ciclo While")
    while i < 10:
        r += i
        print(r)
        i += 1
def listasbyC():
    print("listas por comprehension")
    print([(i*2,x) for i, x in enumerate(range(10), 1)])


        
# def tuplasbyC():
# def conjuntosbyC():


if __name__ == "__main__":
    loopFor()
    loopWhile()
    listasbyC()