
# Lista para almacenar los entrenadores derrotados
TrainersDerrotados = []

PokemonDerrotados = [] #salvajes

def AddTrainer(Trainer):
    TrainersDerrotados.append(Trainer)

def AddPokemon(Pokemon):
    PokemonDerrotados.append(Pokemon)



def PrintHistory(): #Imprimir historial
    print("\n*Historial de combates*\n")
    print("Entrenadores derrotados:\n")
    for index, trainer in enumerate(TrainersDerrotados, start=1):
        print(f"{index}. {trainer['name']} - {trainer['team']['name']}")

    print("\nPokémon salvajes derrotados:\n")
    for index, pokemon in enumerate(PokemonDerrotados, start=1):
        print(f"{index}. {pokemon['name']} - {pokemon['level']}") 


