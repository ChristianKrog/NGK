import sys
from socket import *
from lib import Lib

PORT = 9000
BUFSIZE = 1000
serverName = 'clientTCP'

def main(argv):
	# TO DO Your Code
	clientSock = socket(AF_INET, SOCK_STREAM)
	clientSock.connect((serverName,PORT))

	userInput = raw_input("Please enter a valid filename: ")
	Lib.writeTextTCP(userInput,clientSock)
	Lib.getFileSizeTCP(clientSock)


    
#def receiveFile(fileName,  conn):
	# TO DO Your Code


if __name__ == "__main__":
   main(sys.argv[1:])
