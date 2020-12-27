import socket
import os
import multiprocessing

ClientSocket = socket.socket()
host = '192.168.24.7'
port = 8888

print("Please select operation -\n" \
             "1. Add\n" \
             "2. Subtract\n" \
             "3. Multiply\n" \
             "4. Divide\n" )
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response)
while True:
    select = int(input("Select operations form 1, 2, 3, 4 :"))
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()




