usuarios = { 
"iperurena": { 
        "nombre": "Iñaki", 
                "apellido": "Perurena", 
                "password": "123123" 
        }, 
"fmuguruza": { 
        "nombre": "Fermín", 
                "apellido": "Muguruza", 
                "password": "654321" 
        }, 
"aolaizola": { 
        "nombre": "Aimar", 
                "apellido": "Olaizola", 
                "password": "123456" 
        } 
} 
c=0
user=input("Ingrese el usuario:")
while True:
        if user=="iperurena":
                break
        elif user=="fmuguruza":
                break
        elif user=="aolaizola":
                break
        else:
                print("Este usuario no se encuentra en la base de datos")
                user=input("Ingrese el usuario:")

if user=="iperurena":
        password=input("Ingrese la contraseña:")
        while password!="123123":
                password=input("Ingrese la contraseña:")
                c=c+1
                if c==2:
                        print("Maximo de intentos alcanzado")
                        break
        if password=="123123":
                print("Iñaki Perurena")

if user=="fmuguruza":
        password=input("Ingrese la contraseña:")
        while password!="654321":
                password=input("Ingrese la contraseña:")
                c=c+1
                if c==2:
                        print("Maximo de intentos alcanzado")
                        break
        if password=="654321":
                print("Fermín Muguruza")

if user=="aolaizola":
        password=input("Ingrese la contraseña:")
        while password!="123456":
                password=input("Ingrese la contraseña:")
                c=c+1
                if c==2:
                        print("Maximo de intentos alcanzado")
                        break
        if password=="123456":
                print("Aimar Olaizola")