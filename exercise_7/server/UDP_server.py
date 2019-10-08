import sys
from socket import * 

HOST = '10.0.0.1' #server IP
PORT = 9000 
serverAddr= (HOST, PORT) 
BUF = 1024

uptime = "/proc/uptime"   #filedirectory
loadavg = "/proc/loadavg" #filedirectory


def main(argv):
	serverSock = socket(AF_INET, SOCK_DGRAM) #create UDP socket
	serverSock.bind(serverAddr) #bind socket to the serveraddress 

	while True:
		print 'The server is ready to receive'
		data = serverSock.recvfrom(BUF) #Waiting for client to send something. 
		letter = data[0] #extract message (letter)
		clientAddr = data[1] #extract clientaddress. 
		print 'Letter: "' + letter +'" received from client with address: ' + format(clientAddr)

		if letter  == 'U' or letter  == 'u':
			file1 = open(uptime,"r+") #open file for reading 
			fileData1 = file1.read() #read content of file 
			serverSock.sendto(fileData1, clientAddr) #send content
			print 'Uptime sent'

		elif letter  == 'L' or letter == 'l':
			file2 = open(loadavg,"r+") #open file for reading 
			fileData2 = file2.read() #read content of file 
			serverSock.sendto(fileData2, clientAddr) #send content
			print 'Loadavg sent'

    
if __name__ == "__main__":
   main(sys.argv[1:])

   