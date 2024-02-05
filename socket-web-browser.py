# http://www.dr-chuck.com/page1.html (protocol//host/document)
import socket
# Commencer par faire tourner un serveur en local : "py -m htttp.server"
# Ce script constitue est la partie cliente
# Flow client = .socket() -> .connect() -> .encode() -> .send() -> .recv() -> .decode() -> .close()

# AF_INET=IPv4, AF_INET6=IPv6, SOCK_STREAM= TCP, SOCK_DGRAM= UDP
# Création de la socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connection au serveur (local ou ici data.pr4e.org)
mysocket.connect(("data.pr4e.org", 80))

# \n = newline ou line feed /LF (aller à la ligne) 99% du temps
# \r = cariage return (revenir à gauche)
# In Unix and all Unix-like systems, \n is the code for end-of-line, \r means nothing special
# In Windows - and many old OS - the code for end of line is 2 characters : \r\n  In this order

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# On envoit la requête GET du fichier romeo.txt au serveur
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysocket.close()

# ASCII (128 caractères)
# Unicode (des milliards de caractères)
# UTF-8 has a dynamic length between 1 and 4 bytes ( 256 et 4294967296 caractères)



