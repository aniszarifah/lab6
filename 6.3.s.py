#Python program for simple calculation
import socket
import sys
import time
import errno
import os
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode('Welcome to the Server\n'))
    while True:
        data = s_sock.recv(2048)
        print(data)
        if not data:
            break
        s_sock.sendall(str.encode(ok_message))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

     except:
         #Function to add two numbers
         def add(num1, num2):
             return num1 + num2

         #Function to substract two numbers
         def substract(num1, num2):
             return num1 -num2

         #Function to multiply two numbers
         def multiply(num1, num2):
             return num1 * num2

         #Function to divide two numbers
         def divide(num1, num2):
             return num1 / num2

         #Take input from the user
         if select == 1:
            print(number_1, "+", number_2, "=",
                            add(number_1, number-2))

         elif select == 2:
              print(number_1, "-", number_2, "=",
                              substract(number_1, number_2))

         elif select == 3:
              print(number_1, "*", number_2, "=",
                              multiply(number_1, number_2))

         elif select == 4:
              print(number_1, "/", number_2, "=",
                              divide(number_1, number_2))

         else:
              print("Invalid input")

    except Exception as e:
print('an exception occurred!')
        	print(e)
        	sys.exit(1)
    finally:
     	   s.close()

