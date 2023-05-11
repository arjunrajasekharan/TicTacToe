
import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

HOST = get_ip_address()
PORT = '8080'

while True:
    # Press `CTRL + C` to exit client

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, int(PORT)))

    message = input('\nEnter Message : ')
    client_socket.send(message.encode('utf-8'))

    # print(client_socket.recv(1024).decode('utf-8'))
    client_socket.close()
