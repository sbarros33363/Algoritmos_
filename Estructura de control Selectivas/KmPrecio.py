km = int(input("Digite la cantidad de km recorridos: "))

if km < 300:
    a = 50000
else:
    if km < 1000:
        a = 70000+((km-300)*30000)
    else:
        a = 150000+((km-1000)*9000)

print ("El costo total es de: $",a)