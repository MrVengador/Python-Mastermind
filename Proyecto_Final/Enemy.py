import random


EnemyNames = [
    "Rocío", "Maca", "Javier", "Alexander", "Miriam", "Ricardo", "Sai", "Juanito", "Matias", "Juanka",
    "Liam", "Emma", "Noah", "Sophia", "Oliver", 
    "Isabella", "Elijah", "Mia", "James", "Charlotte", 
    "Benjamin", "Amelia", "Lucas", "Harper", "Henry"
]

#Comienza batalla
EnemyFrase0 = [
    "¡Prepárate para perder!", "¿Crees que puedes vencerme?", "¡Tu aventura termina aquí!",
    "¡No tienes oportunidad contra mí!", "¡Vamos a luchar, valiente entrenador!", 
    "¡Esta será tu derrota más humillante!", "¡Nunca he perdido, no empezaré ahora!", 
    "¡Demuestra lo que sabes hacer!", "¿De verdad quieres enfrentarte a mí?", 
    "¡Eres valiente, pero no lo suficiente!", "¡Entrenadores como tú no me asustan!", 
    "¡Hoy haré historia venciendo a otro rival!", "¡Mis Pokémon son imparables!", 
    "¡Voy a demostrarte el verdadero poder!", "¡El perdedor aquí serás tú!"
]

#Enemigo pierde
EnemyFrase1 = [
    "¡No puede ser! ¡He perdido!", "¡Esto no ha terminado!", "¡Tendré mi revancha!", 
    "¡Mis Pokémon necesitan más entrenamiento!", "¡Eres más fuerte de lo que esperaba!", 
    "¡Tuvimos mala suerte, pero volveremos más fuertes!", "¡Hoy ganaste, pero no siempre será así!", 
    "¡La próxima vez seré invencible!", "¡Mis Pokémon hicieron su mejor esfuerzo!", 
    "¡No lo creo, me derrotaste!", "¡Esto es una derrota temporal!", 
    "¡Me atrapaste desprevenido!", "¡Buena batalla, lo admito!", 
    "¡Esto no es el final de mi camino!", "¡Mis Pokémon lo intentaron con todo!"
]

#Enemigo gana
EnemyFrase2 = [
    "¡Te lo dije, soy invencible!", "¡Sabía que ganaría!", "¡No eras rival para mí!", 
    "¡Fue fácil derrotarte!", "¡Mis Pokémon son los mejores!", 
    "¡Esto fue demasiado sencillo!", "¡Aprende de esta derrota!", 
    "¡Nunca dudes de mi poder!", "¡Mis estrategias siempre ganan!", 
    "¡La victoria es nuestra!", "¡Así es como se lucha!", 
    "¡Mis Pokémon están en otro nivel!", "¡Vuelve cuando seas más fuerte!", 
    "¡No tienes lo necesario para vencerme!", "¡Soy el mejor entrenador de todos!"
]




def GetEnemyProfile(PokemonList, EnemyIndex):
    return {
    "name" : EnemyNames[EnemyIndex],
    "team": [random.choice(PokemonList)],  # Escoge un pokémon aleatorio
    "objects" : None,
    "combats" : 0,
    "money": random.randint(500, 5000), # Dinero aleatorio entre 500 y 5000
        "frases": {
            "inicio": random.choice(EnemyFrase0),  # Frase para el inicio del enfrentamiento
            "derrota": random.choice(EnemyFrase1),  # Frase para cuando pierde
            "victoria": random.choice(EnemyFrase2)  # Frase para cuando gana
        },
}


