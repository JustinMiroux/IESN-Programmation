import concurrent.futures
from socket import socket, AF_INET, SOCK_STREAM

def request(domain, port, i):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((domain, port))
    client_socket.send(f"Message n°{i}".encode())
    response = client_socket.recv(1024).decode()
    #print(f"Response received : {response}")
    return f"Response received : {response}"

def main():
    domain = "localhost"
    port = 5000

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=100)
    futures = []

    for i in range(100):
        #threading.Thread(target=request, args=[domain, port, i]).start()
        future = executor.submit(request, domain, port, i)
        futures.append(future)

    print("Task submitted")

    for future in concurrent.futures.as_completed(futures):
        print(future.result())

    print("Finished")

main()
