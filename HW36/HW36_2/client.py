import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 20002  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as massage:
    massage.connect((HOST, PORT))
    massage.sendall(b"Hello, world")
    massage.sendall(b"5")
    data = massage.recv(2048)

print("Received", repr(data.decode()))
