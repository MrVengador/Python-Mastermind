import random
from Pokemon_DB import getAllPokemons, getAttacksPokemon, RefreshLevelPok, Evolution, TestEv
from Player import GetPlayerProfile, GetItemRandom
from Items import InventoryManagement, OcupeItem, AddItem
from PlayerCombat import Change_Pokemon, CheckLevel
from Enemy import GetEnemyProfile
from CombatManager import TrainerCombat, WildPokemonCombat, PlayerPokemonLives
from Historial import AddTrainer, PrintHistory

#Color text
Green = "\033[32m"
Red = "\033[31m"
Default = "\033[0m"  # Restablecer al color por defecto

LastEnemy = []


def Welcome():
    PokemonData = getAllPokemons(151)  # Cargar datos de los Pokémon #151 primeros pokemons (primera generacion)
    # Hay un error en la pagina, no se pueden cargar todos los pokemons, por lo que recomiendo cargar hasta el 28, el 29 da error al evolucionar y el 30 no carga en la pagina

    print("Bienvenido a tu aventura Pokémon, antes de comenzar, dime.")
    Player = GetPlayerProfile(PokemonData)  # Obtener perfil del jugador
    print("{}, tu aventura pokémon esta por comenzar, suerte junto a {}, {} y {}.\nQue trinfen en todos sus desafios.".format(Player["name"],
        Player["team"][0]["name"], Player["team"][1]["name"], Player["team"][2]["name"]))
    
    for i in range(len(Player["team"])):
        Player["team"][i] = RefreshLevelPok(Player["team"][i])
    
    #Para testear la evolucion
    # Player["team"].append(PokemonData[0]) # Agregar un pokemon extra para el testeo de evolucion
    # Player["team"][-1] = TestEv(Player["team"][-1])

    # print(f"Has agregado a {Player['team'][-1]['name']} con nivel {Player['team'][-1]['exp']} a tu equipo.")
    
    return Player, PokemonData


 
    
def Challenge(PokemonData, Player):
    global LastEnemy #globalizo 

    # Verificar si todos los índices posibles ya han sido utilizados
    if len(LastEnemy) >= 25:  # si supera al limite de enemigos
        print("¡Todos los enemigos han sido desafiados! Reiniciando la lista de enemigos.")
        LastEnemy = []

    # Generar un índice único que no esté en LastEnemy
    while True:
        index = random.randint(0, 25)
        if index not in LastEnemy:
            break

    # Obtener el perfil del enemigo y agregar el índice a la lista
    Enemy = GetEnemyProfile(PokemonData, index)
    Enemy["team"] = RefreshLevelPok(Enemy["team"][0])
    Enemy["team"]["partner"] = "enemy" #Para diferenciar los pokemons capturables de los enemigos

    LastEnemy.append(index)

    print("\nVaya, {} te ha desafiado!!\n".format(Enemy["name"]))
    TrainerCombat(Player, Enemy)
    AddTrainer(Enemy)
    if(PlayerPokemonLives(Player) == False):
        EndGame(1)


def WhoIsPokemon(PokemonData, Player):

    WildPokemon = PokemonData[random.randint(0, len(PokemonData)-1)]
    WildPokemon= RefreshLevelPok(WildPokemon)
    
    WildPokemonCombat(Player, WildPokemon)
    if(PlayerPokemonLives(Player) == False):
        EndGame(1)

def ChoiceAction(PokemonData, Player):
    while True:


        print("\n¿Que deseas hacer?")
        try:
            opcion = int(input("\n1: Batalla con entrenador \t2: Capturar Pokémon \n3: Mochila \t\t\t4: Salir\n").strip())
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")
            continue

        if opcion == 1:  # Batalla con entrenador
            Challenge(PokemonData, Player)

            for Pokemon in Player["team"]:  # Verificar si los pokémon suben de nivel
                Pokemon = CheckLevel(Pokemon)

            Player["objects"] = AddItem(Player["objects"], GetItemRandom()["name"])

        elif opcion == 2:  # Capturar Pokémon
            WhoIsPokemon(PokemonData, Player)

            for Pokemon in Player["team"]: # Verificar si los pokémon suben de nivel
                Pokemon = CheckLevel(Pokemon)


        elif opcion == 3:  # Inventario
            Item = InventoryManagement(Player)
            if Item is not None:
                OcupeItem(Player, None, Item)
            else:
                continue

        elif opcion == 4:  # Salir
            EndGame(0)
            return False

        else:  # Opción inválida
            print("Opción no válida. Intenta de nuevo.")

        ChangeOption(Player)



def ChangeOption(Player):
    choice = ""

    while choice not in ["N", "Y"]:
        print("¿Quieres cambiar el orden del equipo? Y/N")
        choice = input().strip().upper()

        if choice == "Y":
            Change_Pokemon(Player)
            print(f"Tu nuevo primer pokémon es {Player['team'][0]['name']}")
            return
        elif choice == "N":
            return
        else: 
            print("Opción inválida, vuelve a intentarlo.")



def EndGame(option):
    if(option == 0): #No perdiste
        print("Has decidido dejar la aventura hasta aquí.\nDescansas en una posada hasta el proximo día.")
    elif(option == 1): #Derrotado
        print("Todos tus pokémon han sido derrotados, vas directamente hacia el centro pokémon más cercano.")

    PrintHistory()

    print("\n-------------")
    print(f"|{Red} GAME OVER {Default}|")
    print("-------------\n")
    exit()  #Para terminar el juego

    

def GetEnemyInfo(PokemonData): 

    Enemy = []

    for index in enumerate(3):
        Enemy.append(GetEnemyProfile(PokemonData, index))

    print("Vaya, mientras caminabas te topaste con algunas entrenadores por distintos accesos de la ruta.\n ¿Contra cual quieres luchar?")
    i = 0
    for enemy in Enemy:
        print(f"{i}.- {enemy["name"]} con su {enemy["team"][0]["name"]} lvl {enemy["team"][0]["exp"]}")
        i+= 1

    opcion = input("Escoge: ").strip().upper()

    if opcion == 1 or opcion == 2 or opcion == 3:  # Seleccion de enemy a enfrentar
        print(f"Escojes ir por la ruta donde se encuentra {Enemy[opcion-1]["team"][0]["name"]}")
        return Enemy[opcion-1]

    else:  # Opción inválida
        print("Opción no válida. Intenta de nuevo.")

    return
