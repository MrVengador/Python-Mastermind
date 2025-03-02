import pyttsx3
import speech_recognition as sr

# Inicializar el motor de texto a voz
engine = pyttsx3.init()
engine.setProperty("rate", 150)
engine.setProperty("voice", "spanish")

def speak(message):
    """Reproducir un mensaje de texto usando el motor de voz."""
    engine.say(message)
    engine.runAndWait()


def listen():
    """Escuchar al usuario y transcribir la entrada de voz."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Puedes hablar.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="ES-CL")
            return text.lower()
        except sr.UnknownValueError:
            speak("No entendí, ¿podría repetirlo?")
            return None
        except sr.RequestError:
            speak("Lo siento, no puedo acceder al reconocimiento de voz en este momento.")
            return None


