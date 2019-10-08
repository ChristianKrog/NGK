import sys
from socket import * 

HOST = '10.0.0.1'
PORT = 9000
serverAddr= (HOST, PORT)
BUF = 1024

uptime = "/proc/uptime"
loadavg = "/proc/loadavg"


def main(argv):
	# TO DO Your Code
	serverSock = socket(AF_INET, SOCK_DGRAM)
	serverSock.bind(serverAddr)

	while True:
		print 'The server is ready to receive'
		data = serverSock.recvfrom(BUF)
		letter = data[0]
		clientAddr = data[1]
		print 'Letter: "' + letter +'" received from client with address: ' + format(clientAddr)

		if letter  == 'U' or letter  == 'u':
			file1 = open(uptime,"r+")
			fileData1 = file1.read()
			serverSock.sendto(fileData1, clientAddr)
			print 'Uptime sent'

		elif letter  == 'L' or letter == 'l':
			file2 = open(loadavg,"r+")
			fileData2 = file2.read()
			serverSock.sendto(fileData2, clientAddr)
			print 'Loadavg sent'

    
if __name__ == "__main__":
   main(sys.argv[1:])