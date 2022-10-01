Algoritmo Lector_Minutos
	Escribir 'Cuantos minutos quiere cambiar a horas: '
	Leer m
	d<-trunc(m/60)
	h<-m MOD 60
	Escribir "Horas " d
	Escribir "Minutos " h
FinAlgoritmo
