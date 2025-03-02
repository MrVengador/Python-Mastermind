import os
import random
from PlayerCombat import PlayerAttack, Change_Pokemon, View_Inventory
from EnemyCombat import EnemyAttack
from Pokemon_DB import TablaEfectividad

#Color text
Green = "\033[32m"
Red = "\033[31m"
Default = "\033[0m"  # Restablecer al color por defecto

PokemonInFight = []
FrasesEfectividad = ["¡El ataque no tuvo efecto!","No es muy efectivo...",
"¡Es bastante efectivo!", "¡Es súper efectivo!"]


def Lifes(Player, Enemy):
    # Gengar life
    print(f"{Green}\nLvl: {Player['exp']}  {Player['name']}:{Default}")
    Current_Life = int(Player["current_health"] // 10)  
    Lost_Life = int(Player["base_health"] // 10 - Current_Life)  
    print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, int(Player["current_health"]), int(Player["base_health"])))

    # Pikachu life
    print(f"{Red}\nLvl: {Enemy['exp']}  {Enemy['name']}:{Default}")
    Current_Life = int(Enemy["current_health"] // 10)  
    Lost_Life = int(Enemy["base_health"] // 10 - Current_Life)  
    print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, int(Enemy["current_health"]), int(Enemy["base_health"])))


def PlayerPokemonLives(Player): #Verifica que todos los pokemon del jugador esten con vida (current_health >=0)
    return sum([pokemon["current_health"] for pokemon in Player["team"]]) > 0



# Combate contra entrenador
def TrainerCombat(Player, Enemy):
    print(f"{Enemy['name']} envía a {Enemy['team']['name']} al combate!")
    print(f"\n{Player['name']}: ¡Vamos, {Player['team'][0]['name']}!")
    print(f"{Enemy['team']['name']} - {Enemy['team']['current_health']}")
    
    PokemonInFight.append(Player['team'][0]) # Agregar el primer pokemon del jugador a la lista de pokemons en combate
    
    while PlayerPokemonLives(Player):
        # Turno del jugador
        PlayerTurn(Player, Enemy['team'], True)
        
        if Player['team'][0] not in PokemonInFight: # Para no repetir pokemons en combate
            PokemonInFight.append(Player['team'][0]) # Agregar el pokemon a la lista de pokemons en combate

        # Verificar estados combinados
        if not CheckCombatState(Player, Enemy['team']):
            return  # Termina el combate si las verificaciones fallan
    
        # Turno del enemigo
        EnemyTurn(Player, Enemy['team'])

        if not CheckCombatState(Player, Enemy['team']):
            return
    




def WildPokemonCombat(Player, WildPokemon):
    """Gestiona el combate contra un Pokémon salvaje."""
    print(f"¡Un {WildPokemon["name"]} salvaje apareció!")
    print(f"\n{Player["name"]}: ¡Vamos, {Player["team"][0]["name"]}!")
    print(f"{WildPokemon["name"]} - {WildPokemon["current_health"]}")

    PokemonInFight.append(Player['team'][0]) # Agregar el primer pokemon del jugador a la lista de pokemons en combate

    while PlayerPokemonLives(Player) and WildPokemon["current_health"] > 0:
        # Turno del jugador
        if PlayerTurn(Player, WildPokemon, False) == "Run":
            return # Termina el combate si el jugador huye

        if Player['team'][0] not in PokemonInFight: # Para no repetir pokemons en combate
            PokemonInFight.append(Player['team'][0]) # Agregar el pokemon a la lista de pokemons en combate

        # Verificar estados combinados
        if not CheckCombatState(Player, WildPokemon):
            return  # Termina el combate si las verificaciones fallan

        # Turno del enemigo
        EnemyTurn(Player, WildPokemon)

        if not CheckCombatState(Player, WildPokemon):
            return




def PlayerTurn(Player, Enemy, isTrainerBattle):

    Lifes(Player["team"][0], Enemy)
    while True:
        print(f"Turno de {Player["name"]}") 
        print(f"¿Qué debe hacer {Player["team"][0]["name"]}?\n")

        print("Opciones:")
        print("1.- Atacar\t2.- Cambiar Pokémon\n3.- Objetos\t4.- Huir")

        choice = input("Selecciona una opción (1-4): ")

        if choice == "1":
            print(f"{Player["team"][0]["name"]} se prepara para atacar!")
            
            Attack(Player["team"][0], Enemy, PlayerAttack(Player["team"][0], Enemy))

            return "Attack"

        elif choice == "2":
            print(f"{Player["name"]} decide cambiar de Pokémon.")
            Change_Pokemon(Player)
            return "Change"

        elif choice == "3":
            print(f"{Player["name"]} revisa su inventario.")
            View_Inventory(Player, Enemy)
            return "Inventory"

        elif choice == "4":
            if isTrainerBattle:
                print("No puedes huir de un combate contra un entrenador!")
            else:
                print(f"{Player["name"]} huye del combate.")
                return "Run"

        else:
            os.system("cls")
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 4.")





def EnemyTurn(Player, Enemy):
    Lifes(Player["team"][0], Enemy)
    print(f"Turno de {Enemy["name"]}")
    Attack(Enemy, Player["team"][0], EnemyAttack(Enemy, Player))

    return 

    
def Attack(attacker, target, selected_move):

    print(f"\n{attacker["name"]} ataca a {target["name"]} usando {selected_move["name"]}!")
    multiplicador = AttackType(selected_move["type"], target["type"]) #Multiplicador de efectividad
    damage =  selected_move["damage"] * multiplicador #Daño total del ataque

    target["current_health"] -= damage
    target["current_health"] = max(0, target["current_health"])  # No permitir salud negativa
    #print(multiplicador)
    EfectividadMSG(multiplicador)
    print(f"{target["name"]} recibe {damage} de daño. Vida restante: {target["current_health"]}")
    # Comprobar si el objetivo ha sido derrotado
    if target["current_health"] == 0:
        print(f"¡{target["name"]} ha sido derrotado!")
    
    return 


def AttackType(AttackType, TargetType):
    total_multiplier = 1.0  # Empieza con multiplicador de 1, este aumentara en caso de efectividad

    for target_type in TargetType:        
        # Verifica si los tipos existen en la tabla de efectividad
        if AttackType in TablaEfectividad and target_type in TablaEfectividad[AttackType]:
            multiplier = TablaEfectividad[AttackType][target_type]  # Accede correctamente a la tabla
            total_multiplier *= multiplier # Multiplica la efectivida 1 x ?

    return total_multiplier #Devuelve el daño total

def EfectividadMSG(multiplicador): #Frases por ataque efectivo
    if(multiplicador == 0):
        print(FrasesEfectividad[0]) 
    elif(multiplicador == 0.5):
        print(FrasesEfectividad[1]) 
    elif(multiplicador == 1.5):
        print(FrasesEfectividad[2]) 
    elif(multiplicador >= 2):
        print(FrasesEfectividad[3])


def CheckPlayerPokemon(Player):  #Verifica si el Pokémon del jugador está debilitado y pregunta si quiere continuar. 
    if Player["team"][0]["current_health"] <= 0:
        print(f"\n{Red}{Player["team"][0]["name"]} se ha debilitado.{Default}\n")

        if not PlayerPokemonLives(Player): # Si no tiene Pokémon vivos, termina el combate
            return False  
        
        print("¿Quieres continuar el combate?")
        
        while True:  # Bucle para asegurar una respuesta válida
            ContinueFight = input("Y/N: ").strip().upper()
            if ContinueFight == "Y":
                print("Escoge a tu siguiente Pokémon:")
                Player["team"] = Change_Pokemon(Player)
                return True  # Continuar el combate
            elif ContinueFight == "N":
                print("¡El jugador ha huido del combate!")
                Player["team"] = Change_Pokemon(Player)
                return False  # Finalizar el combate
            else:
                print("Por favor, responde con 'Y' o 'N'.")
    return True  # El Pokémon sigue vivo, continuar el combate



def CheckCombatState(Player, Enemy): #Combina verificaciones del estado del jugador y del oponente.
    if not CheckPlayerPokemon(Player):
        return False  # Termina el combate si el jugador no puede continuar

    if Enemy["current_health"] <= 0:
            return LoseEnemy(Player, Enemy)
    
    if Enemy["partner"] == "Player":
        print(f"¡El jugador capturó a {Enemy["name"]}!")
        return False  # Terminar el combate 

    return True  # Continuar el combate


def LoseEnemy(Player, Enemy): # Si el enemigo perdio
        print("¡El jugador ganó el combate!")

        for pkm in Player["team"]:
            if pkm in PokemonInFight:
                expWin = XP_Win(pkm, Enemy, len(PokemonInFight))
                print(f"{pkm['name']} ha obtenido {expWin} de experiencia.")
                pkm["current_exp"] += expWin

        PokemonInFight.clear()  # Limpiar la lista de pokémon en combate

        
        return False  # Terminar el combate


def XP_Win(Player, Enemy, Divisor):
    # Calcular la diferencia de nivel basada en la experiencia, para mayor claridad
    nivel_diferencia = Enemy["exp"] - Player["exp"]
    
    # Asegurarse de que la diferencia de nivel no sea negativa, al menos 0 (no se pierde experiencia)
    if nivel_diferencia < 0:
        nivel_diferencia = 0
    
    # Base de experiencia y ajuste por diferencia de experiencia
    xp = (Enemy["exp"] * (1 + nivel_diferencia * 0.1)) / Divisor

    return xp
