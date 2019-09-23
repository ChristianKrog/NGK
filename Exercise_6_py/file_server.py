import sys
import socket
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
	serverSock = socket(AF_INET, SOCK_STREAM)
	serverSock.bind((HOST,PORT))
	serverSock.listen(1)6
	print 'The server is ready to receive'
	conn, addr = serverSock.accept()

	txtClient = Lib.readTextTCP(serverSock)
	
	size = Lib.check_File_Exist(txtClient)

	Lib.writeTextTCP(size, serverSock)

def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code

    
if __name__ == "__main__":
   main(sys.argv[1:])
