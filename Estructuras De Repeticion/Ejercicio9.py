a=0
g=0
d=0
while True:
    tipo=int(input())
    if(tipo==1):
        a=a+1
    if(tipo==2):
        g=g+1
    if(tipo==3):
        d=d+1
    if(tipo==4):
        print("MUITO OBRIGADO")
        print("Alcohol:",a)
        print("Gasolina:", g)
        print("Diesel:",d)