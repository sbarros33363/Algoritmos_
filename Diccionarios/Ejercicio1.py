lista=[]
c=0
contador={}
n=int(input("Numero de datos que tendra la lista:"))
while True:
    elemento=int(input())
    lista.append(elemento)
    c=c+1
    if c==n:
        break
for a in lista:
    con=lista.count(a)
    contador.update({a:con})
print(contador)