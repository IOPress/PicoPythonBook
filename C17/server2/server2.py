# This is Python not MicroPython it is supposed to run
# on a desktop machine
from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
      
    def log_message(self,*args, **kwargs):
        pass

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        bodyString= body.decode(encoding="utf-8")
        temp=float(bodyString)
        print(temp)
        self.send_response(200)
        self.end_headers()

httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
