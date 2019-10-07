import sys
from socket import * 
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
serverAddr= (HOST, PORT)
BUF = 1024

def main(argv):
	# TO DO Your Code
	serverClient = socket(AF_INET, SOCK_DGRAM)

	while True: 
		print 'Please enter a valid letter ("U", "u" , "L" or "l")'
		input1 = input()
		serverClient.sendto(input1, serverAddr)
		data = serverClient.recvfrom(BUF)
		print data
    
if __name__ == "__main__":
   main(sys.argv[1:])