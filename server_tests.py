import os
import sys
import socket
import threading

port = 1953

def handler(connection):
    global message
    global filelist
    filelist = []
    file = connection.makefile()
    file.flush()
    filelist.append(file)
    message = ''
    while 1:
        i = 0
        while i < (len(filelist)):
            filelist[i].flush()
            temp = filelist[i].readline()

            if temp == 'quit':
                break

            with lock:
                message += temp

            i = i + 1
    file.close()

global lock
acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
acceptor.bind(('', port))
acceptor.listen(10)
lock = threading.allocate_lock()

while 1:
    connection, addr = acceptor.accept()
    threading.start_new_thread(handler, (connection,))

"""
import select, socket, sys, threading

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    client.send(response)
                else:
                    raise ValueError('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    port_num = input("Port? ")
    port_num = int(port_num)
    ThreadedServer('',port_num).listen()




"""


