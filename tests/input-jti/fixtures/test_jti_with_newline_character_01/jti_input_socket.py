'''
	Simple udp socket server
'''
import socket
import sys
HOST = ''	# Symbolic name meaning all available interfaces
PORT = 3000	# Arbitrary non-privileged port
# Datagram (udp) socket
try :
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	print 'Socket created'
except socket.error, msg :
	print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
# Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error , msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()
print 'Socket bind complete'
#now keep talking with the client
ctr = 0
while 1:
	# receive data from client (data, addr)
	d = s.recvfrom(2000)
        ctr += 1
        f = open("file_" + str(ctr) + '.txt', "ab")
	data = d[0]
	addr = d[1]
        f.write(data)
        f.close()
	if not data: 
		break
	reply = 'OK...' + str(addr)
	#s.sendto(reply , addr)
	print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - '
s.close()
