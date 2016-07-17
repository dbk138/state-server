#!/usr/bin/python2.7
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class Coordinates:

    FILE_NAME = 'states.json'

    def __init__(self, longitude, latitude):
        self.latitude = latitude
        self.longitude = longitude

    '''http://www.ariel.com.au/a/python-point-int-poly.html'''
    @staticmethod
    def point_inside_polygon(x, y, poly):
        n = len(poly)
        inside = False

        p1x, p1y = poly[0]
        for i in range(n + 1):
            p2x, p2y = poly[i % n]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside

    def parse_states_json_for_match(self):
        with open(self.FILE_NAME) as states:
            for line in states:
                data = json.loads(line)
                inside = self.point_inside_polygon(self.latitude, self.longitude, list(data['border']))
                if inside:
                    return data['state']


class StateServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.response = self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        lat_long = dict(value.split("=") for value in post_data.split("&"))
        coordinates = Coordinates(float(lat_long['latitude']), float(lat_long['longitude']))
        state = coordinates.parse_states_json_for_match()
        print state
        self._set_headers()
        self.wfile.write(state)


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
