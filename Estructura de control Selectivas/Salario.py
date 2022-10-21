s = int(input("Ingrese el sueldo del trabajador"))
if s < 900000:
    a = s*0.15
else:
    a = s*0.12
st=s+a
print("Su sueldo tuvo un aumento de $",a,"pesos")
print("Su sueldo total es $",st,"pesos")
