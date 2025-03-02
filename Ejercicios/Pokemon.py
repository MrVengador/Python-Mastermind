from random import randint
from os import system

Max_Health_Pikachu = 100
Max_Health_Gengar = 100

Life_Pikachu = Max_Health_Pikachu
Life_Gengar = Max_Health_Gengar


Damage_Attack = 0

while Life_Pikachu > 0 and Life_Gengar > 0:
    # Si uno muere, se van de aquí

    # Gengar life
    print("\nGengar:")
    Current_Life = Life_Gengar // 5
    Lost_Life = Max_Health_Gengar // 5 - Current_Life
    print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, Life_Gengar, Max_Health_Gengar))

    # Pikachu life
    print("Pikachu:")
    Current_Life = Life_Pikachu // 5
    Lost_Life = Max_Health_Pikachu // 5 - Current_Life
    print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, Life_Pikachu, Max_Health_Pikachu))


    #Pikachu Turno
    print("\nTurno de Pikachu \n")

    Attack_Pikachu = randint(1,3)

    if(Attack_Pikachu == 1):

        print("Pikachu usa Bola voltio")
        Damage_Attack= 15

    elif(Attack_Pikachu == 2):
         
         print("Pikachu usa Placaje")
         Damage_Attack= 10

    else:

        print("Pikachu usa Impactrueno")
        Damage_Attack= 20


    Life_Gengar-= Damage_Attack
    print("Gengar pierde {} de vida, vida actual {}.".format(Damage_Attack, Life_Gengar))
    Damage_Attack = 0
    input()
    system('cls')

    #Gengar Turno
    print("\nTurno de Gengar \n")
    Attack_Gengar = None

    # Gengar life
    print("\nGengar:")
    Current_Life = Life_Gengar // 5
    Lost_Life = Max_Health_Gengar // 5 - Current_Life
    print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, Life_Gengar, Max_Health_Gengar))

    # Pikachu life
    print("Pikachu:")
    Current_Life = Life_Pikachu // 5
    Lost_Life = Max_Health_Pikachu // 5 - Current_Life
    print("{}{} [{}/{}]".format("🟩" * Current_Life, "⬛" * Lost_Life, Life_Pikachu, Max_Health_Pikachu))


    if(Life_Gengar > 0):
        while Attack_Gengar != 1 and  Attack_Gengar != 2 and Attack_Gengar != 3:

            Attack_Gengar = int(input("Ataques disponibles:\n[1] Placaje \t[2] Bola Sombra \n[3] Arañazo \n"))

            print("Turno de Gengar")

            if(Attack_Gengar == 1):
                print("Gengar usa Placaje")
                Damage_Attack = 5

            elif Attack_Gengar == 2:
                print("Gengar usa Bola sombra")
                Damage_Attack = 20

            elif Attack_Gengar == 3:
                print("Gengar usa Arañazo")
                Damage_Attack = 10
            else:
                system('cls')

        Life_Pikachu-= Damage_Attack
        print("Pikachu pierde {} de vida, vida actual {}.".format(Damage_Attack, Life_Pikachu))
        Damage_Attack = 0
    
if(Life_Pikachu > 0):
    print("Pikachu es el ganador")

elif(Life_Gengar > 0):
    print("Gengar es el ganador")
        

print("Fin del juego")



