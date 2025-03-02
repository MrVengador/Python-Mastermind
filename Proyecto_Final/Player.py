import random

# Inventario como diccionario 
Mochila = {
    "Posiones": [ 
        {"name": "posión", "health": 20, "cantidad": 1},
        {"name": "superposión", "health": 50, "cantidad": 0},
        {"name": "hyperposión", "health": 100, "cantidad": 0}
    ],
    "Pokeballs": [
        {"name": "pokeball", "percent": 10, "cantidad": 1},
        {"name": "superball", "percent": 30, "cantidad": 0},
        {"name": "ultraball", "percent": 50, "cantidad": 10}
    ]
} # Evaluar si agregar objetos de evolución (piedras, etc)

def GetPlayerProfile(PokemonList):
    return {
    "name" : input("¿Cúal es tu nombre? "),
    "team" : [random.choice(PokemonList) for Pokemon in range(3)], # Escoge un pokemon random (3 pokemon)
    "objects" : Mochila.copy(),
    "combats" : 0,
    "money" : 1000,
    }


def GetItemRandom():
    
    category = random.choice(list(Mochila.keys())) # Selecciona una categoria aleatoria
    item = random.choice(Mochila[category])  # Selecciona un ítem aleatorio dentro de la categoria

    print(f"\nHas obtenido {item['name']}.")
    return item