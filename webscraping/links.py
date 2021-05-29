import requests
from bs4 import BeautifulSoup
import cv2

response = requests.get('https://www.luci-lua.tk/')

print ('Status: ', response.status_code)

content = response.content

site = BeautifulSoup(content, 'html.parser')

print(site.prettify())

# tag, atributo
rl = site.find('div', attrs={'class': 'left'})

p = rl.find('p')
h1 = rl.find('h1')
 
print(h1.text ,p.text)

projetos = site.findAll('div', attrs={'class': 'btn-h'})

title = site.findAll('a', attrs={'class': 'acc'})

for title in title:
   print(title.text,':',title['href'])