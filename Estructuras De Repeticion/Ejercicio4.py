n=6
lista=[]
while True:
    if n<61:
        lista.append(n)
        n=n+5
    if n==61:
        lista.append(n)
        print("El doceavo termino es:",n)
        print("la suma de todos los terminos es:",sum(lista))
        break
