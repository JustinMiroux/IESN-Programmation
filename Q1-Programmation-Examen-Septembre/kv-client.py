from sys import argv
from socket import socket, AF_INET, SOCK_STREAM

def menu():
    print("===================")
    print("Send a request :")
    print("1) PUT")
    print("2) GET")
    print("3) DELETE")
    return input("Choice :")

def get_key():
    return input("Key? ")

def get_value():
    return input("Value? ")

def put_request():
    key = get_key()
    value = get_value()
    request = f"PUT {key} {value}"
    client_socket = send(request)

def get_request():
    key = get_key()
    request = f"GET {key}"
    client_socket = send(request)
    response = client_socket.recv(1024).decode()
    print(response)

def delete_request():
    key = get_key()
    request = f"DELETE {key}"
    client_socket = send(request)
    response = client_socket.recv(1024).decode()
    print(response)

def send(request):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((ip, int(port)))
    sock.send(request.encode())
    return sock

ip = argv[1]
port = argv[2]

while True:
    choice = menu()
    if choice == "1":
        put_request()
    elif choice == "2":
        get_request()
    elif choice == "3":
        delete_request()
