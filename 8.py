"""
@author: David Santos
version: 3.7.3
"""
import re
while True:
    print(" *** Dado el ingreso de una hora en formato hh:mm:ss dividirla por el : despues anadirle un seg *** \n")
    date = input("Ingrese una hora en especifico: ")
    regex = re.compile('\d{2}:\d{2}:\d{2}')
    regex.match(date)
    if regex.match(date):
        hor = int(date.split(":")[0])
        m = int(date.split(":")[1])
        seg = int(date.split(":")[2])
        if seg > -1 and seg < 59:
            print("La hora es: " + "%02d : %02d : %02d \n" % (hor, m, seg + 1))
        elif hor == 23 and m == 59 and seg == 59:
            hor = 0
            m = 0
            seg = 0
            print("La hora es: " + "%02d : %02d : %02d \n" % (hor, m, seg))
        elif m == 59 and seg == 59:
            hor += 1
            m = 0
            seg = 0
            print("La hora es: " + "%02d : %02d : %02d \n" % (hor, m, seg))
        elif seg == 59:
            m += 1
            seg = 00
            print("La hora es: " + "%02d : %02d : %02d \n" % (hor, m, seg))
        
        else:
            pass
    else:
        print("Por favor ingrese una hora con el formato indicado!")
