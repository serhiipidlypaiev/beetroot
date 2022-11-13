import socket
from caesar_encrypt import caesar_encrypt

# Create a UDP socket
UDPServersock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address_port = ("localhost", 20002)
print("starting up on {} port {}".format(*server_address_port))
UDPServersock.bind(server_address_port)

print("UDP server up and listening")

while True:

    bytesAddressPair = UDPServersock.recvfrom(1024)
    bytesAddressPair2 = UDPServersock.recvfrom(1024)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    message2 = bytesAddressPair2[0]
    address2 = bytesAddressPair2[1]

    clientMsg = message.decode()
    clientMsg2 = int(message2.decode())
    encrypt_message = caesar_encrypt(clientMsg, clientMsg2)
    clientIP = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # Sending a reply to client
    UDPServersock.sendto(str.encode("".join(str(e) for e in encrypt_message)), address)
