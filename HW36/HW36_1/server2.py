import socket

# Create a UDP socket
UDPServersock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address_port = ('localhost', 20002)
msgFromServer = "Hello UPD Client"
bytesToSend = str.encode(msgFromServer)
print('starting up on {} port {}'.format(*server_address_port))
UDPServersock.bind(server_address_port)

print("UDP server up and listening")

while(True):

    bytesAddressPair = UDPServersock.recvfrom(1024)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    print(clientMsg)
    print(clientIP)
    # Sending a reply to client
    UDPServersock.sendto(bytesToSend, address)
