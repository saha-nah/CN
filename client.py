
import socket			
s = socket.socket()		
port = 7			
s.connect(('127.0.0.1', port))
print (s.recv(1024).decode())
s.close()	
	
