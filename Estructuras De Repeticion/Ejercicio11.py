while True:
    c=0
    lp=0
    menoresm=0
    hombresam=0
    encuestados=0
    pc=0
    pw=0
    e=[]
    encuestados=encuestados+1
    licor=input("¿Cosume licor?(Si o No):")
    if licor=="No":
        print("No se puede tomar en cuenta para esta encuesta")
    if licor=="Si":
        tipo=int(input("Licor prefereido (1- Aguardiante, 2-Ron, 3-Cerveza, 4-Tequila, 5-Whisky, 6-Otro):"))
        edadp=("Que edad tiene:")
        e.append[edadp]
        genero=input("Escriba su genero (Masculino o Femenino):")

        if licor=="Si":
            c=c+1
        if genero=="Femenino":
            if edadp<18:
                menoresm=menoresm+1
        if genero=="Masculino":
            if tipo!=1:
                if edadp>=20 and edadp<=25:
                    hombresam=hombresam+1
        for _ in e:
            if tipo==3:
                pc=pc+_
                promediopc=pc/encuestados
            if tipo==5:
                pw=pw+1
                porcentajepw=(pw*100)/encuestados
            print("El total de personas encuestadas que consumen licor es de:",c)
            print("El total de mujeres menores de edad es de:",menoresm)
            print("El total de hombres que no consumen aguardiente y tiene entre 20 y 25 años es de:",hombresam)
            print("El promedio de edad de las personas que consumen cerveza es de:",promediopc)
            print("El porcentaje de personas que consumen whisky en relacion a el numero de encuestados es de:",porcentajepw)
            seguir=input("¿Desea seguir con la investigación?(True=Si y False=No):")
            if seguir==True:
                seguir=seguir
            if seguir==False:
                break