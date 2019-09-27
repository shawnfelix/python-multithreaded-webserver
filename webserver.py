# Shawn A. Felix
# SID: 109316150
# NID: safelix

#import socket module
from socket import *
import threading
import sys # In order to terminate the program
 
def main():
	#af_inet = ipv4 addresses
	#sock_stream = TCP connection
	serverSocket = socket(AF_INET, SOCK_STREAM)

	#Prepare a sever socket
	host = gethostname()
	port = 2345
	serverSocket.bind((host, port))
	print("[server ip(type into browser):", gethostbyname(getfqdn()), "]")
	print("[server port:", port,"]")

	serverSocket.listen(5)
	print("[server listening]")

	while True:
		#Establish the connection
		print('Ready to serve...')
		connectionSocket, addr = serverSocket.accept()
		th = threading.Thread(target=threads, args=(connectionSocket,addr,))
		th.start()

	serverSocket.close()

def threads(connectionSocket, address):
	try:
		print("Recieved at (" + address[0] + ")\n")
		message = connectionSocket.recv(2048)
		filename = message.split()[1]
		print(filename)
		f = open(filename[1:])
		outputdata = f.read()
		#Send one HTTP header line into socket
		connectionSocket.send('HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=ISO-8859-1\r\n\r\n'.encode());
		#Fill in start
		#Fill in end
		#Send the content of the requested file to the client
		for i in range(0, len(outputdata)):
			connectionSocket.send(outputdata[i].encode())
		connectionSocket.send("\r\n".encode())
		connectionSocket.close()
	except IOError:
		print("Client requested file not found: 404")
		#Send response message for file not found
		connectionSocket.send('HTTP/1.1 404 Not Found\r\n'.encode())
		connectionSocket.send('Content-Type: text/html\r\n\r\n'.encode())
		connectionSocket.send('<html><body><h1>404: Not Found</h1></body></html>'.encode())
		#Close client socket
		connectionSocket.close()
#	sys.exit()#Terminate the program after sending the corresponding data 

if __name__ == "__main__":
	main()