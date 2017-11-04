import socket
import os

TCP_IP = 'localhost'
TCP_PORT = 8000
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(10)

while True:
    conn, address = s.accept()
    data = conn.recv(BUFFER_SIZE)
    request = data.split('\r\n',1)[0].split(' ')[1]

    if address == "/about/aboutme.html":
        file = open("/home/lisa/Documents/"+address, mode = 'r')
        conn.send("""HTTP/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read()) 
	file.close() 

    if address == "/index.html" or "/":
        file = open("/home/lisa/Documents/index.html", mode = 'r')
	conn.send("""HTTP/1.1 200 OK \n Content type:text HTML\n\n\n """ + file.read())  
	file.close()
			
conn.close()
s.close()
