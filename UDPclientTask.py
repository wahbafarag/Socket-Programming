# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:05:13 2022

@author: S.A
"""

from socket import *
import sys
port = sys.argv[1]
p = int(port)
message = sys.argv[2]
serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.bind(('', p))
clientSocket.sendto(message.encode(), (serverIP, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage.decode())

clientSocket.close()
message = input('please enter to exit')