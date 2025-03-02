import random

#Codigo aparte por si implemento que se pueda dar pociones del enemigo o utilizar una baya en el pokémon (Posiblemente no lo haga, pero ordena más el codigo creo)

def EnemyAttack(Enemy, Player):
   
    # Seleccionar un movimiento aleatorio
    if not Enemy["movs"]:
        print(f"{Enemy["name"]} no tiene movimientos disponibles y pierde el turno.")
        return

    return random.choice(Enemy["movs"])
