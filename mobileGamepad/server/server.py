from BaseHTTPServer import HTTPServer
from httpHandler import HttpHandler
from multiprocessing import Process
import asyncore
import socketServer

def create_http():
	http = HTTPServer(('0.0.0.0', 9000), HttpHandler)
	print 'HTTP server started...'
	http.serve_forever()

def create_sock():
	socketServer.SocketServer('0.0.0.0', 9001)
	print 'Socket server started...'
	asyncore.loop()

def main():
	hs = Process(target=create_http, args=[])
	ss = Process(target=create_sock, args=[])

	try:
		hs.start()
		ss.start()

	except KeyboardInterrupt:
		ss.terminate();
		hs.terminate();
		print 'KeyboardInterrupt: closing servers'

	except Exception as e:
		ss.terminate();
		hs.terminate();
		print 'ERROR: ' + e

if  __name__ =='__main__': main()