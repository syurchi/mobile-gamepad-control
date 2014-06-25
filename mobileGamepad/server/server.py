from BaseHTTPServer import HTTPServer 
import httpHandler
import socketHandler

def main():
	try:
		http = HTTPServer(('0.0.0.0', 9000), httpHandler.httpHandler)
		print 'HTTP server started...'
		http.serve_forever()

	except KeyboardInterrupt:
		print 'HTTP server closed'
		http.socket.close()

if  __name__ =='__main__': main()