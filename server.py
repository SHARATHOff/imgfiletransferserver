
import socket , time , sys , pickle

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
host = socket.gethostbyname(host)
print(host ,' is the code ')
port = 8080
s.bind((host,port))
s.listen()
c , addr = s.accept()
print('server has connected to ',addr)
imagefile = open('new.jpg','wb')
image_chuck = c.recv(2048)
while image_chuck:
    imagefile.write(image_chuck)
  #  image_chuck = c.recv(2048)
imagefile.close()
c.close