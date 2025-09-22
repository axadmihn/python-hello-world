from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        pi = 355 / 113
        radius = 7
        area = pi * (radius ** 2)
        message = f"Hi, this is Jongmin. Call me Mihn. Area: {int(area)}"
        self.wfile.write(message.encode('utf-8'))

        return
