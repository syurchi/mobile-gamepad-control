import asyncore
from clients import Clients

class SocketHandler(asyncore.dispatcher_with_send):
	def __init__(self, socket):
		self.clients = Clients()
		asyncore.dispatcher_with_send.__init__(self, socket);

	#send data to desktop client
	def __send_to_desktop(self, data):
		clientList = self.clients.get()
		
		#for our purpose there should only be two clients, one desktop, one mobile (for now)
		for c in clientList:
			if c is not self:
				c.send(data)				
				print 'Sending data to desktop client'

	#handle a read() call
	def handle_read(self):
		data = self.recv(8192)
		if data:
			self.__send_to_desktop(data)
			print data