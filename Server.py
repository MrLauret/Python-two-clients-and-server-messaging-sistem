import socket
import threading

TheIP = ("127.0.0.1", 1025)
Server = socket.create_server(TheIP)

Clients = {}

def ClientDataManager(ClientIs):
    SendedDataTimes = 0


    while True:
        ClientData = ClientIs.recv(4096).decode()

        if SendedDataTimes == 0:
            TalkingTo = ClientData
        elif SendedDataTimes == 1:
            Username = ClientData
            global Clients

            Clients[Username] = {
                "ClientSocket": ClientIs
            }


        elif SendedDataTimes > 1:
            try:
                TargetSocket = Clients[TalkingTo]["ClientSocket"]
                TargetSocket.send(ClientData.encode())
            except KeyError:
                print(f"Can't find {TalkingTo}")
            

        SendedDataTimes += 1


def ServerAccept():
    global ClientSocket 
    global ClientAdrress

    while True:
        try:
            ClientSocket, ClientAdrress = Server.accept()
            threading.Thread(target=ClientDataManager, args=(ClientSocket,), daemon=True).start()
        except Exception as e:
            print("Server error:", e)


ServerThread = threading.Thread(target=ServerAccept, daemon=False)
ServerThread.start()
print("Server is online")