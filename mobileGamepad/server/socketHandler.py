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
	def __create_frame(self, string):
		encoded = ""
		b1 = 0x80

		b1 |= 0x01
		payload = string

		#add FIN flag
		encoded += chr(b1)

		#second byte never masked
		b2 = 0

		length = payload.__len__()
		if length < 126:
			b2 |= length
			encoded += chr(b2)
		elif length < 65535: # 2^16 -1
			b2 |= 126
			encoded += chr(b2)
			x = struct.pack(">H", length)
			encoded += x
		else:
			x = struct.pack(">Q", length)
			b2 = 126
			encoded += chr(b2)
			encoded += x

		encoded += payload

		return str(encoded)

	#decode message from mobile client
	def __decode_message(self, data):
		bytes = [ord(character) for character in data]
		length = bytes[1] & 127 #following eight bytes used for length
		firstMask = 2

		#special cases
		if length == 126:
			firstMask = 4
		elif length == 127:
			firstMask = 10

		#extract masks to find first data byte
		masks = [m for m in bytes[firstMask : firstMask + 4]]
		firstDataByte = firstMask + 4

		decoded = []
		i = firstDataByte
		j = 0

		while i < bytes.__len__():
			#unmask current byte and add to decoded array
			decoded.append(chr(bytes[i] ^ masks[j % 4]))
			i += 1
			j += 1

		return str(decoded)

	#send data to desktop client
	def __send_to_desktop(self, data):
		clientList = self.clients.get()
		print clientList
		
		#for our purpose there should only be two clients, one desktop, one mobile (for now)
		for c in clientList:
			if c is not self:
				encodedData = self.__create_frame(data)
				c.send(encodedData)

	#handle a read() call
	def handle_read(self):
		data = self.recv(8192)
		if data:
			if self.handshaken is False:
				handshake = self.__create_handshake(data)
				self.handshaken = True
				self.send(handshake)
			else:
				decodedMessage = self.__decode_message(data)
				print 'Decoded Message:'
				print decodedMessage
				print '\n\n'
				self.__send_to_desktop(decodedMessage)