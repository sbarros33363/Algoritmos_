Algoritmo Calculadora_notas
	Escribir'Cual es su 1ra nota:'
	Leer n1
	Escribir'Cual es su 2da nota:'
	Leer n2
	Escribir'Cual es su 3ra nota:'
	Leer n3
	
	n1a<-trunc(n1*0.55)
	n2a<-trunc(n2*0.30)
	n3a<-trunc(n3*0.15)
	
	tt<-trunc(n1a+n2a+n3a)
	
	Escribir "Su definitiva es: " tt
FinAlgoritmo
