t = int(input("Ingrese la temperatura en grados fahrenheit"))

if t > 85:
    print("Natacion")
else:
    if t > 70:
        print("Tenis")
    else:
        if t > 32:
            print("Golf")
        else:
            if t > 10:
                print("Esqui")
            else:
                print("Marcha")