# Area para cargar librerias

ppt = __import__('Juego1').jugar_ppt
ahor = __import__('Juego2').jugar_ahorcado
traer_lista_p = __import__('Juego2').listado

# Programa

Nombre_J = input("Digite el nombre del jugador : ")
print("Hola ",Nombre_J)
print("")
print("Selecciona uno de nuestros juegos: ")
juego = input('Presiona:\n(A) Piedra, Papel o Tijera \n(B) Ahorcado \n(C) \n(D) Juego de la Vida\nSelecciona una de esas tres opciones : ').upper()

if (juego == 'A'):
    #Jugar Piedra Papel o Tijera
    ppt()
    print(ppt)
    


elif (juego == 'B'):
    #Ahorcado
    ahor()

# **************************************************