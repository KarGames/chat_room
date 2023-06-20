import socket
import threading

s = socket.socket()
host = socket.gethostname()
port = 7979

s.bind((host, port))
s.listen(10)

clientList = []
client_name = {}
name_client = {}
clients = len(clientList)

def checkClient():
    while True:
       client, address = s.accept()
       name = client.recv(1024).decode('utf-8')
       client_name[client] = str(name)
       name_client[str(name)] = client
       print(f"{name} has joined the server")
       client.send("Connected, /p for Private Messaging".encode('utf-8'))
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
                if msg.lower()[int(msg.find(":"))+2:int(msg.find(":")+4)] == "/p":
                    print("client str: " + msg.lower()[int(msg.find(":"))+5:int(msg.find(")"))])
                    if msg.lower()[int(msg.find(":"))+5:int(msg.find(")"))] == client_name[send_client].lower():
                        name_client[client_name[send_client]].send(msg.encode('utf-8'))
                        break
                
                send_client.send(msg.encode('utf-8'))
        if msg.lower()[int(msg.find(":"))+2:] == "disconnect":
            clientList.remove(client)
        
            print(f"TOTAL CLIENTS: {len(clientList)}")
            break