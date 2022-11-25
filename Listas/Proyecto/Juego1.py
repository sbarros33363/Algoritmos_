import random

def jugar_ppt():
    J1 = int(input("¡Eligue tu arma! \n 1-Para piedra: \n 2-Para papel: \n 3-Para tijera:\n Selecciona uno de esos numero: "))
    C = random.randrange(1,4)
    print("La computadora escogio: ",C)
    
    if J1 == C:
        return 'Empate'
    elif ((J1 == '1' and C == '3')
    or (J1 =='3' and C =='2')
    or(J1 == '2' and C == '1')):
        return 'Ganaste la partida'
    else:
        return 'Lo lamento, perdiste'

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


