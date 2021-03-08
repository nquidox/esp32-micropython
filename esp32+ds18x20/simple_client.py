import socket
import time

host = "192.168.1.101"
port = 9000

sock = socket.socket()
sock.connect((host, port))

print(f"Connecting to {host}:{port}")
counter = 0

while True:
	counter += 1
	sock.send(bytes(1))
	data = sock.recv(4096)
	param_list = data.decode()
	print(f"#{counter}", "[" + str(time.ctime()) + "]", param_list)
	time.sleep(1)
