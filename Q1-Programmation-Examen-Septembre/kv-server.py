"""
My Server File for the Exam of september for Programmation Q1.
"""

import sys
import os

from threading import *
from socket import *

class KVServer:
    """
    The main class running in the background
    """

    def __init__(self, ip, port):
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind((ip, int(port)))
        self.server_socket.listen()
        self.lock = Lock()


    def listen_loop(self):
        """
        Listens for a connection and start handle client in a thread for each client
        """

        while True:
            client_socket, client_address = self.server_socket.accept()
            Thread(target=self.handle_client, args=[client_socket]).start()


    def handle_client(self, client_socket):
        """
        Get the data from the client and start the management class with each
        object in the data.slpit()
        """

        data = client_socket.recv(1024).decode()
        while data:

            self.lock.acquire()
            data_list = data.split()

            if len(data_list) == 2:
                data_list.append(None)
            else:
                pass

            start_manage = Management(data_list[0], data_list[1], data_list[2])
            answer = start_manage.check_request()

            if answer is not None:
                client_socket.send(answer.encode())
            else:
                pass

            self.lock.release()
            data = client_socket.recv(1024).decode()

        client_socket.close()


class Management:
    """
    Class used for processing the request and manupilating files
    """

    def __init__(self, request, key, value):
        self.request = request
        self.key = key
        self.value = value


    def check_request(self):
        """
        Check wich request the client sent
        """
        if self.request == "PUT":
            self.create_new()
        elif self.request == "GET":
            val = self.get_exist()
            return val
        elif self.request == "DELETE":
            val = self.delete_exist()
            return val


    def create_new(self):
        """
        Creat/modify the file named self.key with self.value
        """

        file = open(self.key, "w")
        file.write(self.value)
        file.close()


    def get_exist(self):
        """
        Check for an existing file:
            - if exist : open the file name self.key and return it's value with VALUE in front
            - if not exist : return NOVALUE
        """

        if os.path.exists(self.key):
            file = open(self.key, "r")
            value = "VALUE "+file.read()
            file.close()
        else:
            value = "NOVALUE"
        return value


    def delete_exist(self):
        """
        Check for an existing file:
            - if exist : open the file name self.key and return it's value with VALUE in front
                         and deletes the file named self.key afterwards
            - if not exist : return NOKEY
        """

        if os.path.exists(self.key):
            file = open(self.key, "r")
            value = "VALUE "+file.read()
            file.close()
            os.remove(self.key)
        else:
            value = "NOKEY"
        return value


server = KVServer(sys.argv[1], sys.argv[2])
server.listen_loop()
