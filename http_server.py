import http.server
import socketserver
import socket
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(socket.gethostname().encode())

httpd = socketserver.TCPServer(('', 80), Handler)
httpd.serve_forever()
