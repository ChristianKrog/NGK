import sys
import socket
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
	serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serverSock.bind((HOST,PORT))
	serverSock.listen(1)
	print 'The server is ready to receive'
	
	while True 
		conn, addr = serverSock.accept()
		print 'Connected to clint - Port - ', PORT
		txtClient = Lib.readTextTCP(conn)
		fileSize = Lib.check_File_Exist(txtClient)
		Lib.writeTextTCP(fileSize, conn)
		if fileSize != 0
			conn.sendFile()


def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
	f = open(fileName, 'rb')
	l = f.read(BUFSIZE)
	while(l)
		conn.send(l)
		l = f.read(BUFSIZE)
	f.close()
	print('Done sending')
    
if __name__ == "__main__":
   main(sys.argv[1:])