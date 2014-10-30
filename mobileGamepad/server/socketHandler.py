import asyncore
from hashlib import sha1
from base64 import b64encode
from clients import Clients
from parse import httpParse

class SocketHandler(asyncore.dispatcher_with_send):
	handshake = (
        'HTTP/1.1 101 Web Socket Protocol Handshake\r\n'
        'Upgrade: WebSocket\r\n'
        'Connection: Upgrade\r\n'
        'WebSocket-Origin: %(origin)s\r\n'
        'WebSocket-Location: ws://%(bind)s:%(port)s/\r\n'
        'Sec-Websocket-Origin: %(origin)s\r\n'
        'Sec-Websocket-Location: ws://%(bind)s:%(port)s/\r\n'
        'Sec-Websocket-Accept: %(response)s\r\n'
        '\r\n'
	)

	def __init__(self, server, socket):
		self.clients = Clients()
		self.server = server
		self.handshaken = False
		asyncore.dispatcher_with_send.__init__(self, socket);

	def __create_handshake(self, headers):
		print 'Beginning handshake...'
		print headers
		
		h = httpParse(headers)

		#create response key for handshake accept
		guid = '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
		key = h['Sec-WebSocket-Key']
		response_key = b64encode(sha1(key + guid).digest())

		handshake = SocketHandler.handshake % {
			'origin': h['Origin'], 
			'port': self.server.port, 
			'bind': self.server.bind, 
			'response': response_key
		}
		return handshake

	#TODO: encode message frame to send message to desktop client
	def __create_frame(self, data):
		pass

	#TODO: decode message from mobile client
	def __decode_message(self, data):
		pass

	#send data to desktop client
	def __send_to_desktop(self, data):
		clientList = self.clients.get()
		print clientList
		
		#for our purpose there should only be two clients, one desktop, one mobile (for now)
		for c in clientList:
			print c
			if c is not self:
				newData = self.__create_frame(data)
				c.send(newData)				
				print 'Sending data to desktop client'

	#handle a read() call
	def handle_read(self):
		data = self.recv(8192)
		print 'reading...\n'
		if data:
			if self.handshaken is False:ya 
				handshake = self.__create_handshake(data)
				self.handshaken = True
				self.send(handshake)
			else:
				self.__send_to_desktop(data)
				print data