from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        if self.path == "/":
            self.homepage_handle()
        elif self.path == "/events":

        #self.wfile.write(bytes(json.dumps({'text': 'Hello World'}), 'utf-8'))

    def homepage_handle(self):
        self.wfile.write(bytes("This is the homepage", 'utf-8'))

    def events_handle(self):
        self.wfile.write(bytes("Events handle", 'utf-8'))

    def members_handle(self):
        self.wfile.write(bytes("Members handle", 'utf-8'))

    def transaction_sheet_handle(self):
        self.wfile.write(bytes("Transaction sheet handle", 'utf-8'))

def main():
    web_server = HTTPServer(('localhost', 8080), Server)
    print("local server started at localhost port 8080")
    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    main()
