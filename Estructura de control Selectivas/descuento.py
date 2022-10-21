a = int(input("Ingrese el monto de la compra"))
n = input("Ingrese su nombre")

if a < 50000:
    d = 0
else:
    if a <100001:
        d = 5
    else:
        if a < 700001:
            d = 11
        else:
            if a < 1500001:
                d = 18
            else:
                d = 25

print("Hola!",n)
print("Se ha descontado un valor de: $",(d/100)*a)
print("Para un total de: $",a-((d/100)*a))