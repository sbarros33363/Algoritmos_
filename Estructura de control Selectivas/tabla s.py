c = int(input("Ingrese la categoria"))
s = int(input("Ingrese el salario bruto"))

if c == 1:
    t = s *0.1
else:
    if c == 2:
        t = s*0.15
    else:
        if c == 3:
            t = s*0.2
        else:
            if c == 4:
                t = s*0.4
            else:
                if c == 5:
                    t = s*0.6

print("La categoria del trabajador es",c,"y su salario total es",s+t)