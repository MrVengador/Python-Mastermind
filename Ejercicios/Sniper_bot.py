from time import sleep
from requests_html import HTMLSession

# URLs de ejemplo
url1 = "https://www.solotodo.cl/products/253373-kingston-nv3-1-tb-snv3s1000g"  # debería tener stock
url2 = "https://www.solotodo.cl/products/75693-msi-mag-forge-100r"          # no tiene stock

def Sniper_bot(url):
    session = HTMLSession()
    sleep(5)  # Pausar 5 segundos antes de reintentar

    while True:
        try:
            print(f"\nVerificando stock en {url}")

            # Realizar solicitud GET para obtener el HTML de la página
            r = session.get(url)

            # Buscar el elemento <p> con la clase específica que indica "Producto no disponible"
            stock_element = r.html.find("MuiTypography-root MuiTypography-body1 css-4r64qm", first=True)

            if stock_element:
                # Si encontramos el elemento, significa que el producto no tiene stock
                print("Producto no disponible actualmente.")
                break
            else:
                # Si no existe el elemento, significa que el producto está disponible
                print("¡El producto está disponible!")
                break

        except Exception as e:
            print(f"Error al acceder a la página {url}: {e}")


def Sniper_bot2(url):
    session = HTMLSession()

    while True:
        try:
            print(f"\nVerificando stock en {url}")

            # Realizar solicitud GET para obtener el HTML de la página
            r = session.get(url)

            # Buscar el mensaje específico dentro del HTML
            if 'Este producto no está disponible actualmente' in r.text:
                print("Producto no disponible actualmente.")
                break
            else:
                print("¡El producto está disponible!")
                break

        except Exception as e:
            print(f"Error al acceder a la página {url}: {e}")

        sleep(5)  # Pausar 5 segundos antes de reintentar

# Ejecutar el script para ambas URLs
Sniper_bot(url1)
Sniper_bot(url2)
