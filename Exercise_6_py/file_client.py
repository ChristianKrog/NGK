import sys
import socket 
from lib import Lib

HOST = '10.0.0.2'
PORT = 80
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
	clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientSock.connect((HOST,PORT))

	userInput = raw_input("Please enter a valid filename: ")
	Lib.writeTextTCP(userInput,clientSock)
	Lib.getFileSizeTCP(clientSock)

#def receiveFile(fileName,  conn):
	# TO DO Your Code

if __name__ == "__main__":
   main(sys.argv[1:])
