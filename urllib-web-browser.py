# Permet de faire la même chose que socket-web-browser.py en encore plus concis
import urllib.request
import urllib.parse
import urllib.error

# urlopen here "eats" the header
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
