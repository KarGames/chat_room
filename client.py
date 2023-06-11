import socket
import threading
import sys

c = socket.socket()
host = socket.gethostname()
port = 5050

name = input("enter username: ")

c.connect((host, port))
c.send(name.encode('utf-8'))
print(c.recv(1024).decode('utf-8'))

def message(msg):
    msg = f"{name}: {msg}".encode('utf-8')
    c.send(msg)

def recv_message():
    while True:
        recv_msg = c.recv(1024).decode('utf-8')
        print(f"{recv_msg}\n")

recv_message = threading.Thread(target=recv_message)
recv_message.start()

try:
    while True:
        msg = input("")
        message(msg)
        if msg.lower() == "disconnect":
            print(f"Have a good day {name}")
            c.close()
            sys.exit(0)
except KeyboardInterrupt:
    c.close()