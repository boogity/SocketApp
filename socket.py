# #This will be my socket app, project due later in the semester.

#https://www.tutorialspoint.com/python/python_networking.htm
#Hoping this works
# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)			#Creating socket object
# host = socket.gethostname()						#Gets local machine name
# port = 69696									#Reserving port for socket
# s.bind(host, port)								#Binding socket to ip/port

# s.listen(5)										#Wait for client connection (5) is default behavior
# while True:
# 	c, addr = s.accept()						#Establish connection
# 	print 'Connection established with', addr	
# 	c.send('You are currently connected')
# 	c.close()
	



# https://docs.python.org/2/howto/sockets.html
# 	This tutorial is a bit harder / more complex I think
class mysocket:
    '''demonstration class only
      - coded for clarity, not efficiency
    '''

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)