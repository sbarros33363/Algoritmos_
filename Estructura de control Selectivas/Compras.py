m = int(input("Ingrese el monto total"))

if m > 5000000:
    inversionPropia = m*0.55
    prestamoBanco = m*0.33
    creditoFabrica = m*0.15
    intereses = creditoFabrica*0.20
    total = inversionPropia+prestamoBanco+creditoFabrica+intereses
else:
    inversionPropia = m*0.7
    creditoFabrica=m*0.3
    intereses=creditoFabrica*0.20
    total = inversionPropia+creditoFabrica+intereses
print("Monto inversion propia: $",inversionPropia)
print("Monto prestamo del banco: $",prestamoBanco)
print("Monto credito del fabricante: $",creditoFabrica)
print("Monto interes del fabricante: $",intereses)
print("Total de la compra: $",total)