"""
@author: David Santos
"""
dias = [(1, "lunes"), (2, "martes"), (3, "miercoles"), (4, "jueves"), (5, "viernes"), (6, "sabado"), (7, "domingo")]
def dias_de_la_semana():
    while True:
        x = int(input("Ingrese un numero: "))    
        if x > 0 and x < 8:
            print(dias[x - 1])
        else:
            print("por favor ingresa un numero entre 1 - 7 \n")
            pass

if __name__ == "__main__":
    dias_de_la_semana()