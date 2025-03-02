from Voz_Assistence import listen, speak
from datetime import datetime
import re
from Sniper_bot_Steam import Search_Game_Steam, Sniper_steam_bot_Price, First_Game_Steam_relevant, Date_to_spanish


# Variables globales
Asistence_name = "Alfred"


def identify_name(text):
    """Identificar el nombre del usuario a partir del texto."""
    patterns = [
        "me llamo ([A-Za-z]+)",
        "mi nombre es ([A-Za-z]+)",
        "llámame ([A-Za-z]+)",
        "^([A-Za-z]+)$"
    ]
    for pattern in patterns:
        match = re.findall(pattern, text)
        if match:
            return match[0]
    return None


def respond_to_query(query, session):
    """Responder a la consulta del usuario."""
    global User_Name

    if "hora actual" in query:
        mensaje = f"Son las {datetime.now().hour} con {datetime.now().minute}."
        speak(mensaje)

    elif "te llamas" in query or "tu nombre" in query:
        mensaje = "Mi nombre es: " + Asistence_name
        speak(mensaje)

    elif "me llamo" in query or "mi nombre" in query:
        name = identify_name(query)
        if name:
            User_Name = name
            mensaje = f"Mucho gusto, {User_Name}. Guardaré tu nombre."
        else:
            mensaje = "No entendí tu nombre, por favor repítelo."
        speak(mensaje)

    elif "di" in query or "repite" in query:
        mensaje = query.replace("di ", "").replace("repite ", "")
        speak(mensaje)

    elif "liset" in query or "lisett" in query or "sobrina" in query:
        mensaje = (
            "Hola Lisett, soy el computador de tu tío. Dice que te crees gato, "
            "¿quieres que busque lugares donde puedas encontrar un ratón para comer? Jajaja, es broma. Cuídate."
        )
        speak(mensaje)

    elif "descansa" in query or "apágate" in query or "no gracias" in query or "nada" in query or query == "no":
        mensaje = f"Desactivando sistema, {Asistence_name}."
        speak(mensaje)
        return False
    elif "busca en steam" in query or ("steam" in query and "el juego" in query or "un juego" in query):
        
        game = None
        while game is None:
            mensaje = "Diga el nombre del juego a buscar, por favor."
            speak(mensaje)
            game = listen()
            print(game)

            if game:
                if "cancelar" in game:
                    speak("Búsqueda cancelada.")
                    break

                speak(f"Buscando el juego {game} en Steam...")
                if Search_Game_Steam(game, session):
                    break
                else:
                    speak(f"No se encontraron juegos relacionados a {game}, intenta nuevamente.")
                    game = None

            else:
                speak("No entendí el nombre del juego. ¿Podrías repetirlo?")
                
    return True
