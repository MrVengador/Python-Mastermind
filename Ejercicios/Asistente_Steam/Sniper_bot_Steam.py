from datetime import datetime
from Voz_Assistence import listen, speak
import requests
from io import BytesIO
from PIL import Image

# Funciones relacionadas con Steam
def Date_to_spanish(date):
    """Convertir una fecha en inglés al formato español."""
    meses_en_espanol = {
        "Jan": "enero",
        "Feb": "febrero",
        "Mar": "marzo",
        "Apr": "abril",
        "May": "mayo",
        "Jun": "junio",
        "Jul": "julio",
        "Aug": "agosto",
        "Sep": "septiembre",
        "Oct": "octubre",
        "Nov": "noviembre",
        "Dec": "diciembre"
    }

    if not date:
        return "Fecha no proporcionada"

    try:
        date_obj = datetime.strptime(date, "%d %b, %Y")
        mes_abreviado = date_obj.strftime("%b")
        mes_en_espanol = meses_en_espanol.get(mes_abreviado, mes_abreviado)
        formatted_date = date_obj.strftime(f"%d de {mes_en_espanol} del %Y")
        return formatted_date

    except ValueError:
        return "Formato de fecha no válido"

def Show_Img(url):
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image.show(title="Imagen de prueba")  # Muestra la imagen


    except Exception as e:
        print(f"Error al cargar la imagen: {e}")

def First_Game_Steam_relevant(Game_dates):
    # Eliminar el símbolo de moneda y convertir el precio a un formato limpio
    Game_dates[1] = Game_dates[1].replace("CLP$", "").strip()    
    Game_dates[2] = Date_to_spanish(Game_dates[2]) 

    msj = f"El juego más relacionado con el nombre proporcionado es {Game_dates[0]}, con un precio de {Game_dates[1]} pesos chilenos. Su fecha de lanzamiento es {Game_dates[2]}."
    msj += " Se mostrarán en la consola la información más relevante de este y otros juegos, incluyendo títulos y precios."
    speak(msj)

def Search_Game_Steam(Name, session):
    # Modifica Name para que los espacios se reemplacen por '+'
    formatted_name = Name.replace(" ", "+")
    print("Buscando:", formatted_name)

    

    # Realizar solicitud GET para obtener el HTML de la página de búsqueda
    url = f"https://store.steampowered.com/search/?term={formatted_name}&supportedlang=latam%2Cspanish&ndl=1"
    r = session.get(url)

    # Buscar el contenedor de resultados de juegos
    avaible_game = r.html.find('#search_resultsRows', first=True)

    if avaible_game:
    # Buscar todas las filas de resultados
        game_items = avaible_game.find('.search_result_row')
        print(f"Se han encontrado {len(game_items)} juegos relacionados a {Name}")
    
        for i, game in enumerate(game_items):
            # Extraer datos clave del hijo
            title_element = game.find('.title', first=True)
            title = title_element.text if title_element else "No disponible"
            
            url = game.attrs.get('href', "No disponible")
            
            release_date_element = game.find('.search_released', first=True)
            release_date = release_date_element.text if release_date_element else "No disponible"
            
            price_element = game.find('.search_price_discount_combined .discount_final_price', first=True)
            price = price_element.text if price_element else "No disponible"

             

            if(i == 0):
                game_date = [title, price, release_date]
                First_Game_Steam_relevant(game_date)
                # Obtener la URL de la imagen
                img_element = game.find('img', first=True)
                img_url = img_element.attrs['src'] if img_element else "No disponible"
                Show_Img(img_url)


            elif(i >= 10):
                break

            # Imprimir información del juego
            print(" ")


            print(f"Título: {title}")
            print(f"URL: {url}")
            print(f"Fecha de Lanzamiento: {release_date}")
            print(f"Precio: {price}")
            print(f"Imagen: {img_url}\n\n")

            
    else:
        print("No se encontraron juegos.")
        return False

    return True

def Sniper_steam_bot_Price(url, session):
    
    r = session.get(url)

    price_element = r.html.find('div.game_purchase_price.price', first=True)
    game_name = r.html.find('#appHubAppName', first=True)
    game_name = game_name.text if game_name else "Nombre no disponible"




    if price_element:
        if 'data-price-final' in price_element.attrs:
            price = price_element.attrs['data-price-final']
            print(f"El precio de {game_name} es: {price}")
        elif 'Free' in price_element.text:
            print(f"{game_name} es gratuito.")
        else:
            print(f"El precio de {game_name} no está disponible, pero el texto dice: {price_element.text}")
    else:
        print("No se encontró el elemento del precio.")

# Ejemplo de URLs de juegos
url_Marvel_Rivals = "https://store.steampowered.com/app/2767030/Marvel_Rivals/"
url_Spiderman_Miles = "https://store.steampowered.com/app/1817190/Marvels_SpiderMan_Miles_Morales/"
url_Resident_Evil_4_RE = "https://store.steampowered.com/app/2050650/Resident_Evil_4/"

