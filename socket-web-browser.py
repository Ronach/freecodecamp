import socket

# http://www.dr-chuck.com/page1.html (protocol//host/document)
# ce script constitue la partie cliente qui se connecte au serveur
# pour faire tourner un serveur en local : "py -m htttp.server"
# Flow client = .socket() .connect() .encode() .send() .recv() .decode() .close()
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET=IPv4, AF_INET6=IPv6, SOCK_STREAM= TCP, SOCK_DGRAM= UDP
mysocket.connect(("data.pr4e.org", 80))
# \n = newline ou line feed/LF (aller à la ligne) 99% du temps & /r = cariage return (revenir à gauche)
# in Unix and all Unix-like systems, \n is the code for end-of-line, \r means nothing special
# in Windows (and many old OSs), the code for end of line is 2 characters, \r\n, in this order
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
mysocket.close()
# ASCII (128) --> Unicode (billions). UTF-8 has a dynamic length between 1 (equivalent to ASCII) and 4 bytes



