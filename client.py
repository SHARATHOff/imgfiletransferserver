from email.mime import image
from re import L
import socket , time , sys

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host = input('enter the code : ')
host = '192.168.44.1'
port = 8080
c.connect((host,port))
print('trying to connect')
fileaname = input('enter the fullpath of the file : ')
imagefile = open('{}'.format(fileaname),'rb')
imageread = imagefile.read(2048)
while imageread:
    c.send(imageread)
    imageread = imagefile.read(2048)
imagefile.close()
c.close()