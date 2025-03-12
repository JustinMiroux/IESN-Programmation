import concurrent.futures
import time
from socket import socket, AF_INET, SOCK_STREAM

def serve(domain, port):
    with socket(AF_INET, SOCK_STREAM) as server_socket:
        server_socket.bind((domain, port))
        server_socket.listen()
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=10)
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            #threading.Thread(target=handle_request, args=[client_socket]).start()
            executor.submit(handle_request, client_socket)
        

def handle_request(client_socket: socket):
    request = client_socket.recv(1024).decode()
    print(f"Request received : {request}")
    time.sleep(1)
    client_socket.send(request.encode())
    client_socket.close()

def main():
    domain = "localhost"
    port = 5000
    serve(domain, port)

main()