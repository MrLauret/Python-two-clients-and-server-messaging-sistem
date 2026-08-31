import socket
import threading

TheIP = ("127.0.0.1", 1025)
ClientSocket = socket.socket()
ClientSocket.connect(TheIP)

TalkTo = input("Who do you want to contact? (1/2) ").encode()
ClientSocket.send(TalkTo)

Username = input("Username: ").encode()
ClientSocket.send(Username)

def Sending():
    while True:
        Mensaje = input().encode()
        ClientSocket.send(Mensaje)



def Recibing():
    while True:
        Mensaje = ClientSocket.recv(4096).decode()
        print(f"They said: {Mensaje}")



SendingThread = threading.Thread(target=Sending, daemon=False)
RecibingThread = threading.Thread(target=Recibing, daemon=False)

SendingThread.start()
RecibingThread.start()
