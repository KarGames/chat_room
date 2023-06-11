import socket
import threading

s = socket.socket()
host = socket.gethostname()
port = 5050

s.bind((host, port))
s.listen(10)

clientList = []
clients = len(clientList)

def checkClient():
    while True:
       client, address = s.accept()
       name = client.recv(1024).decode('utf-8')
       print(f"{name} has joined the server")
       client.send("Connected".encode('utf-8'))
       clientList.append(client)
       threading.Thread(target=recv_message, args=(client, )).start()
       print(f"TOTAL CLIENTS {len(clientList)}")
        
clientCheck = threading.Thread(target=checkClient)
clientCheck.start()

def recv_message(client):
    while True:
        msg = client.recv(1024).decode('utf-8')
        
        for send_client in clientList:
            if client != send_client:
                send_client.send(msg.encode('utf-8'))
        print(msg)
        if msg.lower()[int(msg.find(":"))+2:] == "disconnect":
            clientList.remove(client)
            print(f"TOTAL CLIENTS: {len(clientList)}")
            break