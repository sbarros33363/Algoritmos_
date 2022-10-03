Algoritmo descuento_tienda
	Escribir 'Cual es el total de su compra: '
	Leer t
	
	d<-trunc(t*0.15)
	tt<-trunc(t-d)
	
	Escribir "Su Descuento fue de: " d
	Escribir "Su total es: " tt
	
FinAlgoritmo
