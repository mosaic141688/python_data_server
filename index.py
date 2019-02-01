#!/usr/bin/python
import numpy as np
import json
import sys

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 3001

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            X = np.random.uniform(0, 10, 1000000).reshape(-1, 2)
	    print(X)
            self.wfile.write(json.dumps(X.tolist()))
            return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER

	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
	sys.exit(0)
