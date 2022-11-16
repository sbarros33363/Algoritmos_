b = int(input("Ingrese la cantidad de dinero "))

if b>= 100000:
    queda=b//100000
    print("Existen "+str(queda)+" billetes de 100.000")
    b = b % 100000

if b>= 50000:
    queda=b//50000
    print("Existen "+str(queda)+" billetes de 50.000")
    b = b % 50000

if b>= 20000:
    queda=b//20000
    print("Existen "+str(queda)+" billetes de 20.000")
    b = b % 20000

if b>= 10000:
    queda=b//10000
    print("Existen "+str(queda)+" billetes de 10.000")
    b = b % 10000

if b>= 5000:
    queda=b//5000
    print("Existen "+str(queda)+" billetes de 5.000")
    b = b % 5000

if b>= 2000:
    queda=b//2000
    print("Existen "+str(queda)+" billetes de 2.000")
    b = b % 2000

if b>= 1000:
    queda=b//1000
    print("Existen "+str(queda)+" billetes de 1.000")
    b = b % 1000

if b>= 500:
    queda=b//500
    print("Existen "+str(queda)+" monedas de 500")
    b = b % 500

if b>= 200:
    queda=b//200
    print("Existen "+str(queda)+" monedas de 200")
    b = b % 200

if b>= 100:
    queda=b//100
    print("Existen "+str(queda)+" monedas de 100")
    b = b % 100

if b>= 50:
    queda=b//50
    print("Existen "+str(queda)+" monedas de 50")
    b = b % 50