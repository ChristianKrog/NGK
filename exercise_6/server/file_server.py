import sys
from socket import * 
from lib import Lib

HOST = '10.0.0.1' #server IP
PORT = 9000
BUFSIZE = 1000

def main(argv):
	serverSock = socket(AF_INET, SOCK_STREAM) #create TCP socket
	serverSock.bind((HOST,PORT)) #Bind socket to IP og port(address)
	serverSock.listen(1) #waiting for client to connect. 
	print 'The server is ready to receive'
	
	while True: 
		conn, addr = serverSock.accept() #completes connection with client
		print 'Connected to client - Port - ', PORT
		txtClient = Lib.readTextTCP(conn) #Reads file and directory from client
		fileName = Lib.extractFilename(txtClient) 
		fileSize = str(Lib.check_File_Exists(fileName)) 
		Lib.writeTextTCP(fileSize, conn) #send filesize to client. 
		sendFile(fileName,fileSize,conn) #calls sendfile()


def sendFile(fileName,  fileSize,  conn):
	f = open(fileName, 'rb') #opens the file for binary read. 
	dataTosend = f.read(BUFSIZE) #reads the first 1000 bytes
	
	while dataTosend: 
		conn.send(dataTosend) #sends file in chunks of 1000 bytes
		
		dataTosend = f.read(BUFSIZE) #reads chunks of 1000 bytes until finished
	print('Done sending')
	f.close() #close file

    
if __name__ == "__main__":
   main(sys.argv[1:])



