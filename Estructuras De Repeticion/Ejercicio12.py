n=[]
pt=[]
datos=int(input("Ingrese el numero de estudiantes a los que le va a tomar datos:"))
promedio=0
pi=0
ps=0
pip=0
psp=0
def max_dat(pt):
    m=pt[0]
    for i in pt:
        if i>m:
            m=i
    return m
def min_dat(pt):
    mi=pt[0]
    for i in pt:
        if i<mi:
            mi=i
    return mi

for _ in range(0,datos):
    Name=input("Ingrese el nombre:")
    puntajefinal=float(input("Ingrese el puntaje final:"))

    n.append(Name)
    pt.append(puntajefinal)
    Listaf=list(zip(n,pt))

    for a,b in Listaf:
        i=max_dat(pt)
        j=min_dat(pt)
        if b==i:
            nombremax=f"El nombre de la persona con mejor puntaje es:{a}"
        elif b==j:
            nombremin=f"El nombre de la persona con menor puntaje es:{a}"
        maxpt=f"El mayor puntaje obtenido es: {i}"
        minpt=f"El menor puntaje obtenido es: {j}"

    for puntajefinal in pt:
        suma=sum(pt)
        promedio=suma/datos
        prom=f"El promedio de los puntajes obtenidos es de:{promedio}"
        if puntajefinal<promedio:
            pi=pi+1
            pip=(pi/datos)*100
            porcentajei=f"El porcentaje de personas con puntaje inferior al promedio es de:{pip}%"
        elif puntajefinal>=promedio:
            ps=ps+1
            psp=(ps/datos)*100
            porcentajes=f"El porcentaje de personas con puntaje superior al promedio es de:{psp}%"
print(nombremax)
print(nombremin)
print(maxpt)
print(minpt)
print(prom)
print(porcentajei)
print(porcentajes)
