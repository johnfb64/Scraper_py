import requests
from bs4 import BeautifulSoup

# Hacer una solicitud HTTP a la página web
url = "https://picsum.photos/"
response = requests.get(url)

# Analizar el contenido HTML de la página web
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar todas las imágenes en la página
images = soup.find_all("img")

# Recorrer todas las imágenes y descargarlas
for i, image in enumerate(images):
    img_url = image["src"]
    img_response = requests.get(img_url)
    with open("image_{}.jpg".format(i), "wb") as f:
        f.write(img_response.content)