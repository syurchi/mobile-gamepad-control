#create a clients list to keep track of the mobile and desktop clients
clients = []

class Clients():
	def __init__(self):
		self.clients = clients

	#check to see if client exists or not
	def __isNewClient(self, client):
		return client in self.clients

	def append(self, client):
		if self.clients == None:
			self.clients = [client]
		elif self.__isNewClient(client) == False:
			print 'Adding client\n'
			self.clients.append(client)
		else:
			#TODO: add better error handling
			print 'Client already exists\n'

	def get(self):
		return self.clients

	def remove_all(self):
		while self.clients.__len__():
			self.clients.pop()