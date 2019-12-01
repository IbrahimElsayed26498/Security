from socket import *
import sys
s = socket()
host = "127.0.0.1"
port = 9999
s.bind((host, port))
s.listen(5)
c, a = s.accept()
print("Connection from", a[0])
cd = c.recv(2024).decode("utf-8")
print(cd, end="")
while True:
	cmd = input()
	if cmd == 'q':
		s.close()
		c.close()
		sys.exit()
	if len(cmd) > 0 :
		c.send(cmd.encode("utf-8"))
		print(c.recv(2048).decode("utf-8"), end="")