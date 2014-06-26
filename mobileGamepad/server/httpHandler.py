from BaseHTTPServer import BaseHTTPRequestHandler
import re

class httpHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		
		h = self.__parse()

		if self.__isMobile(h['User-Agent']):
			self.__open_file('../client/gamepad.html')
		elif self.__isDesktop(h['User-Agent']):
			self.__open_file('../client/gamepad.html')
		else:
			self.send_error(404, 'Device not supported')
		return

	#parse http headers and put keys and values into a dictionary
	def __parse(self):
		headers = str(self.headers)
		header_dict = dict(re.findall(r"(?P<name>.*?): (?P<value>.*?)\r\n", headers))
		return header_dict

	#returns true if the device is mobile, false otherwise
	def __isMobile(self, str):
		return True if str.count('iPad') > 0 else False

	#returns true if the debice is a desktop, false otherwise
	def __isDesktop(self, str):
		return True if str.count('Linux') > 0 else False

	#open the html template file
	def __open_file(self, path):
		try:
			file = open(path, 'r')
			self.wfile.write(file.read())
			file.close()
		except IOError:
			self.send_error(404, 'File not found')


