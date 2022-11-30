# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:06:36 2022

@author: S.A
"""

from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("This message: ", message.decode(), "\n", "is received from: ", clientAddress)