# Republishing copyrighted information is not allowed
# Violating terms of service is not allowed
# robots.txt to know more about it

from bs4 import BeautifulSoup
import urllib.request

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
# création d'un objet soup
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))


