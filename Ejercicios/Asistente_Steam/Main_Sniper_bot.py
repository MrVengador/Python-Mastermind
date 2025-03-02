from datetime import datetime
import pyttsx3
import speech_recognition as sr
from requests_html import HTMLSession
from datetime import datetime
from Voz_Assistence import listen, speak
from Sniper_bot_Steam import Search_Game_Steam, Sniper_steam_bot_Price, First_Game_Steam_relevant, Date_to_spanish
from Assistence_questions import identify_name, respond_to_query




def actually_hour():
    """Determinar un saludo basado en la hora actual."""
    hora_actual = datetime.now().hour
    if 6 <= hora_actual < 12:
        saludo = "Buenos días"
    elif 12 <= hora_actual < 21:
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"
    return saludo



def main():
    # Crear una sesión HTML
    session = HTMLSession()
    """Función principal del asistente."""
    saludo = actually_hour()
    speak(saludo + ", espero se encuentre bien.")

    running = True
    while running:
        speak("¿Cómo puedo ayudarle?")
        query = listen()
        print(query)
        if query:
            running = respond_to_query(query, session)


if __name__ == "__main__":
    main()

    
