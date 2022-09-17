# -*- coding: utf-8 -*-

# mostrar o numero informado no intervalo [0,25],[25,50],[50,75],[75,100]

numero = float(input("Informe um numero:"))
if numero >= 0 and numero <= 25:
    print("[0,25]")
elif numero > 25 and numero <= 50:
    print("[25,50]")
elif numero > 50 and numero <= 75:
    print("[50,75]")
elif numero > 75 and numero <= 100:
    print("[75,100]")
else:
    print("Fora do intervalo")
    