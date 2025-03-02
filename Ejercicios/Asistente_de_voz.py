from datetime import datetime
import pyttsx3
import speech_recognition as sr
import re

Asistence_name = "Alfred"
User_Name = "Vengador"

def Create_Save_file(Path): #Para concervar variables como el nombre del usuario u otras variables relevantes

    File = open(Path + "Save_File_Assistence", "w")
    return File



def Actually_hour():
    # Obtener la hora actual
    hora_actual = datetime.now().hour

    # Determinar el saludo
    if (6 <= hora_actual < 12):
        saludo = "Buenos días"
    elif (12 <= hora_actual < 21):
        saludo = "Buenas tardes"
    else:
        saludo = "Buenas noches"

    return saludo 

def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z}]+)", "mi nombre es ([A-Za-z}]+)", "llamame ([A-Za-z}]+)", "^([A-Za-z}]+)$"]
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
        except IndexError:
            print("No me ha dicho su nombre...")

    return name
        

engine = pyttsx3.init()

engine.setProperty("rate",120)
engine.setProperty("voice", "spanish")

mensaje = Actually_hour() + ", espero se encuentre bien."
engine.say(mensaje)
engine.runAndWait()

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Puedes hablar")
    engine.say("¿Cómo puedo ayudarle hoy?")
    engine.runAndWait()
    audio = r.listen(source)
    text = r.recognize_google(audio, language ="ES-CL")
    print(text)
    
    if ("hora actual" in text.lower()):
        mensaje = f"Son las {datetime.now().hour} con {datetime.now().minute}."
        engine.say(mensaje)
        engine.runAndWait()

    elif("te llamas" in text.lower() or "tu nombre" in text.lower()):
        mensaje = "Mi nombre es: " + Asistence_name
        engine.say(mensaje)
        engine.runAndWait()

    elif("me llamo" in text.lower() or "mi nombre" in text.lower()):
        mensaje = "Su nombre es: " + User_Name
        engine.say(mensaje)
        engine.runAndWait()

    elif("di" in text.lower() or "repite" in text.lower()):
        mensaje = text #Eliminar el primer di o repite
        engine.say(mensaje)
        engine.runAndWait()

    elif("liset" in text.lower() or "lisett" in text.lower() or "sobrina" in text.lower()):
        mensaje = "Hola Lisett, soy el computador de tú tío. Dice que te crees gato, ¿Quieres que busque lugares donde puedas encontrar un ratón para comer? jajaja, es broma. Cuidate."
        engine.say(mensaje)
        engine.runAndWait()

    # elif("cambiar nombre" in text.lower()):
    #     new_Name = re.findall("Me llamo ([A-Za-z}]+)", text) #en caso de ser invitado o de
    #     User_Name = new_Name


    engine.say("Necesita alguna otra cosa {}?".format(User_Name))
    engine.runAndWait()


    audio = r.listen(source)
    text = r.recognize_google(audio, language ="ES-CL")
    print(text)
            
    if ("descansa" in text.lower() or "apágate" in text.lower() or "no gracias" in text.lower() or text == " No"):
        mensaje = "Desactivando sistema {}, es un honor servirle {}".format(Asistence_name, User_Name)
        engine.say(mensaje)
        engine.runAndWait()
