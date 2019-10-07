import sys
from socket import * 
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
BUFSIZE = 1000

def main(argv):
	# TO DO Your Code
	serverSock = socket(AF_INET, SOCK_STREAM)
	serverSock.bind((HOST,PORT))
	serverSock.listen(1)
	print 'The server is ready to receive'
	
	while True: 
		conn, addr = serverSock.accept()
		print 'Connected to client - Port - ', PORT
		txtClient = Lib.readTextTCP(conn)
		fileName = Lib.extractFilename(txtClient)
		fileSize = str(Lib.check_File_Exists(fileName))
		Lib.writeTextTCP(fileSize, conn)
		sendFile(fileName,fileSize,conn)


def sendFile(fileName,  fileSize,  conn):
	# TO DO Your Code
	f = open(fileName, 'rb')
	dataTosend = f.read(BUFSIZE)
	
	while dataTosend: 
		conn.send(dataTosend)
		
		dataTosend = f.read(BUFSIZE)
	print('Done sending')
	f.close()

    
if __name__ == "__main__":
   main(sys.argv[1:])