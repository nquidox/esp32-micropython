import socket
import time

host = "192.168.1.101"
port = 9000

sock = socket.socket()
sock.connect((host, port))

while True:
    sock.send(bytes(1))
    data = sock.recv(4096)
    param_list = data.decode()
    print(param_list)
    time.sleep(1)
