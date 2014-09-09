from socketHandler import SocketHandler
from clients import Clients
import asyncore
import socket

class SocketServer(asyncore.dispatcher):
	def __init__(self, host, port):
		self.clients = Clients()
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.set_reuse_addr()
		self.bind((host, port))
		self.listen(5)

	#handle when a connection is established and a connect() has been issued, add client
	def handle_accept(self):
		pair = self.accept();
		if pair != None:
			socket, addr = pair
			self.clients.append(socket)
			self.socketHandler = SocketHandler(socket)

	#handle when connection is closed and remove client
	def handle_close(self):
		self.clients.remove_all()
		print 'Sockets closed'