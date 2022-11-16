m = input("Ingrese las variables separadas (A/B/C/D)")
(a,b,c,d)= m.split("/")
a = int(a)
b = int(b)
c = int(c)
d = int(d)

if c > 5:
    b = b+1
    c = 0
    d = 0
else:
    c = 0
    d = 0

pa = str(a)
pb = str(b)
pc = str(c)
pd = str(d)

print(pa+pb+pc+pd)

