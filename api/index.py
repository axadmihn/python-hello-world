from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write('Hi, this is Jongmin. Call me Mihn'.encode('utf-8'))
        pi=355/113
        radius=7
        area=(pi*radius**2)
        self.int('area')
        return
