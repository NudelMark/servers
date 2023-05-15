import socket 
import threading

LOCALHOST = "127.0.0.1"
PORT = 1488

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)

server.bind((LOCALHOST , PORT))
print("Сервер запущен")


class ClientThread(threading.Thread):
    def __init__(self,clientAddres , clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("новое подключение:" , clientAddres)


    def run(self):
        msg = ""
    
        while True:
            data = self.csocket.recv(4096)
            msg = data.decode()
            print(msg)
            if msg == '':
                print("Оключение")
                break
            
            elif msg == "GPS":
                self.csocket.send(bytes("Марк нудель самый гениальный человек на планете" , "UTF-8"))

while True:
    server.listen(1)
    clientsock , clientAddres = server.accept()
    newthread = ClientThread(clientAddres , clientsock)
    newthread.start()