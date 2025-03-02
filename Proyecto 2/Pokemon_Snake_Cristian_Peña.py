import random
from os import system
import readchar

## Me disculpo por el desorden, aun no me adapto bien al funcionamiento de python ##

##### SNAKE ###############
#Para el vector
Pos_X = 0
Pos_Y = 1

Width_Map = 20
Height_Map = 15

My_pos = [3,1]
My_Tail = []
player_Tail = 0

Points_count = 2

Points = [] 

Win = 0

Player_Color = "\033[32m"
Points_Color = "\033[31m"
Obstacles_Color = "\033[34m"
Reset = "\033[0m"  # Restablecer al color por defecto


Obstacles_Map = """\
##      ##### ######
                    
#  ### ####  ####  #
#  #      #  ####  #
#     ####  #      #
#     #      ######  #
      ### ####      #
#  #              ##  #
#      ##    ## ###  #
#  #               #  #
#     ##   ###  ####  #
                  #  #
#  ######  ######  #  #
#                    #
#######  ###########\
"""
##### SNAKE ###############

##### POKÉMON ############

Max_Health = 100
# Player_Life = Max_Health
# Enemy_Life = Max_Health

Damage_Attack = 0

My_Pokemon = ["Bulbasaur", "Charmander", "Squirtle"]
My_index = 0

My_Pokemon_Attacks = [
    ["Placaje", "Látigo Cepa", "Tierra Viva"],   # Bulbasaur
    ["Placaje", "Ascuas", "Corte Fuego"],        # Charmander
    ["Placaje", "Pistola Agua", "Puño Hielo"],   # Squirtle
    ["Placaje", "Impactrueno", "Rayo"],          # Pikachu
]

My_Pokemon_Attacks_Damage = [
    [5, 15, 25],  # Bulbasaur (Placaje, Látigo Cepa, Tierra Viva)
    [5, 15, 25], # Charmander (Placaje, Ascuas, Corte Fuego)
    [5, 15, 25], # Squirtle (Placaje, Pistola Agua, Puño Hielo)
    [5, 15, 25],  # Pikachu (Placaje, Impactrueno, Rayo)
]

Trainer_names = [
    "Entrenador Javier", "Entrenador Alexander", "Entrenadora Rocío", "Entrenadora Macarena", 
    "Entrenadora María", "Entrenador Leonardo", "Entrenador Sasha", "Entrenador Matias", 
    "Entrenador Sergio", "Entrenador Joaquin", "Entrenador Gabriel", "Entrenador Ricardo", 
    "Entrenador Said", "Entrenador Juanito"
]

Pokemon_Enemy = ["Caterpie", "Weedle", "Pidgey", "Rattata", "Spearow"]

Enemy_Attack = [
    ["Placaje", "Disparo Demora", "Picadura"],      # Caterpie
    ["Placaje", "Picadura", "Hilo Seda"],          # Weedle
    ["Placaje", "Tornado", "Ataque Arena"],        # Pidgey
    ["Placaje", "Ataque Rápido", "Colmillo Ígneo"],# Rattata
    ["Picotazo", "Ataque Rápido", "Furia"]         # Spearow
]
Enemy_Attack_Damage = [
    [5, 10, 15],  # Caterpie
    [5, 10, 15],  # Weedle
    [5, 10, 20],  # Pidgey
    [5, 15, 20],  # Rattata
    [10, 15, 20]  # Spearow
]

##### POKÉMON ############

### SNAKE def ####
         
def Tail_pos(My_Tail):
    My_Tail.insert(0, My_pos.copy())  
    My_Tail = My_Tail[:player_Tail]
    return My_Tail


### SNAKE def ####
### POKÉMON def ####

import readchar

My_Pokemon = ["Bulbasaur", "Charmander", "Squirtle", "Pikachu"]  # Iniciales de Kanto

def Start_pokemon():
    print("¡Bienvenido, entrenador Pokémon! Tu aventura está a punto de comenzar. \nEscoge sabiamente uno de estos tres Pokémon iniciales de la región de Kanto para comenzar tu viaje.")    
    
    while True: #Seleccion de pokémon
        index = int(input("\nSelecciona un Pokémon inicial: \n1. Bulbasaur \t2. Charmander \n3. Squirtle\t4. Pikachu\n"))
        
        if index == 1 or index == 2 or index == 3 or index == 4:
            index = int(index) - 1  # Convierte la tecla a índice (0, 1, 2, 3)
            print("\n¿Estás seguro que deseas a {} como tu Pokémon inicial? (Y/N)".format(My_Pokemon[index]))
            
            response = readchar.readkey().upper()
            
            if response == 'Y':  
                print("Has elegido a {} como tu Pokémon inicial.".format(My_Pokemon[index]))
                break  

            elif response == 'N':  
                system("cls")
                print("No has seleccionado a este Pokémon. Elige otro.")  

            else:
                system("cls")
                print("Respuesta no válida. Por favor, responde con 'Y' o 'N'.")
        else:
            system("cls")
            print("\nSelección inválida. Elige 1, 2, 3 o 4 para seleccionar tu Pokémon.")
    
    return index

def Batalla_pokemon(Trainer):
    enemy_index = random.randint(0, len(Pokemon_Enemy) - 1)
    Player_Life = Max_Health
    Enemy_Life = Max_Health
    Turn = 0

    print("\nEs un {}!!!\n".format(Pokemon_Enemy[enemy_index]))

    while Player_Life > 0 and Enemy_Life > 0: # condición de derrota

        if Turn == 0:  # Turno del jugador
            # Player life
            print("{}{}{}:".format(Player_Color, My_Pokemon[My_index], Reset))
            Current_Life = Player_Life // 5
            Lost_Life = Max_Health // 5 - Current_Life
            print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, Player_Life, Max_Health))

            # Enemy life
            print("\n{}{}{}:".format(Points_Color,Pokemon_Enemy[enemy_index], Reset))
            Current_Life = Enemy_Life // 5
            Lost_Life = Max_Health // 5 - Current_Life
            print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, Enemy_Life, Max_Health))

            # Player Turn
            print("\nTurno de {} \n".format(My_Pokemon[My_index]))
            while True:
                Attack = int(input("Ataques disponibles:\n1. {} \t2. {}  \n3. {} \n".format(My_Pokemon_Attacks[My_index][0], My_Pokemon_Attacks[My_index][1], My_Pokemon_Attacks[My_index][2])))

                if Attack in [1, 2, 3]:
                    print("{} realiza {}".format(My_Pokemon[My_index], My_Pokemon_Attacks[My_index][Attack-1]))  # Ajuste de índice de ataque

                    Enemy_Life -= My_Pokemon_Attacks_Damage[My_index][Attack-1]
                    print("\n {} pierde {} de vida. ({}/{})".format(Pokemon_Enemy[enemy_index], My_Pokemon_Attacks_Damage[My_index][Attack-1], Enemy_Life, Max_Health))
                    Turn = 1  # Cambiar al turno del enemigo
                    break
                else:
                    print("Seleccione una opción válida.")
        
        elif Turn == 1:  # Turno del enemigo
            # Player life
            print("{}{}{}:".format(Player_Color, My_Pokemon[My_index], Reset))
            Current_Life = Player_Life // 5
            Lost_Life = Max_Health // 5 - Current_Life
            print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, Player_Life, Max_Health))

            # Enemy life
            print("\n{}{}{}:".format(Points_Color,Pokemon_Enemy[enemy_index], Reset))
            Current_Life = Enemy_Life // 5
            Lost_Life = Max_Health // 5 - Current_Life
            print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, Enemy_Life, Max_Health))
            
            # Enemy Turn
            print("\nTurno de {} \n".format(Pokemon_Enemy[enemy_index]))
            Attack = random.randint(0, len(Enemy_Attack[enemy_index]) - 1)  # Selecciona un ataque dentro del rango de ataques del enemigo
            print("{} realiza {}".format(Pokemon_Enemy[enemy_index], Enemy_Attack[enemy_index][Attack]))

            Player_Life -= Enemy_Attack_Damage[enemy_index][Attack]
            print("\n {} pierde {} de vida. ({}/{})".format(My_Pokemon[My_index], Enemy_Attack_Damage[enemy_index][Attack], Player_Life, Max_Health))

            Turn = 0  # Cambiar al turno del jugador

    if Player_Life > 0:
        print("{} es el ganador".format(My_Pokemon[My_index]))
        print("{} se ha curado tras el combate".format(My_Pokemon[My_index]))
        return 0
    elif Enemy_Life > 0:
        print("{} es el ganador".format(Pokemon_Enemy[enemy_index]))
        print("{}: ha sido una gran batalla.".format(Trainer))
        return 2



### POKÉMON def ####

Obstacles_Map = [list(row) for row in Obstacles_Map.split("\n")]


while len(Points)  < Points_count:
    point_pos = [random.randint(0, Width_Map-1), random.randint(0, Height_Map-1)]

    if point_pos not in Points and point_pos not in My_pos and Obstacles_Map[point_pos[1]][point_pos[0]] != "#":
        Points.append(point_pos)
        print(point_pos, end="")

My_index = Start_pokemon()

# Bucle Snake
while Win == 0:
    print("Jugador {} Largo {}".format(My_Tail, player_Tail))
   
    #DRAW MAP
    print("---" * Width_Map  + "--")
    for rellenar_y in range(Height_Map):
        print("|", end = "") #end es para que no haya salto de linea

        for rellenar_x in range(Width_Map):
            
            value = " "
            point_in = None

            # Obstaculos
            if Obstacles_Map[rellenar_y][rellenar_x] == "#":
                value = Obstacles_Color + "#" + Reset
                            
            # Puntos
            for map_obj in Points:
                if map_obj == [rellenar_x, rellenar_y]:
                    value = Points_Color + "O" + Reset
                    point_in = map_obj
            # Pos
            if(My_pos == [rellenar_x, rellenar_y]):
                value = Player_Color + "X" + Reset

            # Pos cola
            for tail in My_Tail:
                if tail == [rellenar_x, rellenar_y]:
                    value =  Player_Color + "X" + Reset

            print("[{}]".format(value), end="")

        print("|")

    print("---" * Width_Map + "--")

    #Actualizar la cola antes de mover al jugador
    My_Tail = Tail_pos(My_Tail)

    while True: #Movement
        direction = readchar.readkey().upper() 

        if direction == "W":    # Mover arriba
            if My_pos[Pos_Y] > 0 and Obstacles_Map[My_pos[Pos_Y] - 1][My_pos[Pos_X]] != "#":
                My_pos[Pos_Y] -= 1 
                break 
                

            elif My_pos[Pos_Y] == 0 and Obstacles_Map[Height_Map - 1][My_pos[Pos_X]] != "#":
                My_pos[Pos_Y] = Height_Map - 1 
                break 
            

        elif direction == "S":    # Mover abajo
            if My_pos[Pos_Y] < Height_Map - 1 and Obstacles_Map[My_pos[Pos_Y] + 1][My_pos[Pos_X]] != "#":
                My_pos[Pos_Y] += 1  
                break
                

            elif My_pos[Pos_Y] == Height_Map - 1 and Obstacles_Map[0][My_pos[Pos_X]] != "#":
                My_pos[Pos_Y] = 0  
                break
        

        elif direction == "A":    # Mover izquierda
            if My_pos[Pos_X] > 0 and Obstacles_Map[My_pos[Pos_Y]][My_pos[Pos_X] - 1] != "#":
                My_pos[Pos_X] -= 1  
                break
                

            elif My_pos[Pos_X] == 0 and Obstacles_Map[My_pos[Pos_Y]][Width_Map - 1] != "#":
                My_pos[Pos_X] = Width_Map - 1  
                break
                

        elif direction == "D":    # Mover derecha
            if My_pos[Pos_X] < Width_Map - 1 and Obstacles_Map[My_pos[Pos_Y]][My_pos[Pos_X] + 1] != "#":
                My_pos[Pos_X] += 1  
                break
                

            elif My_pos[Pos_X] == Width_Map - 1 and Obstacles_Map[My_pos[Pos_Y]][0] != "#":
                My_pos[Pos_X] = 0  
                break

        elif direction == "Q":    # Salir
            Win = -1
            break
        
        print("Dirección inválida o hay un obstáculo en esa dirección.")


    if My_pos in Points:        #Recoger puntos
        Points.remove(My_pos)
        player_Tail += 1  
        Trainer = Trainer_names[random.randint(0, len(Trainer_names) - 1)]
        print("{} te desafia a una batalla pokémon.".format(Trainer))
        Win = Batalla_pokemon(Trainer)
        Trainer_names.remove(Trainer)

    # Comprobar si el jugador choca con su propia cola
    if My_pos in My_Tail or Win == 2:
        print(Points_Color + "¡Has perdido!" + Reset)
        break    

    if Win == -1:
        print("Cerrar juego")

    # Comprobar si no quedan puntos
    if not Points:  # Si no quedan puntos, el jugador gana
        Win = 1
        system("cls")           
        print("¡Has ganado!")
        break   
      
    system("cls")
