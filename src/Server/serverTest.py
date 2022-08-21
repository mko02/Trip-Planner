from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib import parse

class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        self._set_headers()

        self.wfile.write(bytes(json.dumps({'text': 'Hello World'}), 'utf-8'))

    def get_trip_list(self):
        self.wfile.write(bytes("This is the homepage", 'utf-8'))

    def events_handle(self):
        self.wfile.write(bytes("Events handle", 'utf-8'))

    def members_handle(self):
        self.wfile.write(bytes("Members handle", 'utf-8'))

    def transaction_sheet_handle(self):
        self.wfile.write(bytes("Transaction sheet handle", 'utf-8'))

    def do_POST(self):
        self._set_headers()
        data_string = self.rfile.read(int(self.headers['Content-Length']))
        data = json.loads(data_string)
        print(data)
        print(type(data))
        self.wfile.write(bytes("POST request retrieved", 'utf-8'))

    def update_event_handle(self):
        self.wfile.write(bytes("Event updated", 'utf-8'))

    def update_member_handle(self):
        self.wfile.write(bytes("Member updated", 'utf-8'))

    def update_cost_handle(self):
        self.wfile.write(bytes("Cost updated", 'utf-8'))

    def parse_path(self) -> dict:
        return dict(parse.parse_qsl(parse.urlsplit(self.path).query))



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
