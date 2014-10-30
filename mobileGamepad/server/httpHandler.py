from BaseHTTPServer import BaseHTTPRequestHandler
# import re
from parse import httpParse

class HttpHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		h = httpParse(self.headers)

		#TODO: check only if mobile, otherwise assume desktop
		#TODO: create dictionary, with key stating if client is desktop or not -> isMobile: true
		if self.path == '/':
			if self.__is_mobile(h['User-Agent']):
				self.__open_file('/home/syurchi/Documents/programming/projects/mobileGamepad/mobileGamepad/client/gamepad.html')
			elif self.__is_desktop(h['User-Agent']):
				self.__open_file('/home/syurchi/Documents/programming/projects/mobileGamepad/mobileGamepad/client/game.html')
			else:
				self.send_error(404, 'Device not supported')
		elif self.path == '/home/syurchi/Documents/programming/projects/mobileGamepad/mobileGamepad/server/socketServer':
			self.__open_file('/home/syurchi/ififDocuments/programming/projects/mobileGamepad/mobileGamepad/server/socketServer.py')
		else:
			#add appropriate path prefix
			path = '/home/syurchi/Documents/programming/projects/mobileGamepad/mobileGamepad/client/' + self.path
			self.__open_file(path)
		return

	#returns true if the device is mobile, false otherwise
	def __is_mobile(self, str):
		return True if ((str.count('Android') > 0) | (str.count('iPad') > 0)) else False

	#returns true if the debice is a desktop, false otherwise
	def __is_desktop(self, str):
		return True if str.count('Linux') > 0 else False

	#open the html template file
	def __open_file(self, path):
		try:
			file = open(path, 'r')
			self.wfile.write(file.read())
			file.close()
		except IOError:
			self.send_error(404, 'File not found')

