#MOCHILA
import random


def InventoryManagement(Player): #
    Inventary = Player["objects"] # Tomamos los objetos del jugador

    msg = ["Selecciona el número del objeto a ocupar: ", "Selecciona el número del objeto a tirar: "]
    print("\n--- Tu mochila ---")
    AvaibleItems = ViewInventary(Inventary) # Pasamos los items individualmente en una lista

    while True:
        choice = int(input("\nElige qué hacer: \n1. Usar un objeto \n2. Botar un objeto \n3. Salir\n"))  # Elegir acción

        if choice == 1 or choice == 2:
            print(msg[choice - 1])

            item = SelectItem(AvaibleItems, choice)  # Devuelvo el ítem seleccionado

            if item is None:  # Se seleccionó salir en selección de ítem
                print("Volviendo a la mochila.")
                continue  # Vuelvo a preguntar

            if choice == 2:
                confirmation = input(f"¿Estás seguro que quieres eliminar {item['name']}? Y/N: ").strip().lower()
                if confirmation == "y":
                    RemoveItem(Player["objects"], item["name"], "tirado")
                    print(f"El objeto {item['name']} ha sido eliminado.")
                else:
                    print("Eliminación cancelada.")
                continue  

            else:  # Caso para choice == 1
                return item

        elif choice == 3:  # Salir del bucle y del programa
            print("Saliendo del menú...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.") 

        
def ViewInventary(Inventary):
    index = 1
    AvaibleItems = []  # Para guardar el nombre y usarlo posteriormente

    for category, items in Inventary.items():
        # Verificar si hay algún ítem con cantidad > 0 en la categoría
        if any(item["cantidad"] > 0 for item in items):
            print(f"\n*{category}*")
            for item in items:
                if item["cantidad"] > 0:
                    print(f"{index}.- {item['cantidad']} x {item['name']}")
                    AvaibleItems.append(item)
                    index += 1
    return AvaibleItems


def SelectItem(AvaibleItems, action): #Selecciono el item a ocupar
    if(AvaibleItems):
                try:
                    choice = int(input()) - 1
                    #print(f" Objetos {AvaibleItems}")
                    #Ocupar el objeto
                    if(0 <= choice < len(AvaibleItems) and action == 1):
                        return AvaibleItems[choice]#RemoveItem(Inventary, AvaibleItems[choice]["name"], "ocupado")
                        
                    #Tirar objeto
                    elif (0 <= choice < len(AvaibleItems) and action == 2): #Revisa si es una opcion valida entre 0 y la cantidad de items disponibles
                        return AvaibleItems[choice]#RemoveItem(Inventary, AvaibleItems[choice]["name"], "tirado")
                    
                    #Salir
                    elif -1:
                        print("No escoges ningun objeto.")
                        return None

                    else:
                        print("Selección inválida")
                        
                    
                except (ValueError, IndexError):
                    print("Selección inválida.")


def OcupeItem(Player, Enemy, item):  # Uso de item
    
    if("posión" in item["name"]): #El objeto se usara en un pokémon aliado
        print(f"Selecciona con quien deseas usar {item["name"]}")
        UseIteminTeam(Player, item)
        RemoveItem(Player["objects"], item["name"],"usaste") 

    elif("ball" in item["name"] and Enemy != None and Enemy["partner"] == "wild"): #El objeto se usara en un pokémon enemigo salvaje
        print(f"Usas {item["name"]} en {Enemy["name"]}")
        newPok = UsePokeball(item, Enemy)
        RemoveItem(Player["objects"], item["name"],"usaste") 

        if(newPok != None):
            Player["team"].append(newPok)
            print(f"{newPok["name"]} se ha unido a tu equipo.") # quizas limitar a 6 pkm y el resto a pc? (evaluar, quizas innecesario por ahora)


    else:
        print("ERROR, intente nuevamente.")



def AddItem(Inventary, name):
    for category, items in Inventary.items():
        for item in items:
            if(item["name"] == name):
                print(f"Has agregado el objeto {item["name"]} a tu mochila.\n")
                item["cantidad"] +=1
                return Inventary


def RemoveItem(Inventary, name, use): #use es para variar la palabra, usaste x, botaste x 
    for category, items in Inventary.items():
        for item in items:
            if(item["name"] == name):
                print(f"Has {use} el objeto {item["name"]} de tu mochila.\n")
                item["cantidad"] -=1
                return Inventary



def UseIteminTeam(Player, item): #Uso de objeto para el equipo
    i = 1
    for pokemon in Player["team"]:
        print(f"{i}.- {pokemon["name"]}")
        i+=1
    
    while True:
        choice = int(input()) - 1  #se escoge el pokemón a elegir

        if(0 <= choice < len(Player["team"]) and Player["team"][choice]["current_health"] < Player["team"][choice]["base_health"] and Player["team"][choice]["current_health"] > 0):
            print(f"Curar a {Player["team"][choice]["name"]}") 
            HealthPokemon(Player["team"][choice], item["health"])
            return Player["objects"]
        
        elif(Player["team"][choice]["current_health"] == Player["team"][choice]["base_health"]):
            print(f"No puedes curar a {Player["team"][choice]["name"]}, ya que su vida esta completa.") 

        elif(Player["team"][choice]["current_health"] == 0):
            print(f"No puedes curar a {Player["team"][choice]["name"]}, ya que esta noqueado.") 


        else:
            print("Escoje una opción valida.")


def UsePokeball(item, Target):
    
    Captura = random.randint(1, 100) 
    print(f"¡Lanzas una {item['name']} a {Target["name"]}!")

    if Captura <= item["percent"]:  # Si Captura esta dentro del rango del % de la pokeball se captura
        print(f"¡Éxito! {Target['name']} ha sido capturado.")
        Target["partner"] = "Player"  # Asigna el pokémon al jugador
        HealthPokemon(Target, Target["base_health"])  # Cura al pokémon capturado
        return Target
    else:
        print(f"¡Oh no! {Target['name']} escapó de la {item['name']}...")
        return None  # Falla la captura

def HealthPokemon(Pokemon, Health):
    Pokemon["current_health"] = min(Pokemon["current_health"] + Health, Pokemon["base_health"]) # Limito la curación para que no supere base health
    return Pokemon

