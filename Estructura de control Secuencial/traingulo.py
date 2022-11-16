#entrada
LadoA = int(input("Ingrese el primer lado a: "))
LadoB = int(input("Ingrese el segundo lado b: "))
LadoC = int(input("Ingrese el tercer lado c: "))
#caja negra
Perimetro = (LadoA+LadoB+LadoC)
Sp = Perimetro / 2
area=(Sp * (Sp - LadoA) * (Sp - LadoB) * (Sp - LadoC))**0.5
#salida
print("El area del triangulo es: ",area)
