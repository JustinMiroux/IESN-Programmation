import threading
from socket import socket, AF_INET, SOCK_STREAM

def request(domain, port, i):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((domain, port))
    client_socket.send(f"Message n°{i}".encode())
    response = client_socket.recv(1024).decode()
    print(f"Response received : {response}")

def main():
    domain = "localhost"
    port = 5000
    for i in range(100):
        threading.Thread(target=request, args=[domain, port, i]).start()

main()

