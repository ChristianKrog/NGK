import sys
from socket import *
from lib import Lib

HOST = '10.0.0.1' #server IP
PORT = 9000
BUFSIZE = 1000

def main(argv):
	fileName = sys.argv[1] #input from terminal when compiling
	clientSock = socket(AF_INET, SOCK_STREAM) #create tcp socket
	clientSock.connect((HOST,PORT)) #connect socket to the server address 

	print("Connected to server")

	Lib.writeTextTCP(fileName,clientSock) #writes filename to server
	
	receiveFile(fileName, clientSock) #calls recieveFile()

def receiveFile(fileName,  conn):
	fileSize = Lib.getFileSizeTCP(conn) 
	if fileSize == 0: #checks if file exist
		print("Filesize is 0. File doesn't exist")
		conn.close() #close connection to the server
	else:
		print 'Filesize is: ', fileSize
		print("Starting download")

	f = open("fileName", "wb") #open file or create. write binary. 
	receivedData = conn.recv(BUFSIZE) #Reads the first 1000 bytes sent from server
	f.write(receivedData) #write the first chunk of the file
	receivedTotal = len(receivedData) #sets the total number of bytes recieved 
		
	while receivedTotal < fileSize: #runs until total number of recieved bytes is larger or equal to filesize
		receivedData = conn.recv(BUFSIZE) #reads chunks of 1000 bytes sent from server
		f.write(receivedData) #writes the received data to file 
		receivedTotal += len(receivedData) #keeps count on the total number og bytes received. 
	
	print("Dowload completed. Client will close")
	conn.close() #close connection to server. 
		
if __name__ == "__main__":
   main(sys.argv[1:])
