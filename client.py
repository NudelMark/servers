import socket
import serial
 
client = socket.socket()            # создаем сокет клиента
hostname = "127.0.0.1"   # получаем хост локальной машины
port = 12345                        # устанавливаем порт сервера
client.connect((hostname, port))  
ser = serial.Serial("/dev/ttyUSB0" , 9600)
serdata = ser.readline()

while True:# подключаемся к серверу
    data = client.recv(1024)            # получаем данные с сервера
    if data.decode()=="GPS":
        print("GPS:" , serdata)
    elif not data:
        break
