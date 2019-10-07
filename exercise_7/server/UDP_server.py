import sys
from socket import * 
from lib import Lib

HOST = '10.0.0.1'
PORT = 9000
addr= (HOST, PORT)
BUF = 1024

uptime = '/proc/uptime'
loadavg = '/proc/loadavg'


def main(argv):
	# TO DO Your Code
	serverSock = socket(AF_INET, SOCK_DGRAM)
	serverSock.bind(addr)

	while True:
		data = serverSock.recvfrom(BUF)

		if data == ('U' || 'u')
			serverSock.sendto(uptime, addr)

		else if data == ('L' || 'l')
			serverSock.sendto(loadavg, addr)

		else 
			print 'error'

    
if __name__ == "__main__":
   main(sys.argv[1:])