import sys
from socket import * 

HOST = '10.0.0.1' #server IP
PORT = 9000 
serverAddr= (HOST, PORT) 
BUF = 1024

def main(argv):
	serverSock = socket(AF_INET, SOCK_DGRAM) #create UDP socket
	serverSock.bind(serverAddr) #bind socket to the serveraddress 

	while True:
		print 'The server is ready to receive'
		data = serverSock.recvfrom(BUF) #Waiting for client to send something. 
		mesClient = data[0] #extract message (letter)
		clientAddr = data[1] #extract clientaddress. 
		print 'Letter: "' + mesClient +'" received from client with address: ' + format(clientAddr)

		if mesClient !=:
			serverSock.sendto('Hej UDP-Client', clientAddr) #send content
			print 'Message sent'
    
if __name__ == "__main__":
   main(sys.argv[1:])

   