import unittest

from state_server import PointInState
from state_server import PointUtils


class StateTests(unittest.TestCase):

    def test_point_in_polygon_true(self):
        print 'Running test_point_in_polygon_true...'
        state_border = [[-77.475793, 39.719623], [-80.524269, 39.721209], [-80.520592, 41.986872], [-74.705273, 41.375059], [-75.142901, 39.881602], [-77.475793, 39.719623]]
        point = PointInState(40.513799, -77.036133)
        is_point_in_state = point.point_inside_polygon(point.longitude, point.latitude, state_border)
        self.assertEqual(is_point_in_state, True)

    def test_point_in_polygon_false(self):
        print 'Running test_point_in_polygon_false...'
        state_border = [[-77.475793, 39.719623], [-80.524269, 39.721209], [-80.520592, 41.986872], [-74.705273, 41.375059], [-75.142901, 39.881602], [-77.475793, 39.719623]]
        point = PointInState(37.129269, -85.085177)
        is_point_in_state = point.point_inside_polygon(point.longitude, point.latitude, state_border)
        self.assertEqual(is_point_in_state, False)

    def test_parse_request_for_lat_long(self):
        print 'Running test_parse_request_for_lat_long...'
        request = "latitude=40.513799&longitude=-77.036133"
        lat_long = PointUtils().parse_request_for_lat_long(request)
        self.assertEqual(lat_long['latitude'], 40.513799)
        self.assertEqual(lat_long['longitude'], -77.036133)

    def test_parse_request_for_lat_long_blank_value(self):
        print 'Running test_parse_request_for_lat_long_blank_value...'
        request = "latitude=&longitude="
        lat_long = PointUtils().parse_request_for_lat_long(request)
        assert lat_long is None

    def test_parse_request_for_lat_long_half_value(self):
        print 'Running test_parse_request_for_lat_long_half_value...'
        request = "latitude=40.513799"
        lat_long = PointUtils().parse_request_for_lat_long(request)
        assert lat_long is None

    def test_parse_request_for_lat_long_missing_value(self):
        print 'Running test_parse_request_for_lat_long_missing_value...'
        request = "latitude=40.513799&longitude="
        lat_long = PointUtils().parse_request_for_lat_long(request)
        assert lat_long is None

    def test_parse_request_for_lat_long_invalid_value(self):
        print 'Running test_parse_request_for_lat_long_invalid_value...'
        request = "blah blah blah hello& =world"
        lat_long = PointUtils().parse_request_for_lat_long(request)
        assert lat_long is None

    """Test a few random points along state borders and within states to check for accuracy"""

    def test_get_state_from_point_pa(self):
        print 'Running test_get_state_from_point_pa...'
        point = PointInState(40.513799, -77.036133)
        state = point.get_state_from_point()
        self.assertEqual(state, 'Pennsylvania')

    def test_get_state_from_point_ok(self):
        print 'Running test_get_state_from_point_ok...'
        point = PointInState(35.485162, -96.893323)
        state = point.get_state_from_point()
        self.assertEqual(state, 'Oklahoma')

    def test_get_state_from_point_wv(self):
        print 'Running test_get_state_from_point_wv...'
        point = PointInState(39.511637, -80.645768)
        state = point.get_state_from_point()
        self.assertEqual(state, 'West Virginia')

    def test_get_state_from_point_sd(self):
        print 'Running test_get_state_from_point_sd...'
        point = PointInState(44.414159, -103.514929)
        state = point.get_state_from_point()
        self.assertEqual(state, 'South Dakota')

    def test_get_state_from_point_nv(self):
        print 'Running test_get_state_from_point_nv...'
        point = PointInState(35.978121, -114.834509)
        state = point.get_state_from_point()
        self.assertEqual(state, 'Nevada')

    def test_get_state_from_point_az(self):
        print 'Running test_get_state_from_point_az...'
        point = PointInState(34.233012, -114.122451)
        state = point.get_state_from_point()
        self.assertEqual(state, 'Arizona')


if __name__ == '__main__':
    unittest.main()
