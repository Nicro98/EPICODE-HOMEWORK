import socket
UDP_IP = "192.168.0.2"
UDP_PORT = int(input("[+] >> INSERISCI LA PORTA\n"))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP , UDP_PORT))
while 1:
	print(" ******** SERVER IN ASCOLTO ********")
	data , addr = sock.recvfrom(4096)
	print("\n\n 2. Il server riceve: ", data, "\n\n")
	print("%s", data)