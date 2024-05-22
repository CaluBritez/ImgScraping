# Web Scraping para obtención de imágenes

Este proyecto realiza una Web Scraping para obtener las imagenes de algún sitio web, en este caso utilizamos la web de venta de ropa "Tienda Fuencarral".
Obtenemos las URLs de las imágenes y las descargamos en una carpeta local llamada "imagenes". Nos aseguramos de que la carpeta imagenes exista, y si no, automáticamente se crea una. Solo se descargan imágenes con las extensiones .png, .jpg, y .webp.

## Pasos para ejecutar el proyecto

En primera instancia se debe clonar el repositorio. En línea de comandos escribimos:

```
git clone https://github.com/CaluBritez/ImgScraping.git
```
Accedemos a la carpeta correspondiente con:
```
cd actscrapingimg
```
Luego debemos instalar las dependencia utilizadas de la siguiente forma:
```
pip install requests beautifulsoup4
```
Por último ejecutamos el proyecto:
```
python index.py
```
Si todo funciona correctamente, podremos apreciar las imagenes descargadas en una carpeta llamada "imagenes" en nuestro ordenador local.

## Cambiar Web de descargas

Si deseamos realizar las descargas de las imagenes en otra página web, debemos cambiar la variable llamada **url** en nuestro archivo index.py, colocando el nombre correspondiente de la nueva página a trabajar.

