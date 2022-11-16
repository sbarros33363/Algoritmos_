a = int(input("Ingrese la variable A"))
b = int(input("Ingrese la variable B"))
c = int(input("Ingrese la variable C"))
d = (b**2)-(4*(a))*(c)

if d == 0:
	print("x1 = x2 =",-(b)/(2*a))
else:
	if d>0:
		print("x1 =",(-b+(((b**2)-(4*a)*c)**0.5))/2)
		print("x2 =",(-b-(((b**2)-(4*a)*c)**0.5))/2)
	else:
		if d < 0:
			print("No hay soluciones reales")
			