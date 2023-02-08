import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://parascrapear.com/')
soup = BeautifulSoup(r.text, 'html.parser')

blockquote_items = soup.find_all('blockquote')
for blockquote in blockquote_items:
    autor = blockquote.find(class_ = 'author').text
    categoria = blockquote.find(class_ = 'cat').text
    frase = blockquote.find('q').text

    print([autor, categoria, frase])