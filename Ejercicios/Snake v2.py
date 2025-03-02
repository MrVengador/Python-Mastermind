import random
from os import system
import readchar

#Para el vector
Pos_X = 0
Pos_Y = 1

Width_Map = 20
Height_Map = 15

My_pos = [3,1]
My_Tail = []
player_Tail = 0

Points_count = 10

Points = [] 

Win = 0

Mov_Keys = ["W", "A", "S", "D"]

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



def Movements():
   # Movimiento del jugador
    direction = readchar.readkey().upper()  # Captura y convierte a mayúscula

    if direction == "W":    # Mover arriba
        if My_pos[Pos_Y] > 0:
            My_pos[Pos_Y] -= 1  
            

        elif My_pos[Pos_Y] == 0:
            My_pos[Pos_Y] = Height_Map - 1  
           

    elif direction == "S":    # Mover abajo
        if My_pos[Pos_Y] < Height_Map - 1:
            My_pos[Pos_Y] += 1  
            

        elif My_pos[Pos_Y] == Height_Map - 1:
            My_pos[Pos_Y] = 0  
       

    elif direction == "A":    # Mover izquierda
        if My_pos[Pos_X] > 0:
            My_pos[Pos_X] -= 1  
            

        elif My_pos[Pos_X] == 0:
            My_pos[Pos_X] = Width_Map - 1  
            

    elif direction == "D":    # Mover derecha
        if My_pos[Pos_X] < Width_Map - 1:
            My_pos[Pos_X] += 1  
            

        elif My_pos[Pos_X] == Width_Map - 1:
            My_pos[Pos_X] = 0  

    elif direction == "Q":    # Salir
        Win = -1

    

          
def Tail_pos(My_Tail):
    My_Tail.insert(0, My_pos.copy())  
    My_Tail = My_Tail[:player_Tail]
    return My_Tail


Obstacles_Map = [list(row) for row in Obstacles_Map.split("\n")]

    

while len(Points)  < Points_count:
    point_pos = [random.randint(0, Width_Map-1), random.randint(0, Height_Map-1)]

    if point_pos not in Points and point_pos not in My_pos:
        Points.append(point_pos)
        print(point_pos, end="")



# Bucle principal del juego
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

    # Mover al jugador
    Movements()
    if Obstacles_Map[Pos_Y][Pos_X] == "#":
        print("OBSTACULOOOOOO in {}/{}".format([Pos_Y,Pos_X]))
        input()

    if My_pos in Points:        #Recoger puntos
        Points.remove(My_pos)
        player_Tail += 1  

    # Comprobar si el jugador choca con su propia cola
    if My_pos in My_Tail:
        print(Points_Color + "¡Has perdido!" + Reset)
        break    

    if Win == -1:
        print("Cerrar juego")

    # Comprobar si no quedan puntos
    if not Points:  # Si no quedan puntos, el jugador gana
        Win = 1
        system("cls")
        draw_map(player_Tail, Obstacles_Map)             
        print("¡Has ganado! Todos los puntos fueron recolectados.")
        break   
      
    # Limpiar pantalla
    system("cls")





