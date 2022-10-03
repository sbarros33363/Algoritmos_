Algoritmo Salario_Comsiones
	Escribir "Tenga en cuenta que esta calculadora toma en cuenta 3 variables iguales mas un 10% de comision"
	Escribir 'Cual es su salario por venta: '
	Leer s
	s1<-trunc(s*3)
	s2<-trunc(s1*0.10)
	s3<-trunc(s2 + s1)
	
	Escribir "Su Salario es de :" s
	Escribir " Sus Comisiones son de: " s2
	Escribir " Su total es: " s3
FinAlgoritmo
