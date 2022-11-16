print ("Digitar la cantidad invertida")
c = int(input())
print("Digite la tasa de interes")
t = int(input())
interes = c * t
if interes > 100000:
    print("Los intereses ganados son",interes,"superan los $100.00")
else:
    print("Los intereses ganados son",interes,"no superan los $100.00")

print("El saldo total en la cuenta es:",c+interes)