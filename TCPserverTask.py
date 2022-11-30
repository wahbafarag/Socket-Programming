# TCP Server

from socket import *
serverIP = '127.0.0.1'
serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
print ('The server is ready to receive')
while True:
     
     connectionSocket, addr = serverSocket.accept()
     serverInfo = serverIP + "," + str(serverPort)
     print('Server Connected To: {} {!r}'.format("", addr))
     condition = 1
     while condition == 1:
         sentence = connectionSocket.recv(1024).decode()
         if sentence == 'Exit' or sentence == 'exit' :
             print('Received Message from Client :' + sentence)
             condition = 0
         else:
             sentenceLen = str(len(sentence))
             prntSenLen = 'Your data was' + sentenceLen +'bytes'
             print('Received Message from Client :' + sentence)
             connectionSocket.send(prntSenLen.encode())
     
     
     
     connectionSocket.send('Disconnect'.encode())
     print("Reply Sent, Server Socket Closed , Goodbye")
     connectionSocket.close()
