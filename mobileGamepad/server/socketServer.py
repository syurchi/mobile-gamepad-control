from socketHandler import SocketHandler
from clients import Clients
from multiprocessing import Process
import asyncore
import socket

class SocketServer(asyncore.dispatcher):
	def __init__(self, host, port):
		self.clients = Clients()
		asyncore.dispatcher.__init__(self)
		self.port = port
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.set_reuse_addr()
		self.bind((host, port))
		self.bind = host
		self.listen(5)

	def __sock_thread(self, socket):
		self.clients.append(socket)
		print 'Stopped adding client'
		self.socketHandler = SocketHandler(self, socket)
		print 'Should have read and printed data'

	#handle when a connection is established and a connect() has been issued, add client
	def handle_accept(self):
		pair = self.accept()
		if pair != None:
			print 'Printing pair '
			print pair
			socket, addr = pair
			self.s = Process(target=self.__sock_thread(socket), args=[])

			try:
				self.s.start()
			except:
				self.s.terminate()

	#handle when connection is closed and remove client
	def handle_close(self):
		self.clients.remove_all()
		self.s.close()
		print 'Sockets closed'