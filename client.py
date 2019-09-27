from socket import *
import sys

#host to connect to
h = sys.argv[1]
#port to connect to 
p = int(sys.argv[2])

#setup socket and connect to it
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((h,p))

#send the message to server
#file name arg should be in format: "/home.html", "/test/home.html", etc.
message = 'GET ' + sys.argv[3] + ' HTTP/1.1\r\n\r\n'
clientSocket.send(message.encode())

recievedMessage = ""
while True:
	#get response
	data = clientSocket.recv(2048)
	#check if server is done sending responses
	if(len(data) == 0):
		break;
	#append message
	recievedMessage = recievedMessage + data.decode('ascii')

print('RECIEVED RESPONSE:')
print(recievedMessage)
clientSocket.close()
