import sys
from socket import *
from lib import Lib


HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000


def main(argv):
	fileName = sys.argv[1]
	clientSock = socket(AF_INET, SOCK_STREAM)
	clientSock.connect((HOST,PORT))

	print("Connected to server")

	Lib.writeTextTCP(fileName,clientSock)
	
	receiveFile(fileName, clientSock)

def receiveFile(fileName,  conn):
	fileSize = Lib.getFileSizeTCP(conn)
	if fileSize == 0:
		print("Filesize is 0. File doesn't exist")
		conn.close()
	else:
		print 'Filesize is: ', fileSize
		print("Starting download")

	f = open("fileName", "wb")
	receivedData = conn.recv(BUFSIZE) 
	f.write(receivedData)
	receivedTotal = len(receivedData)
		
	while receivedTotal < fileSize:
		receivedData = conn.recv(BUFSIZE) 
		f.write(receivedData)
		receivedTotal += len(receivedData)	
	
	print("Dowload completed. Client will close")
	conn.close()
		
if __name__ == "__main__":
   main(sys.argv[1:])
