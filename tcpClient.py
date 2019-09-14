from socket import *

def run_client():
    server_name = 'localhost' #can be an IP address
    server_port = 3070
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_name, server_port))
    sentence = input("Input lowercase sentence: ")
    bytes_sent = client_socket.send(sentence.encode())
    modified_sentence = client_socket.recv(1024)
    print("From Server:", modified_sentence.decode())
    client_socket.close()
    
if __name__ == "__main__":
    run_client()