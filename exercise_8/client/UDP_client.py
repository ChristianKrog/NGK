import sys
from socket import * 

HOST = '10.0.0.1' #server IP
PORT = 9000
serverAddr= (HOST, PORT)
BUF = 1024

def main(argv):
	clientSock = socket(AF_INET, SOCK_DGRAM) #create UDP socket

	while True: 
		print 'Please enter a "S": '
		input1 = raw_input() #get input from terminal 

		if input1 == 'S':
			clientSock.sendto(input1, serverAddr) #Sends the terminal input to server 

		data = clientSock.recvfrom(BUF) #receive message from server
		print data[0] 

		
    
if __name__ == "__main__":
   main(sys.argv[1:])

