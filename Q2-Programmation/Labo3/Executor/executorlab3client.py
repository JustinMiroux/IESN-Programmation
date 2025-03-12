import concurrent.futures
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:

        for i in range(100):
            executor.submit(request, domain, port, i)
        print("Task submitted")

    print("Finished")

main()