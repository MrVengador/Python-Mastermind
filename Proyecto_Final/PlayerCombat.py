from Items import InventoryManagement, OcupeItem
from Pokemon_DB import Evolution

# Ejemplo de implementación de las funciones auxiliares (simplificadas):
def PlayerAttack(Player, Enemy):
    print("\nMovimientos disponibles:")
    for idx, move in enumerate(Player["movs"], start=1):
        print(f"{idx}. {move["name"]} (Daño: {move["damage"]})")

    while True:
        try:
            # Elegir un movimiento
            indexAttack = int(input(f"Selecciona un movimiento (1-{len(Player["movs"])}): ")) - 1
            if 0 <= indexAttack < len(Player["movs"]):
                return  Player["movs"][indexAttack]
            
            else:
                print(f"Opción no válida. Selecciona un número entre 1 y {len(Player["movs"])}.")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número válido.")


def Change_Pokemon(Player):
    print("\nPokémon disponibles:")
    for i, pokemon in enumerate(Player["team"]):
        status = "KO" if pokemon["current_health"] <= 0 else "OK"# Si estan muertos, no estan disponibles
        print(f"{i + 1}.- {pokemon["name"]} (Salud: {pokemon["current_health"]}/{pokemon["base_health"]}, Estado: {status})")

    while True:
        try:
            choice = int(input("Selecciona un Pokémon para cambiar (1-{}): ".format(len(Player["team"])))) - 1

            if 0 <= choice < len(Player["team"]):
                selected_pokemon = Player["team"][choice]
                if selected_pokemon["current_health"] > 0:
                    # Cambiar el Pokémon seleccionado al frente
                    Player["team"][0], Player["team"][choice] = Player["team"][choice], Player["team"][0]
                    print(f"{selected_pokemon["name"]} ahora está al frente del combate.")
                    return Player["team"]
                else:
                    print(f"{selected_pokemon["name"]} no puede combatir porque está debilitado.")
            else:
                print("Opción no válida. Selecciona un Pokémon entre 1 y 3.")
        except ValueError:
            print("Entrada inválida. Introduce un número entre 1 y 3.")



def View_Inventory(Player, Enemy):
    Item = InventoryManagement(Player)
    if(Item != None):
        OcupeItem(Player, Enemy, Item)


def CheckLevel(Pokemon):
    if(Pokemon["current_exp"] >= 100 and Pokemon["exp"] < 100):
        Pokemon["current_exp"] -= 100
        Pokemon["exp"] +=1
        print(f"{Pokemon["name"]} ha subido de nivel!!")
        NewPokemon = Evolution(Pokemon)

        if(NewPokemon != Pokemon): #Actualizar los datos del pokemon evolucionado
            confirm = input(f"{Pokemon["name"]} va a evolucionar!!! \nConfirma si deseas que evolucione.(Y/N)") #Preguntar si se desea evolucionar
            if(confirm == "Y"):
                print(f"{Pokemon["name"]} ha evolucionado a {NewPokemon["name"]}!!!")
                Pokemon["name"] = NewPokemon["name"]	
                Pokemon["pokedex"] = NewPokemon["pokedex"]
                Pokemon["type"] = NewPokemon["type"]
                Pokemon["allmovs"] = NewPokemon["allmovs"]
                Pokemon["evolution"] = NewPokemon["evolution"]

            elif(confirm == "N"):
                print(f"{Pokemon["name"]} no evolucionó.")
            else:
                print("Opción no válida.")
        
    
    return Pokemon
        


