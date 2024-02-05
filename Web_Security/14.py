from http.server import SimpleHTTPRequestHandler, HTTPServer

class WebHandler(SimpleHTTPRequestHandler):
    def handle_request(self):
        print('\n' + str(self.headers).strip() + '\n')
        contentLength = int(self.headers.get('Content-Length', 0))
        if contentLength:
            print(self.rfile.read(contentLength))
            print()
        self.send_response(200)
        self.end_headers()
    def do_POST(self):
        self.handle_request()
        response = ""
        self.wfile.write(bytes(response, "UTF-8"))

server_address = ("127.0.0.1", 8000)
server = HTTPServer(server_address, WebHandler)
server.serve_forever()
