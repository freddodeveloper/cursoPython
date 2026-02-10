import requests
from bs4 import BeautifulSoup


def obtener_noticias_python():
    url = "https://www.python.org/"

    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        soup = BeautifulSoup(respuesta.text, 'html.parser')

        print(f"--- Noticias extraídas de {url} ---")

        seccion_noticias = soup.find('div', class_='blog-widget')

        if seccion_noticias:
            lista_items = seccion_noticias.find_all('li')

            for item in lista_items:
                titulo = item.find('a').get_text()
                fecha = item.find('time').get_text()

                print(f"[{fecha}] {titulo}")
        else:
            print("No se encontró la sección de noticias.")

    else:
        print(f"Error al cargar la página: {respuesta.status_code}")


if __name__ == "__main__":
    obtener_noticias_python()
