from http.server import BaseHTTPRequestHandler, HTTPServer
import json

'''
    Still trying to figure out how to build a server in Python
'''
class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(json.dumps({'text': 'Hello World'}), 'utf-8'))

def main():
    webServer = HTTPServer(('localhost', 8080), Server)
    print("local server started at localhost port 8080")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")

if __name__ == "__main__":
    main()
