#create a clients list to keep track of the mobile and desktop clients
class Clients():
	def __init__(self):
		self.clients = []

	#check to see if client exists or not
	def __isNewClient(self, client):
		return client in self.clients

	def append(self, client):
		if self.__isNewClient(client) == False:
			print 'Adding client'
			self.clients.append(client)
		else:
			#TODO: add better error handling
			print 'Client already exists'

	def get(self):
		return self.clients

	def remove_all(self):
		while self.clients.__len__():
			self.clients.pop()