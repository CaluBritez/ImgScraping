import requests
from bs4 import BeautifulSoup
import os

url = "https://www.tiendafuencarral.com.ar/"

response = requests.get(url)

def filtrar_imagenes(lista_img):
    extensiones_validas = ('.png', '.jpg', '.webp')
    lista_filtrada = []
    for img in lista_img:
        if img is not None and img.endswith(extensiones_validas):
            lista_filtrada.append(img)
    
    return lista_filtrada

def crear_carpeta(carpeta):
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

def descargar_imagenes(lista_img, carpeta):
    for i, img_url in enumerate(lista_img):
        try:
            response = requests.get(img_url)
            if response.status_code == 200:
                nombre_imagen = os.path.join(carpeta, f"imagen_{i + 1}.{img_url.split('.')[-1]}")
                with open(nombre_imagen, 'wb') as file:
                    file.write(response.content)
                print(f"Imagen descargada: {nombre_imagen}")
            else:
                print(f"Error al descargar {img_url}: Status code {response.status_code}")
        except Exception as e:
            print(f"Error al descargar {img_url}: {e}")

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find_all('img')
    lista_img = [link.get('src') for link in links]

    lista_img_filtrada = filtrar_imagenes(lista_img)
    print(lista_img_filtrada)

    carpeta_imagenes = 'imagenes'
    crear_carpeta(carpeta_imagenes)
    descargar_imagenes(lista_img_filtrada, carpeta_imagenes)


