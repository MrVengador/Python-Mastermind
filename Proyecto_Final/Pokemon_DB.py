import json #utilizo json por compatibilidad, y por seguridad, ya que lo he usado con anterioridad anque en C#
import os
import random
from requests_html import HTMLSession

# Ruta proyecto (para gestionar mejor el orden)
script_directory = os.path.dirname(os.path.abspath(__file__))

# Ruta pokefile
file_path = os.path.join(script_directory, "PokemonFile.json") #Se que no es necesario, pero me gusta tenerlo en una variable


Pokedex = []

#DB de base de datos de pokemons
url_pokemons = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk=" #+num pokemon
PokemonBase = {
    "name": "",  
    "pokedex": None, #Numero de pokedex
    "type": None,
    "current_health": 100,
    "base_health": 100,
    "exp": 1,
    "current_exp": 0,
    "movs": None, #array de movs actuales,
    "allmovs": None, #array de todos los movs,
    "partner": "wild", # Default: salvaje
    "evolution": {
        "level": 0,
        "dex": None	
    }
}


def getAttacksPokemon(Pokemon):
    Attacks = []
    # Filtrar los movimientos según la experiencia mínima requerida
    for mov in Pokemon["allmovs"]:
        #print(f"{Pokemon["exp"]} -  {mov["minExp"] }")
        if int(Pokemon["exp"]) > int(mov["minExp"]) -1:  # Verificar que el Pokémon tenga suficiente experiencia
            Attacks.append(mov)

    # Mezclar los ataques si hay más de 3 disponibles
    random.shuffle(Attacks)

    # Retornar hasta un máximo de 4 ataques disponibles
    return Attacks[:4]



def getPokemon(index_pokedex):
    url = "{}{}".format(url_pokemons, index_pokedex)
    session = HTMLSession() 
    PokePage = session.get(url)
    PokeName = PokePage.html.find(".mini", first=True).text.split("\n")[0] 
    Pokemon  = PokemonBase.copy()
    Pokemon["name"] = PokeName
    Pokemon["pokedex"] = index_pokedex
    Pokemon["type"] = []
    Pokemon["evolution"] = None
    Pokemon["num"] = index_pokedex
    print(Pokemon["name"])
    for img in PokePage.html.find(".pkmain", first=True).find(".bordeambos", first = True).find("img"):  # Encontrar todas las imágenes en el contenedor
        Pokemon["type"].append(img.attrs["alt"])

    Pokemon["movs"] = []
    Pokemon["allmovs"] = []

    for AttackItem in PokePage.html.find(".pkmain")[-1].find("tr .check3"): #Hago la busqueda de los ataques (1 generacion con -1)
    
        Attack = {
            "name" : AttackItem.find("td", first= True).find("a",first=True).text, #Cargo el nombre del ataque
            "type" : AttackItem.find("td")[1].find("img", first=True).attrs["alt"], #Cargo el tipo del ataque
            "minExp" : AttackItem.find("th", first=True).text, #Cargo el nivel de obtencion del ataque
            "damage" : int(AttackItem.find("td")[3].text.replace("--","0")), #Cargo el daño del ataque
        }
        if(Attack["minExp"] == ""):
            Attack["minExp"] = "0"

        Pokemon["allmovs"].append(Attack) 
          
    Pokemon["evolution"] = EvolutionDates(PokePage)

    return Pokemon

def getAllPokemons(Total):  # Obtengo los datos de los Pokémon de la 1ra generación
    try:  #S
        print("Cargando los datos de los Pokémon")
        with open(file_path, "r") as PokemonFile:  #r leemos el archivo a cargar
            AllPokemons = json.load(PokemonFile)  # cargamos los datos del json

    except FileNotFoundError:  # De lo contrario, cargamos los datos desde la web
        print("\nERROR, en la carga de base de pokemon.\nCargando los datos de los Pokémon de la web, esto puede tardar un poco.")
        AllPokemons = []
        for index in range(Total):  # Iterar sobre los 151 Pokémon de la 1ra generación
            AllPokemons.append(getPokemon(index + 1))  # Función para obtener datos del Pokémon
            print("*", end="")

        print("\n¡Todos los Pokémon han sido descargados!")

        # Guardamos los datos de los Pokémon en formato JSON
        with open(file_path, "w") as PokemonFile: 
            json.dump(AllPokemons, PokemonFile, indent=4) #w, escribimos los datos de los pokemon importados desde la pag

    Pokedex.extend(AllPokemons) #Agregamos los pokemons a la pokedex (lista de pokemons)

    return AllPokemons


def RefreshLevelPok(Pokemon):
    Pokemon["exp"] = random.randint(1, 100)
    Pokemon["movs"] = getAttacksPokemon(Pokemon) 
    Pokemon["base_health"] =  Pokemon["exp"] * 5 #2 es por ahora, para dar un valor por nivel
    Pokemon["current_health"] = Pokemon["base_health"]

    return Pokemon

def TestEv(Pokemon): # Para testear las evoluciones (iniciales)
    Pokemon["exp"] = 15
    Pokemon["movs"] = getAttacksPokemon(Pokemon) 
    Pokemon["base_health"] =  Pokemon["exp"] * 5 
    Pokemon["current_health"] = Pokemon["base_health"]

    return Pokemon


def NewLevelPok(Pokemon):
    porcentaje = int(Pokemon["base_health"] / Pokemon["current_health"])  # Porcentaje en base al base actual
    Pokemon["base_health"] = int(Pokemon["exp"] * 5)  # Aumenta la vida base
    Pokemon["current_health"] = int(Pokemon["base_health"] * porcentaje)  # Se actualiza la vida actual en base al % que corresponde
    EvPokemon = Evolution(Pokemon, Pokedex)
    #Pokemon = Evolution(Pokemon)  # Verifica si el Pokémon evoluciona


    if(NewMove != None): # Hay un nuevo movimiento
        Pokemon["movs"] = ReplaceAttack(Pokemon)  #Actualiza los ataques ahora que tiene un mayor nivel


def Evolution(Pokemon):
    if(len(Pokemon["evolution"][0]) <= 1): # No tiene evoluciones
        #print("El pokemon no tiene evoluciones")
        return Pokemon

    elif(Pokemon["pokedex"] == Pokemon["evolution"][1][-1]): # Es el último de la cadena evolutiva
        #print(f"{Pokemon["name"]} ha alcanzado su máxima evolución.")
        return Pokemon
        
    else: # Imprimir las evoluciones
        #print(f"El pokemon tiene {len(Pokemon["evolution"][0])-1} evoluciones.")
        for i in range(len(Pokemon["evolution"])):
            pokemonEv = Pokemon["evolution"][1][i]
            nivel = Pokemon["evolution"][0][i]
            
            if("piedra" in nivel):
                #print(f"{Pokemon["name"]} evoluciona usando {nivel} en {Pokemon["evolution"][1][i]}")
                return Pokemon # Crear funcion proximamente
            
            elif("felicidad" in nivel):
                #print(f"{Pokemon["name"]} evoluciona con {nivel} de felicidad en {Pokemon["evolution"][1][i]}")
                return Pokemon # Crear funcion proximamente
            
            else:
                nivel = int(''.join(filter(str.isdigit, nivel))) #Extraer el nivel de evolución
                #print(f"{pokemonEv} - {Pokemon["pokedex"]}")
                if(pokemonEv == Pokemon["pokedex"]):
                    #print(f"{Pokemon["name"]} evoluciona al {nivel} en {PokemonDB[Pokemon["evolution"][1][i]]["name"]}")  # Imprimir los criterios de evolución
                    #print(f"{Pokemon["pokedex"]} evoluciona al {nivel} en {Pokemon["evolution"][1][i+1]}")  # Imprimir los criterios de evolución 
                    return Pokedex[pokemonEv]  # Devolver el Pokémon evolucionado
    return Pokemon


def NewMove(Pokemon):
    # Verifica si el Pokémon tiene la experiencia suficiente para aprender algún ataque
    for move in Pokemon["movs"]:
        if Pokemon["exp"] == int(move["minExp"]):  # Compara la experiencia con la minExp del ataque (Podria repeterse si no lo escoge, pero siento que es trabajo de más)
            return move
    return None

    
def ReplaceAttack(Pokemon, new_move):
    if len(Pokemon["movs"]) >= 4:  # Si el Pokémon tiene 4 o más ataques, pedir al jugador que reemplace uno  
        print(f"{Pokemon['name']} quiere aprender {new_move['name']}")

        # Preguntar al jugador si desea que el Pokémon aprenda el nuevo ataque
        confirm = input(f"¿Quieres que {Pokemon['name']} aprenda {new_move['name']}? (Y/N): ").strip().upper()

        if confirm == "Y":
            
            for i, move in enumerate(Pokemon["movs"]): # Mostrar los ataques actuales
                print(f"{i + 1}: {move['name']}")

            while True: 
                try: 
                    choice = int(input("Selecciona el ataque a reemplazar: ")) - 1 # Solicitar al jugador que seleccione un ataque para reemplazar

                    if choice == -1: # Preguntar si realmente no quiere que el Pokémon aprenda el movimiento
                        confirm = input(f"¿No quieres que {Pokemon['name']} aprenda {new_move['name']}? (Y/N): ").strip().upper()

                        if confirm == "Y":
                            print(f"{Pokemon['name']} no aprenderá {new_move['name']}.")
                            return Pokemon["movs"]
                        elif confirm == "N":
                            continue
                        else:
                            print("Por favor, ingresa una opción válida (Y/N).")

                    elif 0 <= choice < len(Pokemon["movs"]): # El Pokémon olvida el ataque seleccionado y aprende el nuevo
                        print(f"{Pokemon['name']} ha olvidado {Pokemon['movs'][choice]['name']} y ha aprendido {new_move['name']}")
                        Pokemon["movs"][choice] = new_move
                        return Pokemon["movs"]
                    
                    else:
                        print("Selección inválida. Por favor, selecciona un número de ataque válido.")
                except ValueError:
                    print("Por favor, ingresa un número válido.")
        
        elif confirm == "N":
            print(f"{Pokemon['name']} no aprenderá {new_move['name']}.")
            return Pokemon["movs"]
        else:
            print("Por favor, ingresa una respuesta válida (Y/N).")
    else:
        Pokemon["movs"].append(new_move)
        return Pokemon["movs"]
    
    return Pokemon["movs"]


TablaEfectividad = {  # Tabla de efectividad
    
    #Ataque    #Objetivo
    "normal": {"roca": 0.5, "fantasma": 0.0},
    "fuego": {"planta": 2.0, "agua": 0.5, "fuego": 0.5, "roca": 0.5, "bicho": 2.0},
    "agua": {"fuego": 2.0, "roca": 2.0, "planta": 0.5, "agua": 0.5},
    "planta": {"agua": 2.0, "fuego": 0.5, "roca": 2.0, "planta": 0.5, "bicho": 0.5},
    "eléctrico": {"agua": 2.0, "planta": 0.5, "eléctrico": 0.5, "tierra": 0.0, "volador": 2.0},
    "hielo": {"planta": 2.0, "fuego": 0.5, "roca": 0.5, "volador": 2.0, "dragón": 2.0},
    "lucha": {"normal": 2.0, "roca": 2.0, "fantasma": 0.0, "volador": 0.5, "psíquico": 0.5},
    "veneno": {"planta": 2.0, "roca": 0.5, "tierra": 0.5, "fantasma": 0.5},
    "tierra": {"fuego": 2.0, "eléctrico": 2.0, "planta": 0.5, "volador": 0.0, "roca": 2.0},
    "volador": {"planta": 2.0, "roca": 0.5, "eléctrico": 0.5, "bicho": 2.0},
    "psíquico": {"lucha": 2.0, "veneno": 2.0},
    "bicho": {"planta": 2.0, "fuego": 0.5, "lucha": 0.5, "volador": 0.5, "psíquico": 2.0},
    "roca": {"fuego": 2.0, "hielo": 2.0, "volador": 2.0, "planta": 0.5, "tierra": 0.5},
    "fantasma": {"normal": 0.0, "psíquico": 2.0, "fantasma": 2.0},
    "dragón": {"dragón": 2},
}

def EvolutionDates(PokePage):
    elements = PokePage.html.find(".pkmain", first=True).find(".bordeambos")
    # Extraer la lista de evoluciones
    evolution_list = [item.text.strip().split("\n") for item in elements[-1].find("td")]
    evolution_list = list(set([item for sublist in evolution_list for item in sublist if item]))
    evolution_list_sorted = sorted([item for item in evolution_list if "nivel" in item.lower() or "piedra" in item.lower()  
                            or "felicidad" in item.lower() or any(char.isdigit() for char in item)], 
                            key=lambda x: (int(''.join(filter(str.isdigit, x))) if any(char.isdigit() for char in x) else float('inf'), x))
    
    # Extraer las evoluciones que no son por nivel
    ev = [item for item in evolution_list_sorted if "nivel" in item.lower() or "piedra" in item.lower() or "felicidad" in item.lower()]
    # Obtener los índices de la Pokédex de las evoluciones
    IndexPjm = [int(''.join(filter(str.isdigit, item))) for item in evolution_list_sorted if not ("nivel" in item.lower() or "piedra" in item.lower() or "felicidad" in item.lower()) and 0 < int(''.join(filter(str.isdigit, item))) <= 151]

    return ev, IndexPjm # Devolver la lista de evoluciones y los índices de la Pokédex
