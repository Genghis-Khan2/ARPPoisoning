import socket

IP_ADDRESS = "127.0.0.1"

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.sendto('Hello', (IP_ADDRESS, 8080))

info = client_socket.recvfrom(1024)

print(info)
