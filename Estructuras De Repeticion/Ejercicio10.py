lista=[]
while True:
    alturas=float(input("Ingrese la altura del estudiante.Si no hay mas estudiantes escriba 0:"))
    if(alturas!=0):
        lista.append(alturas)
    if(alturas==0):
        print("el estudiante mas alto es de:",max(lista))
        break