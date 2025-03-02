from GameManager import Welcome, ChoiceAction

# Ejecución principal del programa
if __name__ == "__main__":
    # Llamamos a la función principal para inicializar el programa
    Player, PokemonData = Welcome()
    ChoiceAction(PokemonData, Player)