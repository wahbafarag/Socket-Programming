# TCP Client 

from socket import *
serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverIP,serverPort))
condition = 1
while condition == 1:
    sentence = input('Input lowercase sentence or exit to close:')
    if sentence == 'exit':
        condition = 0
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print ('From Server:', modifiedSentence.decode())
        print ('You Disconnected, Goodbye')
        clientSocket.close()
    else :
        clientSocket.send(sentence.encode())
        modifiedSentence = clientSocket.recv(1024)
        print('From Server:', modifiedSentence.decode())
