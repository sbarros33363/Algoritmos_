k = int(input("Ingrese su consumo"))

if k > 500:
    t = 120000
else:
    if k > 300:
        t = 100000
    else:
        if k > 100:
            t = 80000
        else:
            t= 4600

print ("El total a pagar es",k*t)