from threading import Thread
import socket

def Send(socket):
    while True:
        msg = input('->')
        msg= msg.encode('utf-8')
        socket.send(msg)
def Reception(socket):
    while True:
        data = socket.recv(500)
        data = data.decode("utf-8")
        print(data)
        

host, port = ("192.168.1.11", 10100)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))

envoi = Thread(target=Send, args=[socket])
reception = Thread(target=Reception, args=[socket])
    
envoi.start()
reception.start()