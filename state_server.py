#!/usr/bin/python2.7

import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class Coordinates(object):

    FILE_NAME = 'states.json'

    '''I found this code snippet in a pure python implementation
    at the following location. Essentially it takes a polygon and x,y coordinates
     and returns a boolean based on whether the point lies within. I decided to reuse this for
    convenience. http://www.ariel.com.au/a/python-point-int-poly.html'''
    def point_inside_polygon(self, x, y, poly):
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

    def parse_states_json_for_match(self, longitude, latitude):
        with open(self.FILE_NAME) as states:
            for line in states:
                data = json.loads(line)
                is_point_in_state = self.point_inside_polygon(latitude, longitude, list(data['border']))
                if is_point_in_state:
                    return data['state']

    def get_state_from_request(self, post_data):
        lat_long = self.get_lat_long_dict(post_data)
        return self.parse_states_json_for_match(float(lat_long['latitude']), float(lat_long['longitude']))

    def get_lat_long_dict(self, post_data):
        try:
            return dict(value.split('=') for value in post_data.split("&"))
        except ValueError:
            return None


class StateServer(BaseHTTPRequestHandler):

    def _set_headers_success(self):
        self.response = self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def _set_headers_failure(self):
        self.response = self.send_response(400)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        request = self.rfile.read(content_length)
        coordinates = Coordinates()
        state = coordinates.get_state_from_request(request)
        self._set_headers_success()
        self.wfile.write(state)

    def do_GET(self):
        self._set_headers_success()
        self.wfile.write("Psst. Send me a post.")


def run(server_class=HTTPServer, handler_class=StateServer, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting server...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
