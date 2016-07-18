#!/usr/bin/python2.7
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class PointInState(object):

    FILE_NAME = 'states.json'

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def point_inside_polygon(self, x, y, poly):
        """For convenience, I decided to reuse this point-in-polygon method that
        I found using a pure python implementation at the location below.
        x,y are longitude and latitude points
        poly is a list of coordinates that form a polygon.
        Returns a boolean based on whether the point lies within.
        http://www.ariel.com.au/a/python-point-int-poly.html
        """

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

    def get_state_from_point(self):
        """
        Opens and parses the states.json file to determine
        if a given point falls between the border coordinates.
        If we are going off of ISO 6709: https://en.wikipedia.org/wiki/ISO_6709
        then longitude should be passed as the x value and latitude will be the y value.
        :returns the name of the state based off given lat/lon otherwise None
        """
        with open(self.FILE_NAME) as states:
            for line in states:
                data = json.loads(line)
                is_point_in_state = self.point_inside_polygon(self.longitude, self.latitude, list(data['border']))
                if is_point_in_state:
                    return data['state']


class StateServer(BaseHTTPRequestHandler):

    def _set_headers_success(self):
        """
        Sets the headers for a successful operation.
        Returns a 200 response to the user.
        """
        self.response = self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def _set_headers_failure(self):
        """
        Sets the headers for a failure scenario.
        Returns a 400 response to the user.
        """
        self.response = self.send_response(400)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def set_failure(self, msg):
        """
        Calls the set header method and writes a failure message to the user.
        :param msg: The failure message displayed to the user.
        """
        self._set_headers_failure()
        self.wfile.write(msg)

    def do_POST(self):
        """
        Handles POST requests sent to http://localhost:8080
        If the data from the request cannot be parsed or if
        no state is found for the given lat/lon then a 400
        is returned. Otherwise, if successful, the name of the
        state is returned.
        """
        content_length = int(self.headers['Content-Length'])
        request = self.rfile.read(content_length)
        lat_long = PointUtils().parse_request_for_lat_long(request)
        if not lat_long:
            self.set_failure('Invalid request. Proper format is "latitude=xx.xxx&longitude=-yy.yyy".')
            return
        point = PointInState(lat_long['latitude'], lat_long['longitude'])
        state = point.get_state_from_point()
        if not state:
            self.set_failure('No state found for given coordinates.')
            return
        self._set_headers_success()
        self.wfile.write(state)

    def do_GET(self):
        """
        No get available, display a 404.
        """
        self.send_error(404)
        return


class PointUtils(object):

    def parse_request_for_lat_long(self, post_data):
        """
        Utility method used to return the latitude and longitude as a dictionary
        :param post_data: the request from the HTTP POST
        :return: a lat/lon dict or None if an error occurs.
        """
        try:
            lat_long = dict(value.split('=') for value in post_data.split('&'))
            lat_long['latitude'] = float(lat_long['latitude'])
            lat_long['longitude'] = float(lat_long['longitude'])
            return lat_long
        except ValueError:
            return None
        except KeyError:
            return None

if __name__ == "__main__":
    server = HTTPServer(('localhost', 8080), StateServer)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
