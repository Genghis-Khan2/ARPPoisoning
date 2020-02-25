import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 8080))

(info, client_address) = server_socket.recvfrom(1024)
server_socket.sendto(info, client_address)

server_socket.close()