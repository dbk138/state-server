import urlparse
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class StateServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.response = self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        length = int(self.headers['Content-Length'])
        post_data = urlparse.parse_qs(self.rfile.read(length))
        for key, value in post_data.iteritems():
            print "%s=%s" % (key, value)

        self._set_headers()
        self.wfile.write("This is a post request.")


def run(server_class=HTTPServer, handler_class=StateServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print
    'Starting httpd...'
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()

'''
with open("states.json") as file:
    for line in file:
        data = json.loads(line)
        print('State: ' + str(data['state']) + ', Borders:' + str(data['border']))
'''