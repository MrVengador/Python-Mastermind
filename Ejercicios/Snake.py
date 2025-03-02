import random
from os import system
import readchar

#Para el vector
Pos_X = 0
Pos_Y = 1

Width_Map = 20
Height_Map = 15

My_pos = [3,1]
My_Tail = [0,0]

player_Tail = 0

Points_count = 10

Points = [] 

Win = 0

Mov_Keys = ["W", "A", "S", "D"]

Player_Color = "\033[32m"
Points_Color = "\033[31m"
Obstacles = "\033[34m"
Reset = "\033[0m"  # Restablecer al color por defecto



def draw_map():
    print("---" * Width_Map  + "--")
    for rellenar_y in range(Height_Map):
        print("|", end = "") #end es para que no haya salto de linea

        for rellenar_x in range(Width_Map):
            
            value = " "

                            
            for map_obj in Points:
                if map_obj == [rellenar_x, rellenar_y]:
                    value = Points_Color + "O" + Reset

            if(My_pos == [rellenar_x, rellenar_y]):
                value = Player_Color + "X" + Reset

            for tail in My_Tail:
                if tail == [rellenar_x, rellenar_y]:
                    value =  Player_Color + "X" + Reset

            print("[{}]".format(value), end="")

        print("|")

    print("---" * Width_Map + "--")

def Movements(My_Tail):
# Movimiento del jugador
    direction = readchar.readkey().upper()  # Captura y convierte a mayúscula

    if direction == "W":    # Mover arriba
        if My_pos[Pos_Y] > 0:
            My_pos[Pos_Y] -= 1  
            #My_Tail.insert(0, My_pos.copy())
            #My_Tail =  My_Tail[:player_Tail]

        elif My_pos[Pos_Y] == 0:
            My_pos[Pos_Y] = Height_Map - 1  
            #My_Tail.insert(0, My_pos.copy())
            #My_Tail =  My_Tail[:player_Tail]

    elif direction == "S":    # Mover abajo
        if My_pos[Pos_Y] < Height_Map - 1:
            My_pos[Pos_Y] += 1  
            #My_Tail.insert(0, My_pos.copy())
            #My_Tail =  My_Tail[:player_Tail]

        elif My_pos[Pos_Y] == Height_Map - 1:
            My_pos[Pos_Y] = 0  
            #My_Tail.insert(0, My_pos.copy())
            #My_Tail =  My_Tail[:player_Tail]

    elif direction == "A":    # Mover izquierda
        if My_pos[Pos_X] > 0:
            My_pos[Pos_X] -= 1  
            # My_Tail.insert(0, My_pos.copy())
            # My_Tail =  My_Tail[:player_Tail]

        elif My_pos[Pos_X] == 0:
            My_pos[Pos_X] = Width_Map - 1  
            # My_Tail.insert(0, My_pos.copy())
            # My_Tail =  My_Tail[:player_Tail]

    elif direction == "D":    # Mover derecha
        if My_pos[Pos_X] < Width_Map - 1:
            My_pos[Pos_X] += 1  
            # My_Tail.insert(0, My_pos.copy())
            # My_Tail =  My_Tail[:player_Tail]

        elif My_pos[Pos_X] == Width_Map - 1:
            My_pos[Pos_X] = 0  
            # My_Tail.insert(0, My_pos.copy())
            # My_Tail =  My_Tail[:player_Tail]

            #My_Tail =  My_Tail[:player_Tail]

    # # Actualizar la cola del jugador
    #My_Tail.insert(0, My_pos.copy())  # Añade la posición actual al inicio de la cola
    #My_Tail = My_Tail[:player_Tail]  # Recorta la cola al tamaño máximo permitido


    if My_pos in Points:
        Points.remove(My_pos)
        player_Tail += 1      

while len(Points)  < Points_count:
    point_pos = [random.randint(0, Width_Map-1), random.randint(0, Height_Map-1)]

    if point_pos not in Points and point_pos not in My_pos:
        Points.append(point_pos)
        print(point_pos)

    

while Win == 0:

    print("Jugador {} Largo {}".format(My_Tail, player_Tail))

    draw_map()             
    #Movements(My_Tail)
# Movimiento del jugador
    direction = readchar.readkey().upper()  # Captura y convierte a mayúscula

    if direction == "W":    # Mover arriba
        if My_pos[Pos_Y] > 0:
            My_pos[Pos_Y] -= 1  
            My_Tail.insert(0, My_pos.copy())
            My_Tail =  My_Tail[:player_Tail]

        elif My_pos[Pos_Y] == 0:
            My_pos[Pos_Y] = Height_Map - 1  
            My_Tail.insert(0, My_pos.copy())
            My_Tail =  My_Tail[:player_Tail]

    elif direction == "S":    # Mover abajo
        if My_pos[Pos_Y] < Height_Map - 1:
            My_pos[Pos_Y] += 1  
            My_Tail.insert(0, My_pos.copy())
            My_Tail =  My_Tail[:player_Tail]

        elif My_pos[Pos_Y] == Height_Map - 1:
            My_pos[Pos_Y] = 0  
            My_Tail.insert(0, My_pos.copy())
            My_Tail =  My_Tail[:player_Tail]

    elif direction == "A":    # Mover izquierda
        if My_pos[Pos_X] > 0:
            My_pos[Pos_X] -= 1  
            My_Tail.insert(0, My_pos.copy())
            My_Tail =  My_Tail[:player_Tail]

        elif My_pos[Pos_X] == 0:
            My_pos[Pos_X] = Width_Map - 1  
            My_Tail.insert(0, My_pos.copy())
            My_Tail =  My_Tail[:player_Tail]

    elif direction == "D":    # Mover derecha
        if My_pos[Pos_X] < Width_Map - 1:
            My_pos[Pos_X] += 1  
            My_Tail.insert(0, My_pos.copy())
            My_Tail =  My_Tail[:player_Tail]

        elif My_pos[Pos_X] == Width_Map - 1:
            My_pos[Pos_X] = 0  
            My_Tail.insert(0, My_pos.copy())
            My_Tail =  My_Tail[:player_Tail]
    
   
    if My_pos in Points:
        Points.remove(My_pos)
        player_Tail += 1      

    while len(Points)  < Points_count:
        point_pos = [random.randint(0, Width_Map-1), random.randint(0, Height_Map-1)]

        if point_pos not in Points and point_pos not in My_pos:
            Points.append(point_pos)
            print(point_pos)
           
    if not Points:  # Si no quedan puntos, el jugador gana
            Win = 1
            system("cls")
            draw_map()             

            print("¡Has ganado! Todos los puntos fueron recolectados.")
            break     
    
    else: system("cls")  # Limpia la consola

