# Shawn A. Felix
# SID: 109316150
# NID: safelix


#import socket module
from socket import *
import sys # In order to terminate the program

#af_inet = ipv4 addresses
#sock_stream = TCP connection
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
host = ""
port = 80
serverSocket.bind((host, port))
print("[server ip:", gethostbyname(getfqdn()), "]")
print("[server port:", port,"]")

serverSocket.listen(5)
print("[server listening]")

while True:
	#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	try:
		print("recieved")
		message = connectionSocket.revc()
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = []
		#Send one HTTP header line into socket
		#Fill in start
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
			connectionSocket.send("\r\n".encode())
			connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#Fill in start 
		print('HTTP/1.1 404 Not Found\r\n')
		print('Content-Type: text/html\r\n\r\n')
		print('<html><head></head><body><h1>404 Not Found</h1></body></html>')
#Fill in end
#Close client socket
#Fill in start
#Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data 